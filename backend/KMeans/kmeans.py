# -*- coding: utf-8 -*-
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab as mpl
import sys
import os
import json
import requests

np.set_printoptions(suppress=True)
mpl.rcParams['font.sans-serif'] = ['simHei']
mpl.rcParams['axes.unicode_minus'] = False

id = sys.argv[1]


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

def clusterclubs(mycentroids, clustassing,numclust,datmat,labels):#bikmeans分类画图
    classlabel = []
    x = []
    y = []
    fig = plt.figure()
    rect=[0.1,0.1,0.8,0.8]
    scattermarkers=['s','o','^','8','p','d','v','h','>','<']
    axprops = dict(xticks=[],yticks=[])
    ax0=fig.add_axes(rect, label='ax0', **axprops)
    imgp = plt.imread(os.path.dirname(__file__)+'/1.jpg')
    ax0.imshow(imgp)
    ax1=fig.add_axes(rect, label='ax1', frameon=False)
    for i in range(numclust):
        ptsincurrcluster = datmat[nonzero(clustassing[:,0].A==i)[0], :]
        x.extend(np.array(ptsincurrcluster)[:, 0])
        y.extend(np.array(ptsincurrcluster)[:, 1])
        tmp = len(np.array(ptsincurrcluster[:, 0]))
        for j in range(tmp):
            classlabel.append(i)
        markerstyle = scattermarkers[i % len(scattermarkers)]
        ax1.scatter(ptsincurrcluster[:,0].flatten().A[0],ptsincurrcluster[:,1].flatten().A[0],marker=markerstyle, s=90)
    ax1.scatter(mycentroids[:,0].flatten().A[0],mycentroids[:,1].flatten().A[0],marker='+',s=300)

    json_data = {}
    json_data['project_id'] = id
    result_list = []
    for i in range(len(classlabel)):
        dict_data = {}
        dict_data['xaxis'] = x[i]
        dict_data['yaxis'] = y[i]
        dict_data['label'] = classlabel[i]
        result_list.append(dict_data)
    json_data['data'] = result_list
    json_data = json.dumps(json_data, cls=NpEncoder)
    requests.post('http://127.0.0.1:8000/api/save_result_kmeans', data=json_data)
    # title = []
    #
    # for i in range(len(labels)):
    #     ch = labels[i].replace('\n', '').replace('\r', '')
    #     title.append(ch)
    #     if i != len(labels) - 1:
    #         title.append('--')
    # title = "".join(title)
    # plt.title('bik-means分类效果图\n\n'+title,fontsize=9)
    # plt.savefig('bik-means分类效果图.png')
    # plt.show()


def guiyihua():#归一化
    dataset = pd.read_csv(os.path.dirname(__file__)+'/dataset_new1.csv')
    dataset = dataset.drop(dataset.columns[[0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]], axis=1)#0, 4, 8, 9, 10, 12, 13, 16, 17, -1#0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18
    dataset = dataset.fillna(0.1)
    datasety = dataset
    #print(dataset)
    labels = dataset.columns
    dataset = dataset.values
    for i in range(dataset.shape[0]):
        for j in range(dataset.shape[1]):
            if(isinstance(dataset[i][j], str)):
                if (dataset[i][j].isspace()):
                    dataset[i][j].strip()
    k=[]
    for i in range(dataset.shape[1]):
        p = normalization(dataset[:,i])

        if (i == 0): k = p
        else:
            k=np.c_[k, p]
    #print(k.shape)
    #print(k)
    #dataset.shape[1]
    #min_max_scaler = preprocessing.MinMaxScaler()
    #X_minMax = min_max_scaler.fit_transform(dataset)
    df = pd.DataFrame(k, columns=labels)#dataset
    # print(datasety)
    datasety.to_csv(os.path.dirname(__file__)+"/kmeans.csv")
    return df,datasety,labels

def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range

def diaoyong(classnum):
    df, datasety,labels = guiyihua()
    df = mat(df.values)
    mycentroids, clustassing = bikmeans(df, classnum, distmeas=distEclud)
    return mycentroids,clustassing,df,labels

#层次聚类
def AgglomerativeClustering(classnum):
    import numpy
    import pandas
    from sklearn import datasets
    import scipy.cluster.hierarchy as hcluster

    df, datasety, labels = guiyihua()
    #df2 = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    data = df.values.T
    print(type(data))
    target = labels.values.T
    target = target.tolist()
    print(type(target))
    # Compute and plot first dendrogram.
    linkage = hcluster.linkage(
        data,
        method='centroid'
    )

    hcluster.dendrogram(
        linkage,
        orientation='right',
        labels=target,
        leaf_rotation=0,
        leaf_font_size=8.
    )
    # plt.xticks(target)
    plt.title('层次聚类效果图')
    plt.savefig('层次聚类效果图.png')
    plt.show()
    hcluster.dendrogram(
        linkage,
        truncate_mode='lastp',
        p=12,
        leaf_font_size=12.
    )

    p = hcluster.fcluster(
        linkage,
        3,
        criterion='maxclust'
    )

    ct = pandas.DataFrame({
        'p': p,
        't': target
    }).pivot_table(
        index=['t'],
        columns=['p'],
        aggfunc=[numpy.size]
    )


#聚类评价指数
def testnum():
    from sklearn import metrics
    from sklearn.cluster import KMeans
    df, datasety = guiyihua()
    df = mat(df.values)
    for i in range(2, 10):
        kmeans = KMeans(n_clusters=i, random_state=123).fit(df)
        score = metrics.calinski_harabasz_score(df, kmeans.labels_)
        print("聚类%d簇的calinski_harabaz分数为：%f" % (i, score))



# testnum()#聚类评价指数
classnum = 4#聚类的组数

flag = 1#聚类方式选择,注意：选择层次聚类的时候要改guiyihua（）函数里面列的选择，多维的效果图好看一点
#如果bikmeans聚类的话，两维聚类的效果图好看一点
if flag==1:#层次聚类
    AgglomerativeClustering(classnum)
elif flag==2:#bikmeans聚类
    mycentroids,clustassing,df,labels= diaoyong(classnum)
    clusterclubs(mycentroids, clustassing,classnum,df,labels)
    #对scv文件添加分类列
    classifylist = clustassing[:,0]
    classifylist = np.matrix.tolist(classifylist.T)
    excel = pd.read_csv(os.path.dirname(__file__)+'/dataset_new1.csv')
    classifylist = np.array(classifylist[0], dtype = int)
    excel.loc[:,('Unnamed: 0')] = classifylist
    excel.rename(columns={'Unnamed: 0':'class'},inplace=True)
    excel.to_csv(os.path.dirname(__file__)+"/kmeansclassify.csv")#最终聚类表示文件

dict = {}
dict['project_id'] = id
data = json.dumps(dict)
requests.post('http://127.0.0.1:8000/api/finish_kmeans', data=data)
