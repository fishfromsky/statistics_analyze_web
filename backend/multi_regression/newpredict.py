# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import mean_squared_error as MSE, r2_score, mean_absolute_error as MAE
import math
import pylab as mpl
from sklearn.linear_model import LassoCV,LinearRegression as LR,Lasso,Ridge,RidgeCV
from sklearn.preprocessing import MinMaxScaler,PolynomialFeatures
import joblib
import json
import sys
import os
import requests
from pandas import json_normalize


np.set_printoptions(suppress=True)
mpl.rcParams['font.sans-serif'] = ['simHei']
mpl.rcParams['axes.unicode_minus'] = False

id = sys.argv[1]
index_list = sys.argv[2]

if index_list == '-1':
    column_list = []
else:
    column_list = index_list.split(',')
    column_list = list(map(int, column_list))


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


def filescvmatrix():
    params = {'project_id': id}

    res = requests.get('http://127.0.0.1:8000/api/get_parameter_regression', params=params)
    json_data = json.loads(res.text).get('data')

    df = json_normalize(json_data)
    df = df.drop(df.columns[[df.shape[1]-1]], axis=1)
    dataset = df.drop(df.columns[[0, 4, 8, 9, 10, 12, 13, 16, 17]], axis=1)
    dataset = dataset.fillna(0.1)

    # 1上海2北京3深圳4广州5-重庆6天津7武汉8南京9杭州10成都11-佛山12青岛13苏州14东莞15西安16长沙17济南18宁波19常州20无锡
    # h = 1  # 第几个城市
    # dataset = dataset[20 * h - 20:20 * h]
    # dataset.dropna(inplace=True)
    Mat=dataset.values
    result = Mat[:, -1]
    Matx = dataset.drop(dataset.columns[[-1]], axis=1)
    labels = dataset.columns

    X_train, X_test, Y_train, Y_test = train_test_split(Matx, result, train_size=.8)
    return X_train, X_test, Y_train, Y_test, Mat, labels

def guiyihui(X_train, X_test, Y_train, Y_test):
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)
    Y_train = scaler.fit_transform(Y_train.reshape(-1, 1))
    Y_test = scaler.fit_transform(Y_test.reshape(-1, 1))
    return X_train,X_test,Y_train,Y_test


def train1(x_train,y_train,x_test,y_test,labels):#多元线性回归
    #simple2 = LassoCV()  #lasso回归 正则化参数
    # simple2 = Lasso(alpha=0.01)
    simple2 = LR().fit(x_train, y_train)
    #simple2.fit(x_train, y_train)
    joblib.dump(simple2, os.path.dirname(__file__)+'/LinearRegression.pkl')
    y_predict = simple2.predict(x_test)
    return y_predict


def draw(ypredict, Y_test, gongshi, choose_col):
    # rmse = math.sqrt(MSE(Y_test, ypredict))
    # print('回归 RMSE %7f' % rmse)

    select_col = ''
    for i in range(len(choose_col)):
        if i != len(choose_col)-1:
            select_col = select_col+choose_col[i]+', '
        else:
            select_col = select_col+choose_col[i]

    r_square = r2_score(y_test, ypredict)
    mse = MSE(y_test, ypredict)
    rmse = mse ** 0.5
    mae = MAE(y_test, ypredict)

    formula = 'y='
    for i in range(len(gongshi)):
        formula = formula+gongshi[i]

    json_data = {}
    json_data['project_id'] = id
    result_list = []
    for i in range(len(ypredict)):
        dict = {}
        dict['real'] = Y_test.values[i]
        dict['pred'] = ypredict[i]
        result_list.append(dict)
    json_data['data'] = result_list
    json_data['r_square'] = r_square
    json_data['mse'] = mse
    json_data['rmse'] = rmse
    json_data['mae'] = mae
    json_data['formula'] = formula
    json_data['choose_col'] = select_col
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/save_regression_result', data=json_data)

    # plt.figure()
    # plt.plot(range(len(Y_test)), Y_test, 'r*', label="test")
    # plt.plot(range(len(ypredict)), ypredict, 'b', label="predict")
    # plt.legend(loc="upper right")  # 显示图中的标签
    # x1 = gongshi[:int(len(gongshi)/2)]
    # x2 = gongshi[int(len(gongshi)/2):]
    # x1 = ''.join(x1)
    # x2 = ''.join(x2)
    # plt.title('多元线性回归对城市生活垃圾产量预测==回归 r2 %7f\n\n'% r2+'y = '+x1+'\n'+x2,fontsize='small')
    # #plt.savefig('los_Predict.png')
    # plt.show()

def test(x_test,Y_test):
    model = joblib.load(os.path.dirname(__file__)+'/LinearRegression.pkl')
    ypredict = model.predict(x_test)
    rmse = math.sqrt(MSE(Y_test, ypredict))
    print('线性回归 RMSE %3f' % rmse)
    error_rate = np.sqrt(MSE(Y_test, ypredict)) / Y_test.mean()
    print('回归 correct_rate %7f' % (1-error_rate))


    plt.figure()
    plt.plot(range(len(ypredict)), Y_test, 'r*', label="test")
    plt.plot(range(len(ypredict)), ypredict, 'b', label="predict")
    plt.legend(loc="upper right")  # 显示图中的标签
    plt.title('多元线性回归对城市生活垃圾产量预测')
    plt.savefig('los_Predict.png')
    plt.show()


def yuchuli(iterations):
    alphaslist = [0.0001,0.001,0.01,0.1, 1.0, 10.0,100,1000,10000]   #alphas列表
    params = {'project_id': id}

    res = requests.get('http://127.0.0.1:8000/api/get_parameter_regression', params=params)
    json_data = json.loads(res.text).get('data')

    df = json_normalize(json_data)
    df = df.drop(df.columns[[0, df.shape[1] - 1]], axis=1)
    dataset = df.drop(df.columns[column_list], axis=1)

    choose_col = dataset.columns.values
    # h = 13  # 第几个城市
    # dataset = dataset[20 * h - 20:20 * h]
    dataset = dataset.fillna(0.1)
    y = dataset.iloc[:, -1]
    x = dataset.drop(dataset.columns[[-1]], axis=1)
    po = PolynomialFeatures(degree=2,interaction_only=False,include_bias=False)
    x_poly = po.fit_transform(x)
    x_change = pd.DataFrame(x_poly, columns=po.get_feature_names())
    labels = x_change.columns
    X_train, X_test, Y_train, Y_test = train_test_split(x_change,y,test_size=0.2,random_state=1)
    model2 = LassoCV(alphas=alphaslist)  # 导入模型传入参数alpha=0.1
    model2.fit(X_train,Y_train)  # 训练数据
    # model2 = Lasso(max_iter = iterations, alphas=1).fit(X_train,Y_train)
    index = model2.coef_
    newindex = []
    if len(labels) == len(index):
        for i in range(len(index)):
            if(index[i] >= 0.00001 and i != 0):#选择系数值绝对值大于等于0.00001的系数
                pass
            else:
                pass
            if(abs(index[i]) >= 0.00001):
                newindex.append(i)
    ypre = model2.predict(X_test)
    x_changenew = x_change.iloc[:, newindex]#形成新的dataset
    #选择新的特征系数重新进行线性回归————————————————————————————————————————————————————————————————————————————————————-———
    X_train, X_test, Y_train, Y_test = train_test_split(x_changenew, y, test_size=0.2, random_state=1)
    model2 = RidgeCV(alphas=alphaslist)  # 导入模型传入参数alpha=0.1
    model2.fit(X_train, Y_train)  # 训练数据
    # model2 = Lasso(max_iter=iterations).fit(X_train, Y_train)
    index = model2.coef_
    gongshi = []
    for i in range(len(index)):
        if(index[i] >= 0 and i != 0):
            gongshi.append('+')
        gongshi.append('%.5f'%index[i]+labels[i])

    return ypre, Y_test, gongshi, choose_col

#多元线性回归
train = 3
X_train, X_test, Y_train, Y_test, Mat, labels = filescvmatrix()
if(train == 1):
    # X_train, X_test, Y_train, Y_test = guiyihui(X_train, X_test, Y_train, Y_test)
    ypredict = train1(X_train, Y_train, X_test, Y_test, labels)
    draw(ypredict, Y_test)
elif(train == 0):
    test(X_test, Y_test)
#多元非线性回归
elif(train == 3):
    #判定系数（r2）：说明列入模型的所有解释变量对因变量的联合的影响程度，不说明模型中单个解释变量的影响程度。
    ypre, y_test, gongshi, choose_col = yuchuli(1000)
    draw(ypre, y_test, gongshi, choose_col)
    dict = {}
    dict['project_id'] = id
    data = json.dumps(dict)
    requests.post('http://127.0.0.1:8000/api/finish_regression_experiment', data=data)
elif(train==4):
    i = 1000
    error_rate = []
    r2 = []
    while(i<100000):
        ypre, y_test,gongshi = yuchuli(i)
        error_rate.append(np.sqrt(MSE(y_test, ypre)) / Y_test.mean())
        r2.append(r2_score(y_test, ypre))
        i = i + 2000
    plt.figure()
    plt.plot(range(len(r2)), r2, 'r', label="r2")
    plt.plot(range(len(r2)), error_rate, 'b', label="error_rate")
    plt.legend(loc="upper right")  # 显示图中的标签
    plt.title('r2和error_rate')
    plt.savefig('test.png')
    plt.show()