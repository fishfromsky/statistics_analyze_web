
import pandas as pd
import matplotlib.pyplot as plt

import sys
import os
import numpy as np
from math import radians, cos, sin, asin, sqrt
from numpy import random
#from gurobipy import *
import geopandas as gpd
from shapely import geos
from shapely.geometry import Point, LineString, shape
import fiona
from fiona.crs import from_epsg, from_string
import os
from shapely.geometry import Polygon
from copy import deepcopy





def point_to_geo(df, lon, lat):                                                 # pandas批量画点
    df['geometry'] = gpd.GeoSeries(list(zip(df[lon], df[lat]))).apply(Point)    # 识别经纬度，转换点数据
    df = gpd.GeoDataFrame(df)                                                   # 转换Geodataframe格式
    df.crs = {'init': 'epsg:4326'}                                              # 定义坐标系WGS84
    del df[lon]
    del df[lat]
    return df


def geo_one_point_plot(lng, lat, base):                                         # 画点
    point1 = Point(lng, lat)
    point_df = gpd.GeoDataFrame(geometry=[point1])
    point_df.plot(ax=base, color='black', alpha=0.5)


#
def plot_type():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    volumns = cost_volume
    allocates = cost_allocate
    allocates = allocates[allocates['decision Varibles']==1].reset_index(drop=True)
    choosed_rrcs = allocates['rrc'].unique()

    ax.scatter(ts['lng'], ts['lat'], s=ts['total_weight'], alpha=1, c='black', label='ts', marker='s')
    
    print(choosed_rrcs)
    for i in choosed_rrcs:
        index_rrc_i = i-1
        if has_selected[index_rrc_i] ==1 and rrc['sub_district'][index_rrc_i]!='山阳镇':
            ax.scatter(rrc['lng'][index_rrc_i], rrc['lat'][index_rrc_i], s=volumns[index_rrc_i]/300+500, alpha=0.8, c='darkgreen')
        else:
            ax.scatter(rrc['lng'][index_rrc_i], rrc['lat'][index_rrc_i], s=volumns[index_rrc_i]/300+500, alpha=0.8, c='red')
        plt.text(rrc['lng'][index_rrc_i], rrc['lat'][index_rrc_i]+0.02, rrc['sub_district'][index_rrc_i], fontsize=40)
    for i in range(allocates.shape[0]):
        ts_index=allocates['ts'][i]-1
        rrc_index=allocates['rrc'][i]-1
        x_list = [ts['lng'][ts_index], rrc['lng'][rrc_index]]
        y_list = [ts['lat'][ts_index], rrc['lat'][rrc_index]]
        plt.plot(x_list, y_list, color='black', linewidth=1.5)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())        # 去掉x轴刻度
    plt.gca().yaxis.set_major_locator(plt.NullLocator())        # 去掉y轴刻度
    plt.savefig('static/plot_allocation_geofig01.png', dpi=300)                    # 保存图片
    ax.legend()
    plt.clf()

def getPicture(plot_num):
    return

p = sys.argv[1]
basic = pd.read_excel(os.path.dirname(__file__)+'/input/P-median-input.xlsx', sheet_name='basic', encoding='gbk')
rrrrc = pd.read_excel(os.path.dirname(__file__)+'/input/P-median-input.xlsx', sheet_name='rrc', encoding='gbk')
has_selected = list(rrrrc['has_selected'])
total_msw = basic[basic['name']=='MSW'].reset_index(drop=True)['value'][0]              # 千吨

cost_allocate = pd.read_csv(os.path.dirname(__file__)+'/output/p='+str(p)+'/r_Yij.csv', encoding='gbk')                    # p根据要求改
cost_weight = pd.read_csv(os.path.dirname(__file__)+'/output/rrc_built_rows.csv', encoding='gbk')          # 重量信息
for i in range(cost_weight.shape[0]):
    list_i = list(cost_weight.iloc[i])
    new_list = [i for i in list_i if i > 0]
    if len(new_list) == p:
        print(list_i)
        break

cost_volume = list_i
print('cost_volume......', cost_volume)

rrc = pd.read_excel(os.path.dirname(__file__)+'/input/P-median-input.xlsx', encoding='gbk', sheet_name='rrc')
ts = pd.read_excel(os.path.dirname(__file__)+'/input/P-median-input.xlsx', encoding='gbk', sheet_name='ts')
ts['total_weight'] = total_msw*ts['weight_percentage']
# -------------------------------------------------画底图
fig, ax = plt.subplots(1, 1, figsize=(30, 30))


shanghai_district = gpd.GeoDataFrame.from_file(os.path.dirname(__file__)+'/input/shapefile/上海区界.shp', encoding='gb18030')  # 读取shapfile数据为geodataframe格式
shanghai_district.plot(color='white', edgecolor='black', ax=ax, label='district')             # 画底图
vol_max = ts['total_weight'].max()
t = ts['total_weight']/vol_max*300
ts['total_weight'] = t

plot_type()
