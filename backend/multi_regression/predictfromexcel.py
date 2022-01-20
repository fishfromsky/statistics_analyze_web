import sys
import pandas as pd
import numpy as np
import os
import datetime

user = sys.argv[1]
project_id = sys.argv[2]
data = sys.argv[3]
coef = sys.argv[4]


def getCoef():
    data = pd.read_excel(coef).values
    coef_params = data[6][~pd.isnull(data[6])][1:].tolist()
    intercept = data[7][~pd.isnull(data[7])][1:].tolist()[0]
    return coef_params, intercept


def getData():
    data_params = pd.read_excel(data).values
    return data_params


def getPredictResult(coef, data, intercept):
    result = []
    m, n = data.shape
    for i in range(m):
        sum = 0
        for j in range(n):
            sum += data[i][j]*coef[j]
        sum += intercept
        result.append(sum)

    result = np.array(result).reshape((len(result), 1))

    result = np.concatenate((data, result), axis=1)

    excel_data = {}
    _, col = result.shape

    for i in range(col):
        if i != col-1:
            excel_data['params'+str(i)] = result[:, i]
        else:
            excel_data['result'] = result[:, i]

    df = pd.DataFrame(excel_data)
    path = 'media/static/predictresult/' + user + '/regression' + '/' + project_id
    if not os.path.exists(path):
        os.makedirs(path)
    time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    df.to_excel(path + '/' + time + '.xlsx')


if __name__ == '__main__':
    coef_params, intercept = getCoef()
    data_params = getData()
    getPredictResult(coef_params, data_params, intercept)
