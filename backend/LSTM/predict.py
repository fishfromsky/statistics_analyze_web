import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM, Dense
from keras.models import Sequential
import matplotlib.pyplot as plt
import numpy as np
import pylab as mpl
import sys
import datetime
import os

file_path = sys.argv[1]
predict_day = sys.argv[2]
user = sys.argv[3]
project_id = sys.argv[4]

Predict_Result = []

predict_day = int(predict_day)

np.set_printoptions(suppress=True)
mpl.rcParams['font.sans-serif'] = ['simHei']
mpl.rcParams['axes.unicode_minus'] = False


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
    values = get_data()
    scaler = MinMaxScaler(feature_range=(0, 1))
    values = values.astype('float32')

    scaled = scaler.fit_transform(values)

    reframed = series_to_supervision(scaled, 3, 1)

    return reframed, scaler, scaled


def get_data():
    data = pd.read_excel(file_path)
    dataset = data['fact'].values
    dataset = dataset.reshape((dataset.shape[0], 1))

    return dataset


# 初始化训练集和测试集
def train_data(reframed, split):
    values = reframed.values
    train = values[:split]
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

    return model


def Update_time_list(data, result):
    data = data.reshape((data.shape[0], data.shape[2]))
    result = np.concatenate((data, result), axis=1)
    result = np.delete(result, 0, axis=1)

    result = result.reshape((result.shape[0], 1, result.shape[1]))

    return result


def Transfer_to_realdata(result, scaler):
   return scaler.inverse_transform(result)


def Predict(days):
    global Predict_Result

    data = get_data()
    reframed, scaler, _ = load_data_to_supervision()
    split = int((3 / 4) * reframed.values.shape[0])
    trainX, trainY, testX, testY = train_data(reframed, split)
    model = train_model(trainX, trainY, testX, testY)
    result = model.predict(testX)

    testX_count = Update_time_list(testX, result)

    result_count = model.predict(testX_count)
    result_count = int(Transfer_to_realdata(result_count, scaler)[-1][0])

    Predict_Result.append(result_count)

    result_old = result
    index_old = data.shape[0] - 1

    xlabel = list()
    ylabel = list()

    for i in range(days):
        testX = Update_time_list(testX, result_old)
        result = model.predict(testX)
        Predict_Result.append(Transfer_to_realdata(result, scaler)[-1][0])
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

    return result_count


def Train():
    reframed, scaler, _ = load_data_to_supervision()
    split = int((3 / 4)*reframed.values.shape[0])
    trainX, trainY, testX, testY = train_data(reframed, split)
    train_model(trainX, trainY, testX, testY)


if __name__ == '__main__':
    Predict(predict_day)
    path = 'media/static/modelresult/' + user + '/lstm' + '/' + project_id + '/predict'
    if not os.path.exists(path):
        os.makedirs(path)
    time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    my_dict = {
        'predict': Predict_Result
    }
    df = pd.DataFrame(my_dict)
    df.to_excel(path + '/' + time + '.xlsx')
