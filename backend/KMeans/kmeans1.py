# -*- coding: utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab as mpl
import sys
import requests
from pandas import json_normalize
import json

np.set_printoptions(suppress=True)
mpl.rcParams['font.sans-serif'] = ['simHei']
mpl.rcParams['axes.unicode_minus'] = False

id = sys.argv[1]
index_list = sys.argv[2]

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


def loadDataSet(filename):#MLiA_SourceCode\machinelearninginaction\Ch10\testSet.txt
    dataMat = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        # map() 会根据提供的函数对指定序列做映射。
        # 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat


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
    m = shape(dataSet)[0]#行数，数据点数目
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
            ptsInCurrCluster = dataset[nonzero(clusterAssment[:, 0].A == i)[0],:]  # get the data points currently in cluster i
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


def clusterclubs(mycentroids, clustassing,numclust,datmat,labels,savep):#bikmeans分类画图
    otherpoints = []
    for i in range(numclust):
        ptsincurrcluster = datmat[nonzero(clustassing[:,0].A==i)[0], :]
        otherpoints.append(ptsincurrcluster.getA())
    # # title = []
    # for i in range(len(labels)):
    #     ch = labels[i].replace('\n', '').replace('\r', '')
    #     title.append(ch)
    #     if i != len(labels) - 1:
    #         title.append('--')
    # title = "".join(title)
    # plt.title('bik-means分类效果图\n'+title,fontsize=12)
    # plt.savefig(savep+'bik-means分类效果图.png')
    # addpicture(savep+'bik-means分类效果图.png')
    # plt.show()
    return otherpoints


def guiyihua(clearlist):#归一化
    params = {'project_id': id}
    res = requests.get('http://127.0.0.1:8000/api/get_parameter_kmeans', params=params)
    json_data = json.loads(res.text).get('data')
    df = json_normalize(json_data)
    data = df.drop(df.columns[[0, 1, 2, 3, 4, -1]], axis=1)
    dataset = data.drop(data.columns[column_list], axis=1)
    # print(dataset)
    datasety = dataset
    labels = dataset.columns
    dataset = dataset.values
    for i in range(dataset.shape[0]):
        for j in range(dataset.shape[1]):
            if (isinstance(dataset[i][j], str)):
                if (dataset[i][j].isspace()):
                    dataset[i][j].strip()
    k = []
    for i in range(dataset.shape[1]):
        p = normalization(dataset[:, i])

        if (i == 0):
            k = p
        else:
            k = np.c_[k, p]
    df = pd.DataFrame(k, columns=labels)

    return df,datasety,labels


def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range


def diaoyong(classnum, clearlist):
    df, datasety,labels = guiyihua(clearlist)
    df = mat(df.values)
    mycentroids, clustassing = bikmeans(df, classnum, distmeas=distEclud)
    return mycentroids,clustassing,df, labels


#层次聚类
def AgglomerativeClustering(path):
    import numpy
    import pandas
    from sklearn import datasets
    import scipy.cluster.hierarchy as hcluster

    df, datasety, labels = guiyihua(path)
    #df2 = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    corr_matrix = df.corr()
    matrix = (1 - abs(mat(corr_matrix.values)))*10
    # print(matrix)
    target = labels.values.T
    target = target.tolist()
    # print(target)
    # Compute and plot first dendrogram.
    linkage = hcluster.linkage(
        matrix,
        method='average'
    )

    hcluster.dendrogram(
        linkage,
        orientation='right',
        labels=target,
        leaf_rotation=0,
        leaf_font_size=9.
    )
    plt.title('层次聚类效果图')
    plt.savefig('层次聚类效果图.png')
    plt.show()


#聚类评价指数
def testnum(clearlist):
    from sklearn import metrics
    from sklearn.cluster import KMeans
    df, datasety, x = guiyihua(clearlist)
    df = mat(df.values)
    max = 0
    index = -1
    for i in range(2, 10):
        kmeans = KMeans(n_clusters=i, random_state=123).fit(df)
        score = metrics.calinski_harabasz_score(df, kmeans.labels_)
        if(score > max):
            max = score
            index = i
        # print("聚类%d簇的calinski_harabaz分数为：%f" % (i, score))

    return index


if __name__ == '__main__':

    savep = "images/"
    classnum = testnum(column_list)  # 聚类评价指数筛选最好的组数
    # print("best num: %d" % classnum)
    mycentroids, clustassing, df, labels = diaoyong(classnum, column_list)
    otherpoints = clusterclubs(mycentroids, clustassing, classnum, df, labels, savep)
    centpoints = mycentroids

    classifylist = clustassing[:, 0]
    classifylist = np.matrix.tolist(classifylist.T)
    classifylist = np.array(classifylist[0], dtype=int)

    df = np.array(df)

    xaxis = []
    yaxis = []
    xaxis.extend(df[:, 0])
    yaxis.extend(df[:, 1])

    params = {'project_id': id}
    res = requests.get('http://127.0.0.1:8000/api/get_parameter_kmeans', params=params)
    json_data = json.loads(res.text).get('data')
    df = json_normalize(json_data)
    district_list = df[['district']]
    districts = district_list.values[:, 0]

    json_data = {}
    json_data['project_id'] = id
    result_list = []
    for i in range(len(classifylist)):
        dict_data = {}
        dict_data['xaxis'] = xaxis[i]
        dict_data['yaxis'] = yaxis[i]
        dict_data['label'] = classifylist[i]
        dict_data['district'] = districts[i]
        result_list.append(dict_data)
    json_data['data'] = result_list
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/save_result_kmeans', data=json_data)

    dict = {}
    dict['project_id'] = id
    data = json.dumps(dict)
    requests.post('http://127.0.0.1:8000/api/finish_kmeans', data=data)




