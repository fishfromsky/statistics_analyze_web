# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import mean_squared_error as MSE, r2_score, mean_absolute_error as MAE
import math
import pylab as mpl
from sklearn.linear_model import LassoCV,LinearRegression as LR, Lasso, Ridge, RidgeCV
from sklearn.preprocessing import MinMaxScaler,PolynomialFeatures
import joblib
import json
import sys
import os
import requests
from pandas import json_normalize
import datetime


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


def draw(ypredict, Y_test, gongshi, choose_col, special_head):

    select_col = ''
    for i in range(len(choose_col)):
        if i != len(choose_col)-1:
            select_col = select_col+choose_col[i]+', '
        else:
            select_col = select_col+choose_col[i]

    formula = 'y='
    for i in range(len(gongshi)):
        formula = formula+gongshi[i]

    path = 'media/static/modelresult/' + user + '/regression' + '/' + project_id
    if not os.path.exists(path):
        os.makedirs(path)
    time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

    pred = ypredict
    fact = Y_test.values

    my_dict = {
        'fact': fact,
        'pred': pred,
        'head': special_head,
        'head_list': select_col,
        'formula': formula,
        'path': file_path
    }
    df = pd.DataFrame(my_dict)
    df.to_excel(path + '/' + time + '.xlsx')


def yuchuli(iterations):
    global special

    drop_list.remove(special)
    alphaslist = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100, 1000, 10000]   # alphas列表

    df = pd.read_excel(file_path)
    head_list = df.columns.values
    special_head = head_list[special]

    dataset = df.drop(df.columns[drop_list], axis=1)
    new_head_list = df.columns.values
    special = list(new_head_list).index(special_head)

    choose_col = dataset.columns.values

    dataset = dataset.fillna(0.1)
    y = dataset.iloc[:, special]
    x = dataset.drop(dataset.columns[[special]], axis=1)
    po = PolynomialFeatures(degree=2, interaction_only=False, include_bias=False)
    x_poly = po.fit_transform(x)
    x_change = pd.DataFrame(x_poly, columns=po.get_feature_names())
    labels = x_change.columns
    X_train, X_test, Y_train, Y_test = train_test_split(x_change,y,test_size=0.2, random_state=1)
    model2 = LassoCV(alphas=alphaslist)  # 导入模型传入参数alpha=0.1
    model2.fit(X_train, Y_train)  # 训练数据
    # model2 = Lasso(max_iter = iterations, alphas=1).fit(X_train,Y_train)
    index = model2.coef_
    newindex = []
    if len(labels) == len(index):
        for i in range(len(index)):
            if index[i] >= 0.00001 and i != 0: # 选择系数值绝对值大于等于0.00001的系数
                pass
            else:
                pass
            if abs(index[i]) >= 0.00001:
                newindex.append(i)
    ypre = model2.predict(X_test)
    x_changenew = x_change.iloc[:, newindex] # 形成新的dataset
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
        gongshi.append('%.5f' % index[i]+labels[i])

    return ypre, Y_test, gongshi, choose_col, special_head


if __name__ == '__main__':
    # 判定系数（r2）：说明列入模型的所有解释变量对因变量的联合的影响程度，不说明模型中单个解释变量的影响程度。
    ypre, y_test, gongshi, choose_col, special_head = yuchuli(2000)
    draw(ypre, y_test, gongshi, choose_col, special_head)
    dict = {}
    dict['project_id'] = project_id
    data = json.dumps(dict)
    requests.post('http://127.0.0.1:8000/api/finish_regression_experiment', data=data)
