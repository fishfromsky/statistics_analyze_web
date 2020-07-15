import pandas as pd
import requests


def read_csv():
    dataset = pd.read_csv('C:\\Users\\Administrator\\Desktop\\collect1.csv')
    return dataset.values, dataset.columns.values


def tranfer(geo):
    params = { 'address': geo, 'city': '上海市', 'key': 'c83eaee63075867503a71b3282e11a1a' }
    base_url = 'https://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base_url, params)
    answer = response.json()
    if len(answer['geocodes']) != 0:
        location = answer['geocodes'][0]['location'].split(',')
        return location[0], location[1]
    else:
        return None, None


def transfer_csv():
    data, cols = read_csv()
    for i in range(0, len(data)):
        if data[i][0] != '宝山区':
            break
        print('转换中，第%d个地址' % (i+1))
        longitude, latitude = tranfer(data[i][1])
        if longitude is not None and latitude is not None:
            data[i][2] = longitude
            data[i][3] = latitude

    dataframe = pd.DataFrame({
        cols[0]: data[:, 0],
        cols[1]: data[:, 1],
        cols[2]: data[:, 2],
        cols[3]: data[:, 3]
    })
    print(dataframe)
    dataframe.to_csv('C:\\Users\\Administrator\\Desktop\\collect_new.csv', encoding='utf_8_sig')


if __name__ == '__main__':
    transfer_csv()