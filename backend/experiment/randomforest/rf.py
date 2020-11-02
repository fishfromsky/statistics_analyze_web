import pandas as pd
from scipy.interpolate import lagrange
from sklearn.ensemble import RandomForestClassifier


def read_csv(path):   # 读入数据并舍弃缺失较多的特征
    df = pd.read_excel(path)
    drop_col = []
    data_columns = df.columns.values.tolist()
    for index in df.columns:
        none_na_count = df[index].count()
        if none_na_count / df.shape[0] < 0.5:
            df = df.drop(columns=[index])
            data_columns.remove(index)
            drop_col.append(index)

    return df, data_columns, drop_col


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


def rf(data, special):
    y = data[special]
    x = data.drop([special, '城市'], axis=1)
    clf = RandomForestClassifier()
    clf.fit(x, y.astype('int'))
    importance = clf.feature_importances_
    print(importance)


if __name__ == '__main__':
    data, use_cols, drop_cols = read_csv('dataset.xlsx')
    data = deal_nan(data)
    special = '城市生活垃圾清运量\n（万吨）'
    rf(data, special)
