# -*- coding:utf-8 -*-
# @Time : 2022-06-04 20:40
# @Author : 肖紫心
# @File : test2.py
# @Software : PyCharm



url('add_xgboost_project', views.add_xgboost_project),  # 添加xgboost项目
url('get_xgboost_project', views.get_xgboost_project),  # 获取xgboost项目
url('amend_xgboost_project', views.amend_xgboost_project),  # 修改xgboost项目
url('start_xgboost', views.start_xgboost),  # 开始xgboost试验
url('finish_xgboost', views.stop_xgboost),  # 结束xgboost算法
url('get_result_xgboost', views.get_result_xgboost),  # 获得xgboost实验结果
url('get_id_xgboost', views.get_idlist_xgboost),  # 获取xgboost所有项目编号
url('get_xgboost_testreport', views.getxgboostTestReport),  # 获取xgboost报告


url('uploadxgboostfile', views.uploadxgboostFile),  # 上传xgboost数据文件
url('getxgboostfilelist', views.getmodelxgboostfilelist),  # 获取xgboost数据文件
url('getxgboostmodelresult', views.getxgboostModelResult),  # 获取xgboost模型结果
