from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import requests
import sys
from pandas import json_normalize
import json
import numpy as np
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


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


def read_csv():
    params = {'project_id': id}
    res = requests.get('http://127.0.0.1:8000/api/getlinearregressionparameter', params=params)
    json_data = json.loads(res.text).get('data')

    df = json_normalize(json_data)
    df = df.drop(df.columns[[0, df.shape[1]-1]], axis=1)

    dataset = df.drop(df.columns[column_list], axis=1)
    dataset = dataset.fillna(0.1)
    dataset_y = dataset.iloc[:, -1]
    dataset_x = dataset.drop(dataset.columns[[-1]], axis=1)

    return dataset_x, dataset_y


def test():
    X, y = read_csv()
    cols_list = list(X.columns.values)
    choose_col = ''
    for i in range(len(cols_list)):
        if i != len(cols_list)-1:
            choose_col = choose_col+cols_list[i]+', '
        else:
            choose_col = choose_col+cols_list[i]

    lr = LinearRegression()
    x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=666)
    lr.fit(x_train, y_train)
    real = y.values
    predict = lr.predict(X)

    coef = list(lr.coef_)
    intercept = lr.intercept_
    formula = 'y='
    for i in range(len(coef)):
        if str(coef[i])[0] != '-':
            formula = formula+'+'
        formula = formula + str(round(coef[i], 5)) + 'x' + str(i)

    formula = formula+'+'+str(round(intercept, 5))

    r_square = r2_score(real, predict)
    mse = mean_squared_error(real, predict)
    rmse = mse**0.5
    mae = mean_absolute_error(real, predict)

    json_data = {}
    json_data['project_id'] = id
    result_list = []
    for i in range(len(predict)):
        dict = {}
        dict['real'] = real[i]
        dict['pred'] = predict[i]
        result_list.append(dict)
    json_data['data'] = result_list
    json_data['formula'] = formula
    json_data['mse'] = mse
    json_data['rmse'] = rmse
    json_data['mae'] = mae
    json_data['r_square'] = r_square
    json_data['choose_col'] = choose_col
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/savelinearregressionresult', data=json_data)

    dict = {}
    dict['project_id'] = id
    data = json.dumps(dict)
    requests.post('http://127.0.0.1:8000/api/finishlinearregression', data=data)


if __name__ == '__main__':
    test()