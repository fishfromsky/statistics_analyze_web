import json
import numpy as np
import pandas as pd
from scipy.interpolate import lagrange
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
import os
import sys
import datetime
import requests


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


def read_csv(path, drop_index):
    drop_index.remove(special)
    dataframe = pd.read_excel(path)
    head_list = dataframe.columns.values
    special_head = head_list[special]
    df = dataframe.drop(dataframe.columns[drop_index], axis=1)
    new_head_list = df.columns.values
    new_special = list(new_head_list).index(special_head)
    return df, new_special


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
    global special
    data, head_special = read_csv(path, drop_col)
    special = head_special
    data = deal_nan(data)
    values = data.values
    scaler = MinMaxScaler(feature_range=(0, 1))
    values = values.astype('float32')

    scaled = scaler.fit_transform(values)

    reframed = series_to_supervision(scaled, 3, 1)

    return reframed, scaler, scaled


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

    model.save(os.path.dirname(__file__)+'/weight/Garbage_weight.h5')


if __name__ == '__main__':
    # 训练模型
    reframed, scaler, scaled = load_data_to_supervision(file_path, drop_index)
    split = int((3 / 4)*reframed.values.shape[0])
    trainX, trainY, testX, testY = train_data(reframed, split, special)
    train_model(trainX, trainY, testX, testY)

    # 预测模型
    model = LSTMmodel(trainX)
    model.load_weights(os.path.dirname(__file__)+'/weight/Garbage_weight.h5')
    predict_data = np.concatenate((trainX, testX), axis=0)
    result = model.predict(predict_data)

    origin_data = scaler.inverse_transform(scaled[3:])
    origin_result = origin_data[:, special]

    scaled[3:, special] = result[:, 0]
    final_result = scaled[3:]

    final_result = scaler.inverse_transform(final_result)[:, special]

    path = 'media/static/result/' + user + '/lstm'
    if not os.path.exists(path):
        os.makedirs(path)
    time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    my_dict = {
        'fact': origin_result,
        'pred': final_result
    }
    df = pd.DataFrame(my_dict)
    df.to_excel(path+'/'+time+'.xlsx')

    json_data = {}
    json_data['user'] = user
    json_data['algorithm_id'] = algorithm_id
    json_data['model_id'] = model_id
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/grouptestfinishlstm', data=json_data)



