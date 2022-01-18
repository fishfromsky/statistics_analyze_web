from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM, Dense
from keras.models import Sequential
from scipy.interpolate import lagrange
import os
import datetime
import pandas as pd
import numpy as np
import pylab as mpl
import sys
import requests
import json
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


np.set_printoptions(suppress=True)
mpl.rcParams['font.sans-serif'] = ['simHei']
mpl.rcParams['axes.unicode_minus'] = False

project_id = sys.argv[1]
select_list = sys.argv[2]
special = sys.argv[3]
user = sys.argv[4]
file_path = sys.argv[5]

special = int(special)

if select_list == '-1':
    drop_list = []
else:
    drop_list = select_list.split(',')
    drop_list = list(map(int, drop_list))


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


def read_csv(path, drop_index):
    drop_index.remove(special)
    dataframe = pd.read_excel(path)
    head_list = dataframe.columns.values
    special_head = head_list[special]
    df = dataframe.drop(dataframe.columns[drop_index], axis=1)
    new_head_list = df.columns.values
    new_special = list(new_head_list).index(special_head)
    return df, new_special, special_head, new_head_list


def ploy(s, n, k=3):   # 拉格朗日插值函数
    y = s.reindex(list(range(n-k, n))+list(range(n+1, n+1+k)))  # 取数
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
    global special
    data, head_special, head_special_name, new_head_list = read_csv(path, drop_col)
    special = head_special
    data = deal_nan(data)
    values = data.values
    scaler = MinMaxScaler(feature_range=(0, 1))
    values = values.astype('float32')

    scaled = scaler.fit_transform(values)

    reframed = series_to_supervision(scaled, 3, 1)

    return reframed, scaler, scaled, head_special_name, new_head_list, data


def train_data(reframed, split, special):
    values = reframed.values
    train = values[:split]
    test = values[split:]

    train_X, train_Y = np.concatenate((train[:, :special], train[:, special+1:]), axis=1), train[:, special]
    test_X, test_Y = np.concatenate((test[:, :special], test[:, special+1:]), axis=1), test[:, special]

    train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
    test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))

    return train_X, train_Y, test_X, test_Y


def LSTMmodel(trainX):
    model = Sequential()
    model.add(LSTM(50, input_shape=(trainX.shape[1], trainX.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam', metrics=['accuracy'])

    return model


def train_model(trainX, trainY, testX, testY):

    model = LSTMmodel(trainX)

    history = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=200, batch_size=5, verbose=2)

    path = 'media/static/modelresult/' + user + '/lstm' + '/' + project_id + '/weight'
    if not os.path.exists(path):
        os.makedirs(path)
    time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

    model.save(path+'/'+time+'.h5')

    return model


if __name__ == '__main__':
    # 训练模型
    reframed, scaler, scaled, new_special_head, new_head_list, origin_data = load_data_to_supervision(file_path, drop_list)
    split = int((3 / 4) * reframed.values.shape[0])
    trainX, trainY, testX, testY = train_data(reframed, split, special)
    model = train_model(trainX, trainY, testX, testY)

    path = 'media/static/modelresult/' + user + '/lstm' + '/' + project_id + '/weight'
    time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

    # 预测模型
    model_result_train = model.predict(trainX)
    model_result_test = model.predict(testX)

    result = np.append(model_result_train[:, 0], model_result_test[:, 0])
    result = result.reshape((result.shape[0], 1))
    scaled_pred = scaled
    scaled_pred[3:, special] = result[:, 0]

    pred = scaler.inverse_transform(scaled_pred)[:, special]

    fact = origin_data.values[:, special]

    new_head_list = list(new_head_list)
    new_head_list.remove(new_special_head)
    select_col = ''
    for i in range(len(new_head_list)):
        if i != len(new_head_list) - 1:
            select_col = select_col + new_head_list[i] + ', '
        else:
            select_col = select_col + new_head_list[i]

    path = 'media/static/modelresult/' + user + '/lstm' + '/' + project_id
    if not os.path.exists(path):
        os.makedirs(path)
    time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    my_dict = {
        'fact': fact,
        'pred': pred,
        'head': new_special_head,
        'head_list': select_col,
        'path': file_path
    }
    df = pd.DataFrame(my_dict)
    df.to_excel(path + '/' + time + '.xlsx')

    dict = {}
    dict['project_id'] = project_id
    data = json.dumps(dict)
    requests.post('http://127.0.0.1:8000/api/experiment_lstm_finish', data=data)

