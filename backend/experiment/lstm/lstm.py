import sys
import json
import numpy as np
import pandas as pd
from scipy.interpolate import lagrange
from sklearn.preprocessing import MinMaxScaler


file_path = sys.argv[1]
drop_col = sys.argv[2]
special = sys.argv[3]


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


def read_csv(path, drop_col):
    dataframe = pd.read_excel(path)
    df = dataframe.drop(dataframe.columns[drop_col], axis=1)
    return df


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


def series_to_supervision(data, n_in=1, n_out=1, dropnan=True):
    # 确定features个数
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()

    # 将时序序列转换为监督学习数据

    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]

    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]

    agg = pd.concat(cols, axis=1)
    agg.columns = names

    if dropnan:
        agg.dropna(inplace=True)

    return agg


def load_data_to_supervision(path, drop_col):
    data = read_csv(path, drop_col)
    data = deal_nan(data)
    values = data.values
    scaler = MinMaxScaler(feature_range=(0, 1))
    values = values.astype('float32')

    scaled = scaler.fit_transform(values)

    reframed = series_to_supervision(scaled, 3, 1)

    return reframed, scaler, scaled


if __name__ == '__main__':
    reframed, scaler, scaled = load_data_to_supervision(file_path, drop_col)