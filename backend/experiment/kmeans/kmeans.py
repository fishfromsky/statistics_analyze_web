import json
from sklearn import metrics
from sklearn.cluster import KMeans
import numpy as np
import sys
import pandas as pd
from numpy import *
from scipy.interpolate import lagrange
import datetime
import requests
import os


user = sys.argv[1]
file_path = sys.argv[2]
select_list = sys.argv[3]
algorithm_id = sys.argv[4]
model_id = sys.argv[5]
test_type = sys.argv[6]
next_list = sys.argv[7]

data_min = []
norm_range = []

norm_flag = False   # 判断是否已经调用过归一化函数

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


def get_drop_col(origin, select):
    drop_col = []
    for item in origin:
        if item not in select:
            drop_col.append(item)

    return drop_col


def guiyihua():
    global norm_flag
    df = pd.read_excel(file_path)
    original_column_list = df.columns.values
    original_column_list_index = [i for i in range(len(original_column_list))]
    drop_col = get_drop_col(original_column_list_index, column_list)
    dataset = df.drop(df.columns[drop_col], axis=1)

    dataset = deal_nan(dataset)

    datasety = dataset
    labels = dataset.columns
    dataset = dataset.values
    for i in range(dataset.shape[0]):
        for j in range(dataset.shape[1]):
            if isinstance(dataset[i][j], str):
                if dataset[i][j].isspace():
                    dataset[i][j].strip()
    k = []

    for i in range(dataset.shape[1]):
        p = normalization(dataset[:, i])
        if i == 0:
            k = p
        else:
            k = np.c_[k, p]

    if not norm_flag:
        norm_flag = True

    df = pd.DataFrame(k, columns=labels)

    return df, datasety, labels


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


def normalization(data):
    global data_min, norm_range, norm_flag
    _range = np.max(data) - np.min(data)
    if not norm_flag:
        norm_range.append(_range)
        data_min.append(np.min(data))
    return (data - np.min(data)) / _range


def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k ,n)))
    for j in range(n):
        minJ = min(dataSet[:, j])
        rangeJ = float(max(dataSet[:, j] - minJ))
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
    return centroids


def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]  #行数，数据点数目
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i, 0] != minIndex: clusterChanged = True
            clusterAssment[i, :] = minIndex,minDist**2
        #print(centroids)
        for cent in range(k):
            # 矩阵.A是把矩阵转换为数组numpy
            # nonzero返回哪些元素不是False或者0，第一个array描述行，第二个array描述列
            pstInClust = dataSet[nonzero(clusterAssment[:, 0].A==cent)[0]]
            centroids[cent, :] = mean(pstInClust, axis=0)
    return centroids, clusterAssment


def bikmeans(dataset, k, distmeas=distEclud):
    m = shape(dataset)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroid0 = mean(dataset, axis=0).tolist()[0]
    centList = [centroid0]  # create a list with one centroid
    for j in range(m):  # calc initial Error
        clusterAssment[j, 1] = distmeas(mat(centroid0), dataset[j, :]) ** 2
    while (len(centList) < k):
        lowestSSE = inf
        for i in range(len(centList)):
            ptsInCurrCluster = dataset[nonzero(clusterAssment[:, 0].A == i)[0], :]  # get the data points currently in cluster i
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distmeas)
            sseSplit = sum(splitClustAss[:, 1])  # compare the SSE to the currrent minimum
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:, 0].A != i)[0], 1])
            # print ("sseSplit, and notSplit: ", sseSplit, sseNotSplit)
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(centList)  # change 1 to 3,4, or whatever
        bestClustAss[nonzero(bestClustAss[:, 0].A == 0)[0], 0] = bestCentToSplit
        # print ('the bestCentToSplit is: ', bestCentToSplit)
        # print ('the len of bestClustAss is: ', len(bestClustAss))
        centList[bestCentToSplit] = bestNewCents[0, :].tolist()[0]  # replace a centroid with two best centroids
        centList.append(bestNewCents[1, :].tolist()[0])
        clusterAssment[nonzero(clusterAssment[:, 0].A == bestCentToSplit)[0],:] = bestClustAss  # reassign new clusters, and SSE
    return mat(centList), clusterAssment


def testnum():
    df, datasety, x = guiyihua()
    df = mat(df.values)
    max = 0
    index = -1
    for i in range(2, 10):
        kmeans = KMeans(n_clusters=i, random_state=123).fit(df)
        score = metrics.calinski_harabasz_score(df, kmeans.labels_)
        if score > max:
            max = score
            index = i
        # print("聚类%d簇的calinski_harabaz分数为：%f" % (i, score))

    return index


def diaoyong(classnum):
    df, datasety, labels = guiyihua()
    df = mat(df.values)
    mycentroids, clustassing = bikmeans(df, classnum, distmeas=distEclud)
    return mycentroids, clustassing, df, labels


def clusterclubs(clustassing, numclust, datmat):   #bikmeans分类画图
    otherpoints = []
    for i in range(numclust):
        ptsincurrcluster = datmat[nonzero(clustassing[:, 0].A == i)[0], :]
        otherpoints.append(ptsincurrcluster.getA())
    return otherpoints


if __name__ == '__main__':
    class_num = testnum()
    mycentroids, clustassing, df, labels = diaoyong(class_num)
    otherpoints = clusterclubs(clustassing, class_num, df)
    col_num = otherpoints[0].shape[1]
    data_tmp = []   # 暂存逆归一化后的数组
    label_tmp = []  # 暂存标记数组
    for i in range(col_num):
        data_tmp.append([])
    for i in range(len(otherpoints)):
        for j in range(otherpoints[i].shape[1]):
            arr_origin = otherpoints[i][:, j]
            arr_final = arr_origin*norm_range[j]+data_min[j]
            otherpoints[i][:, j] = arr_final
            data_tmp[j].extend(arr_final)
            if j == 0:
                for k in range(len(arr_final)):
                    label_tmp.append(i)

    data_tmp = np.array(data_tmp).T
    label_tmp = np.array(label_tmp).T
    data_tmp = np.insert(data_tmp, data_tmp.shape[1], values=np.array(label_tmp).T, axis=1)
    label_index = labels.values
    my_dict = {
        label_index[0]: data_tmp[:, 0],
        label_index[1]: data_tmp[:, 1],
        'label': data_tmp[:, 2]
    }
    dataframe = pd.DataFrame(my_dict)
    path = 'media/static/result/' + user + '/kmeans'
    if not os.path.exists(path):
        os.makedirs(path)
    time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    dataframe.to_excel(path+'/'+time+'.xlsx')
    json_data = {}
    json_data['user'] = user
    json_data['algorithm_id'] = algorithm_id
    json_data['model_id'] = model_id
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/finishgrouptestrelation', data=json_data)





