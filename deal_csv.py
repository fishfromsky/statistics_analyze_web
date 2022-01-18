import pandas as pd
import requests


def read_csv():
    dataset = pd.read_excel('factory_new.xlsx')
    return dataset.values, dataset.columns.values


def tranfer(geo):
    params = {'address': geo, 'city': '上海市', 'key': '2e3b463dd060e05a400b638567469068'}
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
        print('转换中，第%d个地址' % (i+1))
        longitude, latitude = tranfer(data[i][2])
        if longitude is not None and latitude is not None:
            data[i][6] = longitude
            data[i][7] = latitude

    dataframe = pd.DataFrame({
        cols[0]: data[:, 0],
        cols[1]: data[:, 1],
        cols[2]: data[:, 2],
        cols[3]: data[:, 3],
        cols[4]: data[:, 4],
        cols[5]: data[:, 5],
        cols[6]: data[:, 6],
        cols[7]: data[:, 7]
    })
    dataframe.to_csv('collect_new.csv', encoding='utf_8_sig')


if __name__ == '__main__':
    transfer_csv()