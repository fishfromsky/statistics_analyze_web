import numpy as np
import os
import pandas as pd
from scipy.stats import pearsonr
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler, scale
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示负号
import seaborn as sns
from numpy import *
import sys
import json
import requests
import os
from pandas import json_normalize


np.set_printoptions(suppress=True)

project_id = sys.argv[1]
algorithm = sys.argv[2]


class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        """
        只要检查到了是bytes类型的数据就把它转为str类型
        :param obj:
        :return:
        """
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


def ployinterp_column(s, n, k=2):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 - k))]
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


def plotinterplate_columns(s, n, k=5):
    y = s.iloc[list(range(n-k,n)) + list(range(n+1, n+1+k))]
    y = y[y.notnull()]  # 剔除空值
    return lagrange(y.index, list(y))(n)  # 向位置n出插值并返回该插值结果  y.index返回的是费缺失值在原来列表中的位置

# #拉格朗日插值法进行插值
# def deal_csv():
#     b = pd.read_csv('newxxxx.csv').columns.values[:]
#     # use_col = pd.read_csv('newest.csv').columns.values[3:16]
#     # dataset1 = pd.read_csv('newest.csv', usecols=use_col)
#     dataset2 = pd.read_csv('newxxxx.csv', usecols=b)
#     # 缺失值处理
#     # for i in dataset1.columns:
#     #     for j in range(len(dataset1)):
#     #         if (dataset1[i].isnull())[j] and j>=2:
#     #             dataset1[i][j] = ployinterp_column(dataset1[i], j)
#     for i in dataset2.columns:
#         for j in range(len(dataset2)):
#             if (dataset2[i].isnull())[j] and j>=2:
#                 dataset2[i][j] = ployinterp_column(dataset2[i], j)
#     # dataset2=pd.concat([dataset1, dataset2], axis=1)
#     dataset2.to_csv('dataset_newxx.csv')

#excel转csv
def xlsx_to_csv_pd(filename):
    (filepath, tempfilename) = os.path.split(filename);
    (shotname, extension) = os.path.splitext(tempfilename);
    data_xls = pd.read_excel(tempfilename, index_col=0)
    data_xls.to_csv(shotname+'.csv', encoding='utf_8_sig')
    temppath = shotname+'.csv'

    return temppath

#拉格朗日插值法进行插值
def deal2_csv(temppath):
    dataset = pd.read_csv(temppath,low_memory=False)
    cols = dataset.columns
    for col in cols:
        if str(dataset[col].dtype) == 'object':  # 删除非数值的列
            dataset = dataset.drop(col, axis=1)
    for i in dataset.columns[:]:
        for j in range(len(dataset)):
            if (dataset[i].isnull())[j]:
                dataset.loc[j,i] = plotinterplate_columns(dataset[i], j)
    name = 'newdata（拉格朗日插值法）.csv'
    dataset.to_csv(name,encoding='utf_8_sig')

    return name


# 直接丢掉有空格的数据项
def deal1_csv(temppath):
    dataset = pd.read_csv(temppath,low_memory=False)
    dataset = dataset.dropna(axis=0, how='any')
    cols = dataset.columns
    for col in cols:
        if str(dataset[col].dtype) == 'object':#删除非数值的列
            dataset = dataset.drop(col, axis=1)
    datasetname = 'newdata（删除空行+非数值）.csv'
    dataset.to_csv(datasetname, encoding='utf_8_sig')

    return datasetname



def read_csv():
    dataset = pd.read_csv('dataset_new1.csv')
    dataset = dataset.drop(dataset.columns[[0]], axis=1)
    labels = dataset.columns
    dataset = dataset.values
    return dataset, labels


def deal_data(dataset):
    labels = dataset.columns
    scaler = MinMaxScaler()
    dataset = scaler.fit_transform(dataset)
    labels = labels[:-1]
    x = dataset[:, :-1]
    y = dataset[:, -1]
    gbdt = GradientBoostingClassifier(max_depth=6, n_estimators=500, random_state=0)
    gbdt.fit(x, y.astype('int'))
    showbar(labels, gbdt, 'GBDT')


def showbar(labels, model, method):
    feature_importance_df = pd.DataFrame({
        'name': labels,
        'importance': model.feature_importances_
    })
    feature_importance_df.sort_values(by='importance', ascending=False, inplace=True)
    x_axis = list(feature_importance_df['name'])
    y_axis = list(feature_importance_df['importance'])
    json_data = {}
    json_data['project_id'] = project_id
    result_list = []
    for i in range(len(x_axis)):
        dict = {}
        dict['label'] = x_axis[i]
        dict['value'] = y_axis[i]
        result_list.append(dict)
    json_data['data'] = result_list
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/save_relation_RF_result', data=json_data)
    # plt.subplots(figsize=(20, 10))
    # plt.title('importance factors of residential garbage')
    # plt.ylabel('importance')
    # plt.xlabel('factors')
    # plt.xticks(fontsize=9, rotation=30)
    # plt.bar(x_axis, y_axis)
    # if method == 'GBDT':
    #     plt.savefig('GBDT_importance.png')
    # if method == 'RF':
    #     plt.savefig('RF_importance.png')
    # plt.show()


def hot_matrix(dataset):
    corr_matrix = dataset.corr()
    json_data = {}
    json_data['project_id'] = project_id
    result_list = []
    labels = list(corr_matrix.columns)
    dataframe = corr_matrix.values
    for i in range(len(labels)):
        dict = {}
        dict['label'] = labels[i]
        dict['year'] = dataframe[:, 0][i]
        dict['garbage_clear'] = dataframe[:, 1][i]
        dict['population'] = dataframe[:, 2][i]
        dict['city_rural_ratio'] = dataframe[:, 3][i]
        dict['household'] = dataframe[:, 4][i]
        dict['people_per_capita'] = dataframe[:, 5][i]
        dict['sex_ratio'] = dataframe[:, 6][i]
        dict['age_0_14'] = dataframe[:, 7][i]
        dict['age_15_64'] = dataframe[:, 8][i]
        dict['age_65'] = dataframe[:, 9][i]
        dict['disposable_income'] = dataframe[:, 10][i]
        dict['consume_cost'] = dataframe[:, 11][i]
        dict['public_cost'] = dataframe[:, 12][i]
        dict['gdp'] = dataframe[:, 13][i]
        dict['gdp_first_industry'] = dataframe[:, 14][i]
        dict['gdp_second_industry'] = dataframe[:, 15][i]
        dict['gdp_third_industry'] = dataframe[:, 16][i]
        dict['gnp'] = dataframe[:, 17][i]
        dict['education'] = dataframe[:, 18][i]
        result_list.append(dict)
    json_data['data'] = result_list
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/save_relation_hot_matrix_result', data=json_data)

    # plt.subplots(figsize=(12, 12))
    # sns.heatmap(corr_matrix, annot=True, vmax=1, square=True, yticklabels=dataset.columns, xticklabels=dataset.columns, cmap="YlGnBu",annot_kws={'size':7})
    # plt.savefig('heatmap.png')
    # plt.show()


def RF(dataset):
    scaler = MinMaxScaler()
    dataset = dataset.drop(dataset.columns[[0]], axis=1)
    labels = dataset.columns.values
    dataset = scaler.fit_transform(dataset)
    labels = labels[1:]
    x = dataset[:, 1:]
    y = dataset[:, 0]
    forest = RandomForestClassifier(n_estimators=500, max_depth=6, random_state=0)
    forest.fit(x, y.astype('int'))
    showbar(labels, forest, 'RF')


def plot_lostdata():
    dataset, labels = read_csv()
    plt.figure()
    ax = plt.gca()
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")

    plt.tight_layout()
    plt.xticks([x for x in range(2000, 2020)])
    line1 = dataset[:16, 10]
    line2 = dataset[15:, 10]
    plt.plot([x for x in range(2000, 2016)], line1, label='fact')
    plt.plot([x for x in range(2015, 2020)], line2, color='orange', linestyle='--', label='lost')
    plt.title('GDP Growth Rate')
    plt.legend()
    plt.show()


def GRA_ONE(DataFrame, m=0):
    gray=DataFrame
    #读取为df格式
    gray=(gray - gray.min()) / (gray.max() - gray.min())
    #标准化
    std=gray.iloc[:, m]#为标准要素
    ce=gray.iloc[:, 0:]#为比较要素
    n=ce.shape[0]
    m=ce.shape[1]#计算行列

    #与标准要素比较，相减
    a=zeros([m,n])
    for i in range(m):
        for j in range(n):
            a[i,j]=abs(ce.iloc[j,i]-std[j])

    #取出矩阵中最大值与最小值
    c=amax(a)
    d=amin(a)

    #计算值
    result=zeros([m,n])
    for i in range(m):
        for j in range(n):
            result[i,j]=(d+0.5*c)/(a[i,j]+0.5*c)

    #求均值，得到灰色关联值
    result2=zeros(m)
    for i in range(m):
            result2[i]=mean(result[i,:])
    RT=pd.DataFrame(result2)
    return RT


def GRA(DataFrame):
    list_columns = [str(s) for s in range(len(DataFrame.columns)) if s not in [None]]
    df_local = pd.DataFrame(columns=list_columns)
    for i in range(len(DataFrame.columns)):
        df_local.iloc[:,i] = GRA_ONE(DataFrame,m=i)[0]
    return df_local


def ShowGRAHeatMap(DataFrame, labels):
    colormap = plt.cm.RdBu
    plt.figure(figsize=(14, 12))
    plt.title('Gray Relation', y=1.05, size=15)
    sns.heatmap(DataFrame.astype(float), xticklabels=labels, yticklabels=labels, linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True,annot_kws={'size':7})
    plt.show()
    plt.savefig('gray_relate.png')


def gray_relate(dataset):
    dataframe = dataset
    dataframe = dataframe.drop(dataframe.columns[[0]], axis=1)
    cols = dataframe.columns.values
    data_gray = GRA(dataframe)
    # ShowGRAHeatMap(data_gray, cols)

    dataframe = data_gray.values

    json_data = {}
    json_data['project_id'] = project_id
    result_list = []
    labels = cols
    for i in range(len(labels)):
        dict = {}
        dict['label'] = labels[i]
        dict['garbage_clear'] = dataframe[:, 0][i]
        dict['population'] = dataframe[:, 1][i]
        dict['city_rural_ratio'] = dataframe[:, 2][i]
        dict['household'] = dataframe[:, 3][i]
        dict['people_per_capita'] = dataframe[:, 4][i]
        dict['sex_ratio'] = dataframe[:, 5][i]
        dict['age_0_14'] = dataframe[:, 6][i]
        dict['age_15_64'] = dataframe[:, 7][i]
        dict['age_65'] = dataframe[:, 8][i]
        dict['disposable_income'] = dataframe[:, 9][i]
        dict['consume_cost'] = dataframe[:, 10][i]
        dict['public_cost'] = dataframe[:, 11][i]
        dict['gdp'] = dataframe[:, 12][i]
        dict['gdp_first_industry'] = dataframe[:, 13][i]
        dict['gdp_second_industry'] = dataframe[:, 14][i]
        dict['gdp_third_industry'] = dataframe[:, 15][i]
        dict['gnp'] = dataframe[:, 16][i]
        dict['education'] = dataframe[:, 17][i]
        result_list.append(dict)
    json_data['data'] = result_list
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/save_grey_relation_result', data=json_data)


# 归一化
def guiyihua():

    params = {'project_id': project_id}
    res = requests.get('http://127.0.0.1:8000/api/get_relation_parameter', params=params)
    json_data = json.loads(res.text).get('data')

    df = json_normalize(json_data)
    df = df.drop(df.columns[[df.shape[1] - 1]], axis=1)

    dataset = df.drop(df.columns[[0]], axis=1)

    datasety = dataset
    labels = dataset.columns
    dataset = dataset.values
    for i in range(dataset.shape[0]):
        for j in range(dataset.shape[1]):
            if isinstance(dataset[i][j], str):
                if dataset[i][j].isspace():
                    dataset[i][j].strip()
    k=[]
    for i in range(dataset.shape[1]):
        p = normalization(dataset[:, i])

        if i == 0: k = p
        else:
            k=np.c_[k, p]
    df = pd.DataFrame(k, columns=labels)
    return df, datasety


def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range


def get_pearsonr(dataset):
    dataset = dataset.drop(dataset.columns[[0]], axis=1)
    cols = list(dataset.columns.values)
    cols.pop(0)
    dataset = dataset.values
    scaler = MinMaxScaler()
    dataset = scaler.fit_transform(dataset)
    corr_list = list()
    n = dataset.shape[1]
    for i in range(1, n):
        p = pearsonr(dataset[:, i], dataset[:, 0])
        corr_list.append(p)

    json_data = {}
    json_data['project_id'] = project_id
    result_list = []
    labels = cols
    for i in range(len(labels)):
        dict = {}
        dict['label'] = labels[i]
        dict['relate'] = corr_list[i][0]
        dict['p_value'] = corr_list[i][1]
        result_list.append(dict)
    json_data['data'] = result_list
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/save_pearson_result', data=json_data)
    return corr_list


if __name__ == '__main__':

    dataset, datasety = guiyihua() # 归一化
    if algorithm == '1':
        hot_matrix(dataset) # 相关系数热力图
    if algorithm == '2':
        RF(dataset)
    if algorithm == '3':
        gray_relate(dataset)
    if algorithm == '4':
        get_pearsonr(dataset)

    dict = {}
    dict['project_id'] = project_id
    data = json.dumps(dict)
    requests.post('http://127.0.0.1:8000/api/stop_relation', data=data)