import pandas as pd
import os
from math import radians, cos, sin, asin, sqrt




# 读取表
basic = pd.read_excel(os.path.dirname(__file__)+'/input/P-median-input.xlsx', sheet_name='basic', encoding='gbk')
ts = pd.read_excel(os.path.dirname(__file__)+'/input/P-median-input.xlsx', sheet_name='ts', encoding='gbk')
rrc = pd.read_excel(os.path.dirname(__file__)+'/input/P-median-input.xlsx', sheet_name='rrc', encoding='gbk')
cost_matrix = pd.read_excel(os.path.dirname(__file__)+'/input/P-median-input.xlsx', sheet_name='cost_matrix', encoding='gbk')

ts_numbers = ts.shape[0]                # 提取参数
rrc_numbers = rrc.shape[0]
min_p = rrc[rrc['has_selected']==1].reset_index(drop=True).shape[0]
trans_cost = basic[basic['name']=='trans_cost'].reset_index(drop=True)['value'][0]  	# 元/(km*吨)
total_msw = basic[basic['name']=='MSW'].reset_index(drop=True)['value'][0]				# 千吨
recyclable_percent = basic[basic['name']=='recyclable_percent'].reset_index(drop=True)['value'][0]
recyling_rate = basic[basic['name']=='recyling_rate'].reset_index(drop=True)['value'][0]
scale_cost = basic[basic['name']=='scale_cost'].reset_index(drop=True)['value'][0]
factor_m_cost = basic[basic['name']=='factor_m_cost'].reset_index(drop=True)['value'][0]


def get_params():                                                           
    keys = 'ts_numbers, rrc_numbers, min_p'.split(', ')                     			# 构造字典
    values = [ts_numbers, rrc_numbers, min_p]
    params = dict(zip(keys, values))
    return params


def get_weight_ts():
	weight_ts = []
	for pi in ts['weight_percentage']:
		wi = int(1000*total_msw*pi*recyclable_percent*recyling_rate+0.499) 	# 吨
		# print(wi)
		weight_ts.append(wi)
	return weight_ts

def get_max_load():
	list1 = list(rrc['max_load(千吨/年)'])
	res = [i*1000 for i in list1]
	return res


def get_has_selected():
	res = list(rrc['has_selected'])
	return res

def get_weight_distance_df(ts, rrc):
	weight_ts = get_weight_ts()
	rows = []
	for i in range(ts.shape[0]):
		row_i = []
		for j in range(rrc.shape[0]):
			lon1, lat1, lon2, lat2 = map(radians, [ts['lng'][i], ts['lat'][i], rrc['lng'][j], rrc['lat'][j]])
			dlon = lon2 - lon1 
			dlat = lat2 - lat1 
			a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
			c = 2 * asin(sqrt(a)) 
			r = 6371 																	# 地球平均半径，单位为公里
			dij = c * r
			weight_dij = int(dij*weight_ts[i]*trans_cost+0.499)
			row_i.append(weight_dij)

		rows.append(row_i)
	df = pd.DataFrame(rows, columns = rrc['sub_district'])
	df = df/10000  # 变成万元
	# df.to_csv('distance.csv', encoding='gbk')
	return df


def get_cost_df():
	# 构造cost_matrix
	if cost_matrix.shape[0]<ts_numbers:     	# 如果cost_matrix为空，则构造欧几里得距离（也可以先计算好输入--根据路网距离/时间等等参数）
	    cost_matrix_r = get_weight_distance_df(ts, rrc)
	if cost_matrix.shape[0]==ts_numbers:     	# 如果cost_matrix为空，则构造欧几里得距离（也可以先计算好输入--根据路网距离/时间等等参数）
	    cost_matrix_r = cost_matrix
	return cost_matrix_r

