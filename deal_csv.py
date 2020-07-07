import pandas as pd
import requests


def read_csv():
    dataset = pd.read_csv('C:\\Users\\cyy\\Desktop\\collect.csv')
    return dataset.values, dataset.columns.values


def tranfer(geo):
    params = { 'address': geo, 'city': '上海市', 'key': 'c83eaee63075867503a71b3282e11a1a' }
    base_url = 'https://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base_url, params)
    answer = response.json()
    location = answer['geocodes'][0]['location'].split(',')
    return location[0], location[1]


def transfer_csv():
    data, cols = read_csv()
    for i in range(0, len(data)):
        print('转换中，第%d个地址' % (i+1))
        longitude, latitude = tranfer(data[i][2])
        data[i][3] = longitude
        data[i][4] = latitude

    dataframe = pd.DataFrame({
        cols[0]: data[:, 0],
        cols[1]: data[:, 1],
        cols[2]: data[:, 2],
        cols[3]: data[:, 3],
        cols[4]: data[:, 4],
        cols[5]: data[:, 5]
    })
    print(dataframe)
    dataframe.to_csv('C:\\Users\\cyy\\Desktop\\collect_new.csv', encoding='utf_8_sig')


if __name__ == '__main__':
    transfer_csv()