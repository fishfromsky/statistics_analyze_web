from django.conf.urls import url
from . import views
import backend.modelview.pmedianbasic_v as pmedianbasicviews
import backend.modelview.pmediancostmatrix_v as pmediancostmatrixviews
import backend.modelview.pmedianoutputallocationmatrix_v as pmedianoutputallocationmatrixviews
import backend.modelview.pmedianoutputbuildscale_v as pmedianoutputbuildscaleviews
import backend.modelview.pmedianoutputcostmatrix_v as pmedianoutputcostmatrixviews
import backend.modelview.pmedianrecyclingcenter_v as pmedianrecyclingcenterviews
import backend.modelview.pmediantransferstation_v as pmediantransferstationviews

urlpatterns = [
    url('login', views.login, name='login'),
    url('info', views.getInfo, name='getInfo'),
    url('logout', views.logout, name='logout'),
    url('addmodel', views.addModel, name='addModel'),
    url('getmodel', views.getModel, name='getModel'),
    url('getteacher', views.getteacher),
    url('fetchmodel', views.fetchModel, name='fetchModel'),
    url('getsuperuser', views.fetchsuperuser, name='fetchSuperuser'),
    url('fetchsuperuser', views.filtersuperuser, name='filtersuperuser'),
    url('amendmodel', views.amendmodel, name='amendmodel'),
    url('deletemodel', views.deletemodel, name='deletemodel'),
    url('addsuperuser', views.addsuperuser, name='addsuperuser'),
    url('addteacher', views.addteacher),
    url('filterteacher', views.filterteacher),
    url('deleteteacher', views.deleteteacher),
    url('deletesuperuser', views.deletesuperuser, name='deleteSuperuser'),
    url('add_city', views.addCity, name='addCity'),  # 批量导入城市
    url('adddistrict', views.addDistrict, name='addDistrict'),  # 批量导入区
    url('addtown', views.addTown, name='addTown'),  # 批量导入城镇
    url('addbatchgarbagecity', views.addbatchgarbagedata_city, name='addbatchgarbagedata_city'),  # 批量导入生活垃圾数据
    url('addcitygarbagedeal', views.addGarbageDealCity, name='addGarbageDeal'),  # 批量导入无害化处理厂数据
    url('addcitygarbagecapacity', views.addGarbageDealCapacityCity, name='addGarbageDealCapacityCity'),  # 批量导入无害化处理能力数据
    url('addcitygarbagevolume', views.addGarbageDealVolumeCity, name='addGarbageDealVolumeCity'),  # 批量导入无害化处理量数据
    url('addcityeconomy', views.addEconomyCity, name='addEconomyCity'),  # 批量导入城市经济信息
    url('addcitypopulation', views.addPopulationCity, name='addPopulationCity'),  # 批量导入城市人口信息
    url('adddangerousgarbagecity', views.addDangerousGarbageCity),  # 批量导入危险垃圾处置表
    url('getdangerousgarbage', views.getDangerousGarbageCity),  # 获取危险垃圾处置表信息
    url('amenddangerousgarbage', views.amenddangerousgarbage),  # 修改危险垃圾处置表信息
    url('deletedangerousgarbage', views.deletedangerousgarbage),  # 删除危险垃圾处置信息
    url('addbyrow_dangerousgarbage', views.addbyrow_dangerousgarbage),  # 添加危险垃圾处置信息
    url('addgarbageclear', views.addGarbageClear),  # 添加日均清运量
    url('getgarbageclearperday', views.getGarbageClearPerDay),  # 获取垃圾日均清运量
    url('amendgarbageclearperday', views.amendGarbageClearPerDay),  # 修改垃圾日均清运量
    url('deletegarbageclearperday', views.deleteGarbageClearPerDay),   # 删除垃圾日均清运量
    url('addsinglerowforgarbageclear', views.addSingleRowforGarbageClear),   # 增加单条垃圾清运量数据
    url('addirongarbage', views.addirongarbage),  # 增加废钢铁数据
    url('amendirongarbage', views.amendIronGarbage),  # 修改废钢铁数据
    url('getirongarbage', views.getIronGarbage),  # 获取废钢铁数据
    url('geteconomycity', views.geteconomydata_city, name='geteconomycity'),  # 请求城市经济表
    url('getpopulationcity', views.getpopulation_city, name='getpopulationcity'),  # 请求城市人口表
    url('getgarbagecity', views.getgarbage_city, name='getgarbageinfo'),  # 请求城市生活垃圾表
    url('inputgarbagecountry', views.InputGarbageCountry),  # 批量导入城镇垃圾产量表
    url('getgarbagecountry', views.getGarbageCountry),  # 获取城镇垃圾产量表
    url('amendgarbagecountry', views.amendGarbageCountry),  # 修改城镇垃圾产量表
    url('deletegarbagecountry', views.deleteGarbageCountry),  # 删除城镇垃圾产量表
    url('addgarbagecountry', views.addGarbageCountry),  # 增加城镇垃圾产量表
    url('getgarbagedealcity', views.getgarbagedeal_city, name='getgarbagedeal'),  # 请求城市无害化处理厂表
    url('getgarbagecapacitycity', views.getgarbagecapacity_city, name='getgarbagecapacity'),  # 请求城市无害化处理能力表
    url('getgarbagevolumecity', views.getgarbagevolume_city, name='getgarbagevolume'),  # 请求城市无害化处理能力表
    url('amendcityeconomydata', views.amendeconomydata_city, name='amendcityeconomydata'),  # 修改城市经济表中数据
    url('deletecityeconomydata', views.deleteeconomydata_city, name='deletecityeconomydata'),  # 删除经济表中数据
    url('amendcitypopulationdata', views.amendpopulationdata_city, name='amendcitypopulationdata'),  # 修改城市人口表数据
    url('deletecitypopulationdata', views.deletepopulationdata_city, name='deletecitypopulationdata'),  # 删除城市人口表数据
    url('amendcitygarbagedata', views.amendgarbagedata_city, name='amendcitygarbagedata'),  # 修改城市生活垃圾表中的数据
    url('deletecitygarbagedata', views.deletegarbagedata_city, name='deletecitygarbagedata'),  # 删除城市生活垃圾表数据
    url('amendcitygarbagedealdata', views.amendgarbagedealdata_city, name='amendcitygarbagedealdata'),  # 修改城市无害化处理厂表数据
    url('deletecitygarbagedealdata', views.deletegarbagedealdata_city, name='deletecitygarbagedealdata'),  # 删除城市无害化处理厂表数据
    url('amendcitygarbagecapacitydata', views.amendgarbagecapacitydata_city, name='amendcitygarbagecapacitydata'),  # 修改城市无害化处理能力表数据
    url('deletecitygarbagecapacitydata', views.deletegarbagecapacitydata_city, name='deletecitygarbagecapacitydata'),  # 删除城市无害化处理能力表数据
    url('amendcitygarbagevolumedata', views.amendgarbagevolumedata_city, name='amendcitygarbagevolumedata'),  # 修改城市无害化处理量表数据
    url('deletecitygarbagevolumedata', views.deletegarbagevolumedata_city, name='deletecitygarbagevolumedata'),  # 删除城市无害化处理量表数据
    url('addsinglepopulation', views.addsinglepopulation, name='addsinglepopulation'),  # 添加一条人口表数据
    url('addsinglegarbage', views.addsinglegarbageinfocity, name='addsinglegarbage'),  # 添加一条生活垃圾表数据
    url('addsingledealgarbage', views.addsinglegarbagedealcity, name='addsinglegarbagedeal'),  # 添加一条无害化处理厂表数据
    url('addsinglecapacitygarbage', views.addsinglegarbagedealcapacity, name='addsinglegarbagecapacity'),  # 添加一条无害化处理能力表数据
    url('addsinglevolumegarbage', views.addsinglegarbagedealvolume, name='addsinglegarbagevolume'),  # 添加一条无害化处理量表数据
    url('addsinglerowdata', views.addsinglerow_cityeconomy, name='addsinglerowdata'),  # 添加一条经济表数据
    url('getgarbagecity', views.getgarbagepropduction_city),
    url('addpmedianproject', views.add_p_median_project, name='addpmedianproject'),  # 添加p_median项目
    url('getpmedianproject', views.getpmedianproject, name='getpmedianproject'),  # 请求p_median项目
    url('amendpmedianproject', views.amendpmedianproject, name='amendpmedianproject'),  # 修改p_median项目
    url('getnationwaterpollution', views.get_water_pollution, name='getwaterpollution'),  # 爬取国内水体污染数据
    url('getnationpm', views.get_nation_pm, name='getnationpm'),  # 爬取国内空气污染数据
    url('getnationsolidpollution', views.get_nation_solid_pollution, name='getnationsolidpollution'),  # 爬取国内固废垃圾数据
    url('getworldpm', views.get_world_pm, name='getworldpm'),  # 爬取世界空气污染数据
    url('addcityfactorylist', views.addFactoryListCity, name='addFactoryListCity'),  # 批量导入处理厂信息
    url('getfactorylist', views.getfacotylist, name='getFactorylist'),     # 获取处理厂信息
    url('addtransferfactory', views.addTransferFactory, name='addTransferFacory'),   # 批量导入中转站信息
    url('gettransferfactory', views.getTransferFactory, name='getTransferFactory'),   # 获取垃圾中转站信息
    url('amendfactorylist', views.amendfactorylist, name='amendFactoryList'),     # 修改无害化处理厂信息表
    url('deletefactorylist', views.deletefactorylist, name='deletefactorylist'),  # 删除无害化处理厂信息
    url('addfactorylist', views.addfactorylistbyrow, name='addfactorylist'),   # 增加无害化处理厂信息
    url('amendtransferfactory', views.AmendTransferFactory, name='AmendTransferFactory'),   # 修改中转站信息
    url('deletetransferfactory', views.DeleteTransferFactory, name='DeleteTransferFactory'),   # 删除中转站信息
    url('addtransferbyrow', views.addtransferbyrow, name='AddTransferFactoryByRow'),  # 添加中转站信息
    url('addcollectfactory', views.AddCollectFactory, name='AddCollectFactory'),   # 批量导入收集点数据
    url('getcollectfactorybyarea', views.GetCollectFactoryByArea, name='GetCollectFactoryByArea'),   # 根据区域获得指定收集点信息
    url('getcrawlrecord', views.get_crawl_record, name='getcrawlrecord'),  # 获取使用爬虫历史记录
    url('deletecrawldata', views.delete_crawl_data, name='deletecrawldata'),  # 删除爬取的数据
    url('getcrawl_select', views.get_crawl_record_select, name='getcrawl_select'),  # 筛选历史爬虫数据
    url('startpmedianproject', views.start_p_median_project, name='startpmedianproject'),  # 运行p_median项目

    url('add_element_garbage', views.input_garbage_element),  # 批量导入垃圾成分数据
    url('get_element_garbage', views.get_garbage_element),    # 获取垃圾成分表数据
    url('insert_element_garbage', views.add_garbage_element),  # 新增一条垃圾成分数据
    url('delete_element_garbage', views.delete_garbage_element),  # 删除一条垃圾成分数据
    url('amend_element_garbage', views.amend_element_garbage),  # 修改一条垃圾成分数据

    url('geteconomydistrict', views.getEconomyDistrict),  # 获取区级经济信息
    url('amendeconomydistrict', views.amendEconomyDistrict),   # 修改区级经济信息
    url('inputeconomydistrict', views.InputEconomyDistrict),  # 批量导入区级经济信息
    url('addeconomydistrict', views.addEconomyDistrict),  # 添加一条区级经济信息
    url('deleteeconomydistrict', views.deleteEconomyDistrict),  # 删除区级经济信息
    url('filtereconomydistrict', views.filterEconomyDsitrict),  # 根据行政区筛选经济信息
    url('filterPieeconomydistrict', views.filterPieDataEconomyDistrict),   # 根据区域和年份筛选区域经济信息
    url('filterBareconomydistrict', views.filterBarDataEconomyDistrict),  # 根据年份筛选数据

    url('getpopulationdistrict', views.getPopulationDistrict),  # 获取人口区域信息
    url('inputpopulationdistrict', views.InputPopulationDistrict),  # 批量导入人口区域信息表
    url('addpopulationdistrict', views.addPopulationDistrict),   # 添加人口区域信息表
    url('amendpopulationdistrict', views.amendPopulationDistrict),  # 修改人口区域信息表
    url('deletepopulationdistrict', views.deletePopulationDistrict),  # 删除人口区域信息表
    url('filterlinepopulationdistrict', views.filterLinepopulationDistrict),   # 根据地区筛选人口数据
    url('filterbarpopulationdistrict', views.filterBarPopulationDistrict),  # 根据年份筛选人口数据

    url('startgrouptestregression', views.grouptest_regression),  # 开始多元回归算法
    url('finishgrouptestregression', views.grouptest_finish_regression),  # 结束多元回归算法
    url('getregressionexcelresult', views.getRegressionExcelResult),  # 获取多元回归算法excel文件

    url('startgrouptestkmeans', views.grouptest_kmeans),  # 开始模型实验kmeans算法
    url('getkmeansexcelresult', views.getKMeansExcelResult),  # 获取模型实验kmeans算法

    url('getlstmproject', views.get_lstm_project, name='getlstmproject'),  # 获取lstm项目
    url('addlstmproject', views.add_lstm_project, name='addlstmproject'),  # 添加lstm项目
    url('amendlstmproject', views.amend_lstm_project, name='amendlstmproject'),  # 修改lstm项目
    url('lstm_project_id', views.lstm_project_id, name='lstm_project_id'),  # 获得全部LSTM项目编号
    url('experiment_lstm_start', views.experiment_lstm_start, name='experiment_lstm'),  # 开始试验
    url('experiment_lstm_finish', views.experiment_lstm_finish, name='experiment_lstm_finish'),  # 结束实验
    url('get_lstm_result', views.get_lstm_result, name='get_lstm_resut'),  # 获取lstm实验结果

    url('addlinearregressionproject', views.addLinearRegressionProject),  # 添加多元线性回归
    url('getlinearregressionproject', views.getLinearRegressionProject),  # 获取多元线性回归
    url('amendlinearregressionproject', views.amendLinearRegressionProject),  # 修改多元线性回归
    url('getlinearregressionidlist', views.getLinearRegressionidlist),  # 获取项目ID
    url('startlinearregressionexperiment', views.startLinearRegressionExperiment),  # 开始多元线性回归实验
    url('savelinearregressionresult', views.saveLinearRegressionResult),  # 保存多元线性回归实验结果
    url('finishlinearregression', views.finishLinearRegression),  # 结束线性回归实验
    url('getlinearregressionresult', views.getLinearRegressionResult),  # 获取多元线性回归结果

    url('get_regression', views.get_regression_programe),  # 获取多元回归项目
    url('add_regression', views.add_regression_programe),  # 添加多元回归项目
    url('amend_regression', views.amend_regression_programe),  # 修改多元回归模型
    url('get_id_regression', views.regression_idlist),  # 获得多元回归所有项目编号
    url('start_regression_experiment', views.start_regression_experiment),  # 开始多元回归实验
    url('finish_regression_experiment', views.finish_regression_experiment),  # 结束多元回归实验
    url('get_result_regression', views.get_regression_result),  # 获取多元回归实验结果

    url('add_kmeans_project', views.add_kmeans_project),  # 添加kmeans项目
    url('get_kmeans_project', views.get_kmeans_project),  # 获取kmeans项目
    url('amend_kmeans_project', views.amend_kmeans_project),  # 修改kmeans项目
    url('start_kmeans', views.start_kmeans),  # 开始kmeans试验
    url('finish_kmeans', views.stop_kmeans),  # 结束kmeans算法
    url('get_result_kmeans', views.get_result_kmeans),  # 获得kmeans实验结果
    url('get_id_kmeans', views.get_idlist_kmeans),  # 获取kmeans所有项目编号
    url('get_kmeans_testreport', views.getKMeansTestReport),  # 获取kmeans报告

    url('add_relation_project', views.add_relation_project),  # 添加关联分析项目
    url('get_relation_project', views.get_relation_project),  # 获得关联分析项目
    url('amend_relation_project', views.amend_relation_project),  # 修改关联分析项目信息
    url('get_id_relation', views.get_idlist_relation),  # 获得关联分析项目编号
    url('get_relation_parameter', views.get_relation_parameter),  # 获得关联分析参数
    url('input_relation_parameter', views.input_relation_parameter),  # 导入关联分析参数
    url('save_relation_hot_matrix_result', views.save_relation_hot_matrix_result),  # 保存关联分析混淆矩阵结果
    url('start_relation', views.start_relation),  # 开始运行关联分析
    url('stop_relation', views.stop_relation),  # 结束运行关联分析模型
    url('get_relation_hot_matrix_result', views.get_relation_hot_matrix_result),  # 获取关联分析混淆矩阵结果
    url('save_relation_RF_result', views.save_relation_RF_result),  # 保存关联分析随机森林结果
    url('save_grey_relation_result', views.save_Grey_Relation_Result),  # 保存关联分析灰色模型结果
    url('get_grey_relation_result', views.get_grey_relation_result),  # 获取关联分析灰色模型结果
    url('get_relation_rf_result', views.get_relation_RF_result),  # 获得关联分析随机分析结果
    url('save_pearson_result', views.save_pearson_result),  # 保存皮尔逊系数结果
    url('get_pearson_result', views.get_pearson_relation_result),  # 获取皮尔逊系数结果

    url('add_garbage_district', views.inputGarbageDistrict),  # 批量导入区域固废信息表
    url('get_garbage_district', views.getGarbageDistrict),  # 获取区域固废信息表
    url('addbyrowgarbagedistrict', views.addbyrowGarbageDistrict),  # 添加区域固废信息
    url('amendgarbagedistrict', views.amendGarbageDistrict),  # 修改区域固废信息
    url('deletegarbagedistrict', views.deleteGarbageDistrict),  # 删除区域固废信息
    url('filtergarbagedistrictbyyear', views.filterGarbageDistrictByYear),  # 根据年份筛选区域固废信息

    url('getlinearregressiontestreport', views.getLinearRegressionTestReport),  # 获取模型运行相关指标报告
    url('getregressionreport', views.getRegressionReport),  # 获取多元非线性回归模型运行指标报告
    url('getlstmreport', views.getLSTMReport),  # 获取lstm报告

    url('get_algorithm_list', views.get_algorithm_list),  # 获取算法模型列表
    url('add_algorithm_list', views.add_algorithm_list),  # 添加算法模型列表
    url('delete_algorithm_list', views.delete_algorithm_list),  # 删除算法模型列表
    url('get_idlist_algorithm', views.get_algorithm_idlist),  # 获取算法模型ID列表
    url('getbyid_algorithm', views.getbyid_algorithm),   # 根据ID获取模型
    url('getrelationexcelresult', views.getRelaionExcelResultList),  # 获取关联分析excel
    url('deleterelationexcel', views.DeleteRelationExcelResult),  # 删除关联分析excel
    url('finishgrouptestrelation', views.grouptest_finish_relation),  # 完成关联分析

    url('startgrouptestlstm', views.grouptest_lstm),  # 开始lstm模型实验
    url('getlstmexcelresult', views.getLSTMExcelResultList),  # 获取lstm算法实验结果
    url('grouptestfinishlstm', views.grouptest_finish_lstm),  # 完成LSTM算法实验

    url('uploadlstmmodelfile', views.uploadLSTMModelFile),  # 上传LSTM模型数据文件
    url('getlstmmodelfile', views.getmodellstmfilelist),  # 获取LSTM模型数据文件
    url('getlstmmodelresult', views.getlstmmodelresult),  # 获取lstm模型结果
    url('deletefilemodel', views.deleteModelFile),  # 删除模型数据文件
    url('getdatasetfromresult', views.getdatasetfromresult),  # 从结果文件中获取数据文件

    url('uploadlinearregressionfile', views.uploadLinearRegressionFile),  # 上传线性回归数据文件
    url('getlinearregressionmodelfile', views.getmodellinearregressionfilelist),  # 获取线性回归数据文件
    url('getfileresultlinearregression', views.getLinearRegressionModelResult),  # 获取多元线性回归结果文件

    url('uploadregressionfile', views.uploadRegressionFile),  # 获取多元非线性回归数据文件
    url('getregressionfilelist', views.getmodelregressionfilelist),  # 获取多元非线性回归数据文件
    url('getregressionmodelresult', views.getRegressionModelResult),  # 获取多元非线性回归数据文件

    url('uploadkmeansfile', views.uploadKMeansFile),  # 上传kmeans数据文件
    url('getkmeansfilelist', views.getmodelkmeansfilelist),  # 获取kmeans数据文件
    url('getkmeansmodelresult', views.getKmeansModelResult),  # 获取kmeans模型结果

    url('getallmodels', views.getallmodels),  # 获取所有模型列表
    url('upload_img', views.upload_img),  # 上传图片文件
    url('savemodel', views.savemodels),  # 保存模型
    url('filtermodels', views.filtermodels),  # 根据类型筛选模型
    url('get_model_construction', views.getmodelconstruction),  # 获取对应用户对应算法下的模型列表
    url('model_message', views.modelmessage),  # 获取指定模型信息
    url('select_model_add', views.select_model_add),  # 增加特定算法中的模型
    url('select_model_delete', views.select_model_delete),  # 删除特定算法中的模型

    url('algorithmtest', views.algorithmtest),  # 获取算法实验数据
    url('uploadfile', views.upload_file),  # 上传算法数据文件
    url('getdatafilelist', views.getdatafilelist),  # 获取算法列表
    url('getexceldetail', views.getexceldetail),  # 获取excel表信息
    url('grouptest_relation', views.grouptest_relation),  # 组合模型关联分析处理

    url('pmedianbs/list', pmedianbasicviews.pmedianbs_list_get, name='pmedianbs_list_get'),
    url('pmedianbs/download', pmedianbasicviews.pmedianbs_download_get, name='pmedianbs_create_get'),
    url('pmedianbs/create', pmedianbasicviews.pmedianbs_create_post, name='pmedianbs_create_post'),
    url('pmedianbs/update', pmedianbasicviews.pmedianbs_update_post, name='pmedianbs_update_post'),
    url('pmedianbs/delete', pmedianbasicviews.pmedianbs_delete_post, name='pmedianbs_delete_post'),
    url('pmedianbs/upload', pmedianbasicviews.pmedianbs_upload_post, name='pmedianbs_upload_post'),
    url('pmedianbs/clear', pmedianbasicviews.pmedianbs_clear_post, name='pmedianbs_clear_post'),

    url('pmediancstmtr/list', pmediancostmatrixviews.pmediancstmtr_list_get, name='pmediancstmtr_list_get'),
    url('pmediancstmtr/download', pmediancostmatrixviews.pmediancstmtr_download_get, name='pmediancstmtr_create_get'),
    url('pmediancstmtr/create', pmediancostmatrixviews.pmediancstmtr_create_post, name='pmediancstmtr_create_post'),
    url('pmediancstmtr/update', pmediancostmatrixviews.pmediancstmtr_update_post, name='pmediancstmtr_update_post'),
    url('pmediancstmtr/delete', pmediancostmatrixviews.pmediancstmtr_delete_post, name='pmediancstmtr_delete_post'),
    url('pmediancstmtr/upload', pmediancostmatrixviews.pmediancstmtr_upload_post, name='pmediancstmtr_upload_post'),
    url('pmediancstmtr/clear', pmediancostmatrixviews.pmediancstmtr_clear_post, name='pmediancstmtr_clear_post'),

    url('utputallocation/allist', pmedianoutputallocationmatrixviews.getalllist_utputallocation),  # 根据项目名称获取所有数据

    url('utputallocation/list', pmedianoutputallocationmatrixviews.utputallocation_list_get,
        name='utputallocation_list_get'),
    url('utputallocation/download', pmedianoutputallocationmatrixviews.utputallocation_download_get,
        name='utputallocation_create_get'),
    url('utputallocation/create', pmedianoutputallocationmatrixviews.utputallocation_create_post,
        name='utputallocation_create_post'),
    url('utputallocation/update', pmedianoutputallocationmatrixviews.utputallocation_update_post,
        name='utputallocation_update_post'),
    url('utputallocation/delete', pmedianoutputallocationmatrixviews.utputallocation_delete_post,
        name='utputallocation_delete_post'),
    url('utputallocation/upload', pmedianoutputallocationmatrixviews.utputallocation_upload_post,
        name='utputallocation_upload_post'),
    url('utputallocation/clear', pmedianoutputallocationmatrixviews.utputallocation_clear_post,
        name='utputallocation_clear_post'),

    url('dianoutputbuilds/list', pmedianoutputbuildscaleviews.dianoutputbuilds_list_get,
        name='dianoutputbuilds_list_get'),
    url('dianoutputbuilds/download', pmedianoutputbuildscaleviews.dianoutputbuilds_download_get,
        name='dianoutputbuilds_create_get'),
    url('dianoutputbuilds/create', pmedianoutputbuildscaleviews.dianoutputbuilds_create_post,
        name='dianoutputbuilds_create_post'),
    url('dianoutputbuilds/update', pmedianoutputbuildscaleviews.dianoutputbuilds_update_post,
        name='dianoutputbuilds_update_post'),
    url('dianoutputbuilds/delete', pmedianoutputbuildscaleviews.dianoutputbuilds_delete_post,
        name='dianoutputbuilds_delete_post'),
    url('dianoutputbuilds/upload', pmedianoutputbuildscaleviews.dianoutputbuilds_upload_post,
        name='dianoutputbuilds_upload_post'),
    url('dianoutputbuilds/clear', pmedianoutputbuildscaleviews.dianoutputbuilds_clear_post,
        name='dianoutputbuilds_clear_post'),

    url('pmedianoutputcomx/list', pmedianoutputcostmatrixviews.pmedianoutputcomx_list_get,
        name='pmedianoutputcomx_list_get'),
    url('pmedianoutputcomx/download', pmedianoutputcostmatrixviews.pmedianoutputcomx_download_get,
        name='pmedianoutputcomx_create_get'),
    url('pmedianoutputcomx/create', pmedianoutputcostmatrixviews.pmedianoutputcomx_create_post,
        name='pmedianoutputcomx_create_post'),
    url('pmedianoutputcomx/update', pmedianoutputcostmatrixviews.pmedianoutputcomx_update_post,
        name='pmedianoutputcomx_update_post'),
    url('pmedianoutputcomx/delete', pmedianoutputcostmatrixviews.pmedianoutputcomx_delete_post,
        name='pmedianoutputcomx_delete_post'),
    url('pmedianoutputcomx/upload', pmedianoutputcostmatrixviews.pmedianoutputcomx_upload_post,
        name='pmedianoutputcomx_upload_post'),
    url('pmedianoutputcomx/clear', pmedianoutputcostmatrixviews.pmedianoutputcomx_clear_post,
        name='pmedianoutputcomx_clear_post'),
    url('pmedianoutputcomx/cost', pmedianoutputcostmatrixviews.pmedianoutputcomx_get_cost, name='pmedianoutputcomx_get_cost'),

    url('pmedianreccen/list', pmedianrecyclingcenterviews.pmedianreccen_list_get, name='pmedianreccen_list_get'),
    url('pmedianreccen/download', pmedianrecyclingcenterviews.pmedianreccen_download_get,name='pmedianreccen_create_get'),
    url('pmedianreccen/create', pmedianrecyclingcenterviews.pmedianreccen_create_post,
        name='pmedianreccen_create_post'),
    url('pmedianreccen/update', pmedianrecyclingcenterviews.pmedianreccen_update_post,
        name='pmedianreccen_update_post'),
    url('pmedianreccen/delete', pmedianrecyclingcenterviews.pmedianreccen_delete_post,
        name='pmedianreccen_delete_post'),
    url('pmedianreccen/upload', pmedianrecyclingcenterviews.pmedianreccen_upload_post,
        name='pmedianreccen_upload_post'),
    url('pmedianreccen/clear', pmedianrecyclingcenterviews.pmedianreccen_clear_post, name='pmedianreccen_clear_post'),

    url('pmediants/list', pmediantransferstationviews.pmediants_list_get, name='pmediants_list_get'),
    url('pmediants/download', pmediantransferstationviews.pmediants_download_get, name='pmediants_create_get'),
    url('pmediants/create', pmediantransferstationviews.pmediants_create_post, name='pmediants_create_post'),
    url('pmediants/update', pmediantransferstationviews.pmediants_update_post, name='pmediants_update_post'),
    url('pmediants/delete', pmediantransferstationviews.pmediants_delete_post, name='pmediants_delete_post'),
    url('pmediants/upload', pmediantransferstationviews.pmediants_upload_post, name='pmediants_upload_post'),
    url('pmediants/clear', pmediantransferstationviews.pmediants_clear_post, name='pmediants_clear_post'),


]
