import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM, Dense, Dropout
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
import matplotlib.pyplot as plt
import os
import datetime
import numpy as np
import pylab as mpl
from math import *
import sys
import requests
import json


np.set_printoptions(suppress=True)
mpl.rcParams['font.sans-serif'] = ['simHei']
mpl.rcParams['axes.unicode_minus'] = False

id = sys.argv[1]


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


def load_data_to_supervision():
    data, year = get_data()
    values = data.values
    scaler = MinMaxScaler(feature_range=(0, 1))
    values = values.astype('float32')

    scaled = scaler.fit_transform(values)

    reframed = series_to_supervision(scaled, 3, 1)

    return reframed, scaler, scaled, year


def get_data():
    dataset = pd.read_csv(os.path.dirname(__file__)+'/dataset_new.csv')
    year = dataset.values[:, 1]
    dataset = dataset.drop(dataset.columns[[0, 1, 4, 7, 10]], axis=1)

    return dataset, year


# 初始化训练集和测试集
def train_data(reframed, split):
    values = reframed.values
    train = values
    test = values[split:]

    train_X, train_Y = train[:, :-1], train[:, -1]
    test_X, test_Y = test[:, :-1], test[:, -1]

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

    history = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=500, batch_size=5, verbose=2)

    model.save(os.path.dirname(__file__)+'/weight/Garbage_weight.h5')

    # save_process_result(history)

    plt.figure()
    plt.plot(history.history['loss'], label='train')
    plt.plot(history.history['val_loss'], label='test')
    plt.legend()
    plt.savefig('loss')
    plt.show()


# def save_process_result(history):
#     if not os.path.exists('result.pkl'):
#         os.makedirs('result.pkl')
#
#     file = open('result.pkl', 'wb')
#     pickle.dump(history.history, file)
#     file.close()


def Update_time_list(data, result):
    data = data.reshape((data.shape[0], data.shape[2]))
    result = np.concatenate((data, result), axis=1)
    result = np.delete(result, 0, axis=1)

    result = result.reshape((result.shape[0], 1, result.shape[1]))

    return result


def Transfer_to_realdata(result, scaler):
   return scaler.inverse_transform(result)


def Predict(days):
    data, year = get_data()
    data = data.values
    reframed, scaler, _, _ = load_data_to_supervision()
    plt.figure()
    xaxis = [x for x in range(1, data.shape[0]+1)]
    plt.xticks(xaxis)
    plt.plot(data[:, 0], label='fact')
    split = int((3 / 4) * reframed.values.shape[0])
    _, _, testX, testY = train_data(reframed, split)
    model = LSTMmodel(testX)
    model.load_weights(os.path.dirname(__file__)+'/weight/Garbage_weight.h5')
    result = model.predict(testX)

    # testX_count = Update_time_list(testX, result)
    #
    # result_count = model.predict(testX_count)
    # result_count = int(Transfer_to_realdata(result_count, scaler)[-1][0])

    result_old = result
    index_old = data.shape[0] - 1

    xlabel = list()
    ylabel = list()

    for i in range(days):
        testX = Update_time_list(testX, result_old)
        result = model.predict(testX)
        index = index_old + 1
        xlabel.extend([index_old, index])
        ylabel.extend([Transfer_to_realdata(result_old, scaler)[-1][0], Transfer_to_realdata(result, scaler)[-1][0]])
        if i != days-1:
            plt.plot(xlabel, ylabel, color='red')
        else:
            plt.plot(xlabel, ylabel, color='red', label='predict')
        index_old = index
        result_old = result
        xlabel = list()
        ylabel = list()

    plt.legend()
    plt.title('生活垃圾生产量趋势图')
    plt.show()
    #
    # return result_count


def predict_all():
    reframed, scaler, data, year = load_data_to_supervision()
    trainX, trainY, _, _ = train_data(reframed, 1)
    model = LSTMmodel(trainX)
    model.load_weights(os.path.dirname(__file__)+'/weight/Garbage_weight.h5')
    result = model.predict(trainX)

    data[3:, -1] = result[:, 0]
    data = scaler.inverse_transform(data)

    preds = data[:, -1]
    real = pd.read_csv(os.path.dirname(__file__)+'/dataset_new.csv').values[:, -1]

    rmse = sqrt(mean_squared_error(preds, real))
    print('Test RMSE: %.3f' % rmse)

    json_data = {}
    json_data['project_id'] = id
    result_list = []
    for i in range(len(year)):
        dict = {}
        dict['year'] = year[i]
        dict['real'] = real[i]
        dict['pred'] = preds[i]
        result_list.append(dict)
    json_data['data'] = result_list
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/save_lstm_result', data=json_data)

    # data.to_csv(os.path.dirname(__file__)+
    #             '/result/LSTM_result'+datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')+'.csv')

    # plt.title('LSTM模型对城市生活垃圾产量预测')
    # plt.plot(real, label='实际值')
    # plt.plot(preds, label='预测值')
    # plt.legend()
    # plt.savefig(os.path.dirname(__file__)+
    #             '/picture/LSTM_Predict'+datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')+'.png')
    # plt.show()


def Train():
    reframed, scaler, _, _ = load_data_to_supervision()
    split = int((3 / 4)*reframed.values.shape[0])
    trainX, trainY, testX, testY = train_data(reframed, split)
    train_model(trainX, trainY, testX, testY)


if __name__ == '__main__':
    # Predict(10)
    # Train()
    dict = {}
    dict['project_id'] = id
    data = json.dumps(dict)
    predict_all()
    requests.post('http://127.0.0.1:8000/api/experiment_lstm_finish', data=data)
