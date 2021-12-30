
import pymysql
import pandas as pd
import os
import config
###需要配置
host = config.host
user = config.user
password = config.password
database = config.database
app_name = config.app_name
										# app的名称
db = pymysql.connect(host, user, password, database)  	# 数据库Ip, 用户，密码，选择数据库
cur = db.cursor()


class MysqlPandas():
	def __init__(self):
		pass
	def get_all_table(self):
		cur.execute('SHOW TABLES')                                     # 获取mysql中所有表
		results = cur.fetchall()
		ri_list = []
		for ri in results:
			ri_list.append(ri[0].strip(' '))
			# print(ri[0].strip(' '), type(ri[0]))
		return ri_list

	def get_tb_column(self, tb):                                        # 查看数据库中
		cur.execute("select * from {0}".format(tb))                # 查看这个表的列名
		column_name_list = []
		for column in cur.description:	
			column_name_list.append(column[0])
		return column_name_list

	def select_tb_by_cols_value_to_df(self, tb, cols, value):
		sql = '''
		select * from {0}
		where {1}='{2}'
		'''.format(tb, cols, value)
		cur.execute(sql)
		results = cur.fetchall()
		rows = []
		for row in results:
			rows.append(list(row))
		df = pd.DataFrame(rows, columns=self.get_tb_column(tb))
		return df


class PmedianProject():
	def __init__(self, project_id):
		self.project_id = project_id
		self.mp = MysqlPandas()
		tb_list = self.mp.get_all_table()
		if os.path.exists(os.path.dirname(__file__) + '/projects-logs/'+str(project_id)) is False:
			os.mkdir(os.path.dirname(__file__) + '/projects-logs/'+str(project_id))

	def data_extracter(self):
		pmedianbasic = app_name+'_pmedianbasic'
		pmediancostmatrix = app_name+'_pmediancostmatrix'
		pmediantransferstation = app_name+'_pmediantransferstation'
		pmedianrecyclingcenter = app_name+'_pmedianrecyclingcenter'
		df = self.mp.select_tb_by_cols_value_to_df(pmedianbasic, 'project_id', self.project_id)
		# print('pmedianbasic.................\n', df)
		df.to_csv(os.path.dirname(__file__) + '/projects-logs/'+str(self.project_id)+'/basic.csv', index=False, encoding='gbk')
		
		df = self.mp.select_tb_by_cols_value_to_df(pmediancostmatrix, 'project_id', self.project_id)
		# print('pmediancostmatrix.................\n', df)
		df.to_csv(os.path.dirname(__file__) + '/projects-logs/'+str(self.project_id)+'/costmatrix.csv', index=False, encoding='gbk')

		df = self.mp.select_tb_by_cols_value_to_df(pmediantransferstation, 'project_id', self.project_id)
		# print('pmediantransferstation.................\n', df)
		df.to_csv(os.path.dirname(__file__) + '/projects-logs/'+str(self.project_id)+'/transferstation.csv', index=False, encoding='gbk')
		
		df = self.mp.select_tb_by_cols_value_to_df(pmedianrecyclingcenter, 'project_id', self.project_id)
		# print('pmedianrecyclingcenter.................\n', df)
		df.to_csv(os.path.dirname(__file__) + '/projects-logs/'+str(self.project_id)+'/recyclingcenter.csv', index=False, encoding='gbk')


if __name__ == '__main__':
	a = PmedianProject('p001')
	a.data_extracter()





