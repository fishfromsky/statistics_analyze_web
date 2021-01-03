from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import requests
import sys
import pandas as pd
import json
import numpy as np
import os
import datetime
import json

project_id = sys.argv[1]
select_list = sys.argv[2]
special = sys.argv[3]
user = sys.argv[4]
file_path = sys.argv[5]

special = int(special)

if select_list == '-1':
    column_list = []
else:
    column_list = select_list.split(',')
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
    global special
    column_list.remove(special)
    df = pd.read_excel(file_path)
    head_list = df.columns.values
    special_head = head_list[special]

    dataset = df.drop(df.columns[column_list], axis=1)
    new_head_list = dataset.columns.values
    special = list(new_head_list).index(special_head)

    dataset = dataset.fillna(0.1)
    dataset_y = dataset.iloc[:, special]
    dataset_x = dataset.drop(dataset.columns[[special]], axis=1)

    return dataset_x, dataset_y, special_head


def test():
    X, y, new_special_head = read_csv()
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

    path = 'media/static/modelresult/' + user + '/linearregression' + '/' + project_id
    if not os.path.exists(path):
        os.makedirs(path)
    time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    my_dict = {
        'fact': real,
        'pred': predict,
        'head': [new_special_head],
        'head_list': [choose_col],
        'formula': [formula],
        'coef': coef,
        'intercept': [intercept]
    }
    df = pd.DataFrame.from_dict(my_dict, orient='index')
    df.to_excel(path + '/' + time + '.xlsx')

    dict = {}
    dict['project_id'] = project_id
    data = json.dumps(dict)
    requests.post('http://127.0.0.1:8000/api/finishlinearregression', data=data)


if __name__ == '__main__':
    test()