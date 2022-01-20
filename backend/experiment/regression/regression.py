import json
import numpy as np
import sys
import requests
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler,PolynomialFeatures
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LassoCV, RidgeCV
import os
import datetime

file_path = sys.argv[1]
drop_col = sys.argv[2]
special = sys.argv[3]
user = sys.argv[4]
algorithm_id = sys.argv[5]
model_id = sys.argv[6]

special = int(special)

drop_index = drop_col.split(',')
drop_index = list(map(int, drop_index))


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


def yuchuli(file_path):
    global special
    alphaslist = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100, 1000, 10000]  # alphas列表
    df = pd.read_excel(file_path)
    head_list = df.columns.values
    special_head = head_list[special]
    drop_index.remove(special)
    dataset = df.drop(df.columns[drop_index], axis=1)
    new_head_list = dataset.columns.values
    new_special = list(new_head_list).index(special_head)
    special = new_special    # 获取筛选列过后的数据集中特征所在列的下标

    # h = 13  # 第几个城市
    # dataset = dataset[20 * h - 20:20 * h]
    dataset = dataset.fillna(0.1)
    y = dataset.iloc[:, special]
    x = dataset.drop(dataset.columns[[special]], axis=1)
    po = PolynomialFeatures(degree=2, interaction_only=False, include_bias=False)
    x_poly = po.fit_transform(x)
    x_change = pd.DataFrame(x_poly, columns=po.get_feature_names())
    labels = x_change.columns
    X_train, X_test, Y_train, Y_test = train_test_split(x_change, y, test_size=0.2, random_state=1)
    model2 = LassoCV(alphas=alphaslist)  # 导入模型传入参数alpha=0.1
    model2.fit(X_train, Y_train)  # 训练数据
    # model2 = Lasso(max_iter = iterations, alphas=1).fit(X_train,Y_train)
    index = model2.coef_
    newindex = []
    if len(labels) == len(index):
        for i in range(len(index)):
            if index[i] >= 0.00001 and i != 0:  # 选择系数值绝对值大于等于0.00001的系数
                pass
            else:
                pass
            if abs(index[i]) >= 0.00001:
                newindex.append(i)
    ypre = model2.predict(X_test)
    x_changenew = x_change.iloc[:, newindex]  # 形成新的dataset

    # 选择新的特征系数重新进行线性回归————————————————————————————————————————————————————————————————————————————————————-———

    X_train, X_test, Y_train, Y_test = train_test_split(x_changenew, y, test_size=0.2, random_state=1)
    model2 = RidgeCV(alphas=alphaslist)  # 导入模型传入参数alpha=0.1
    model2.fit(X_train, Y_train)  # 训练数据
    # model2 = Lasso(max_iter=iterations).fit(X_train, Y_train)
    index = model2.coef_
    gongshi = []
    for i in range(len(index)):
        if index[i] >= 0 and i != 0:
            gongshi.append('+')
        gongshi.append('%.5f' % index[i] + labels[i])

    return ypre, Y_test, gongshi


def draw(ypredict,Y_test,gongshi):
    # rmse = math.sqrt(MSE(Y_test, ypredict))
    # print('回归 RMSE %7f' % rmse)
    r2 = r2_score(Y_test, ypredict)
    print('回归 r2 %7f' % r2)

    path = 'media/static/result/' + user + '/regression'
    if not os.path.exists(path):
        os.makedirs(path)
    time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    my_dict = {
        'fact': Y_test.values,
        'pred': ypredict
    }
    df = pd.DataFrame(my_dict)
    df.to_excel(path + '/' + time + '.xlsx')

    json_data = {}
    json_data['user'] = user
    json_data['algorithm_id'] = algorithm_id
    json_data['model_id'] = model_id
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/finishgrouptestregression', data=json_data)


if __name__ == '__main__':
    y_pre, Y_test, formula = yuchuli(file_path)
    draw(y_pre, Y_test, formula)



