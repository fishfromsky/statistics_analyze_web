import pandas as pd
from scipy.interpolate import lagrange
from sklearn.ensemble import RandomForestClassifier
import sys
import os
import datetime
import requests
import json
import numpy as np

user = sys.argv[1]
file_path = sys.argv[2]
relative_max = sys.argv[3]
select_list = sys.argv[4]
choose_col = sys.argv[5]
algorithm_id = sys.argv[6]
model_id = sys.argv[7]

column_list = select_list.split(',')
column_list = list(map(int, column_list))


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


def filter_list(main_list, tmp_list):
    result = []
    for item in main_list:
        if item not in tmp_list:
            result.append(item)

    return result


def read_csv(path, select_list, choose_col):   # 读入数据并舍弃缺失较多的特征
    df = pd.read_excel(path)
    reference_col = df.columns.values[int(choose_col)]
    _, n = df.shape
    main_list = list(range(n))
    select_list.append(int(choose_col))
    drop_list = filter_list(main_list, select_list)
    df = df.drop(df.columns[drop_list], axis=1)
    drop_col = []
    data_columns = df.columns.values.tolist()
    for index in df.columns:
        none_na_count = df[index].count()
        if none_na_count / df.shape[0] < 0.5:
            df = df.drop(columns=[index])
            data_columns.remove(index)
            drop_col.append(index)

    return df, data_columns, drop_col, reference_col


def ploy(s, n, k=3):   # 拉格朗日插值函数
    y = s.reindex(list(range(n-k, n))+list(range(n+1, n+1+k))) # 取数
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


def deal_nan(data):
    for i in data.columns:
        for j in range(len(data)):
            if (data[i].isnull())[j]:
                data[i][j] = ploy(data[i], j)

    return data


def rf(data, special):
    y = data[special]
    x = data.drop([special], axis=1)
    clf = RandomForestClassifier()
    clf.fit(x, y.astype('int'))
    importance = clf.feature_importances_
    return importance


if __name__ == '__main__':
    data, use_cols, drop_cols, reference_col = read_csv(file_path, column_list, choose_col)
    data = deal_nan(data)
    special = reference_col
    importance = rf(data, special)
    use_cols.remove(special)
    path = 'media/static/result/'+user+'/relation'
    if not os.path.exists(path):
        os.makedirs(path)
    time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    my_dict = {
        'label': use_cols,
        'result': importance
    }
    df = pd.DataFrame(my_dict)
    df.to_csv(path+'/'+time+'.csv')
    json_data = {}
    json_data['user'] = user
    json_data['algorithm_id'] = algorithm_id
    json_data['model_id'] = model_id
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/finishgrouptestrelation', data=json_data)
