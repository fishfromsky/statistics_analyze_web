from django.conf.urls import url
from . import views

urlpatterns = [
    url('login', views.login, name='login'),
    url('info', views.getInfo, name='getInfo'),
    url('logout', views.logout, name='logout'),
    url('addmodel', views.addModel, name='addModel'),
    url('getmodel', views.getModel, name='getModel'),
    url('fetchmodel', views.fetchModel, name='fetchModel'),
    url('getsuperuser', views.fetchsuperuser, name='fetchSuperuser'),
    url('fetchsuperuser', views.filtersuperuser, name='filtersuperuser'),
    url('amendmodel', views.amendmodel, name='amendmodel'),
    url('deletemodel', views.deletemodel, name='deletemodel'),
    url('addsuperuser', views.addsuperuser, name='addsuperuser'),
    url('deletesuperuser', views.deletesuperuser, name='deleteSuperuser'),
    url('getfactorylist', views.getFacorty, name='getFactory'),
    url('getfactorybyid', views.getFactoryById, name='getFactoryById'),
    url('add_city', views.addCity, name='addCity'),  # 批量导入城市
    url('adddistrict', views.addDistrict, name='addDistrict'),  # 批量导入区
    url('addtown', views.addTown, name='addTown'),  # 批量导入城镇
    url('addbatchgarbagecity', views.addbatchgarbagedata_city, name='addbatchgarbagedata_city'),  # 批量导入生活垃圾数据
    url('addcitygarbagedeal', views.addGarbageDealCity, name='addGarbageDeal'),  # 批量导入无害化处理厂数据
    url('addcitygarbagecapacity', views.addGarbageDealCapacityCity, name='addGarbageDealCapacityCity'),  # 批量导入无害化处理能力数据
    url('addcitygarbagevolume', views.addGarbageDealVolumeCity, name='addGarbageDealVolumeCity'),  # 批量导入无害化处理量数据
    url('addcityeconomy', views.addEconomyCity, name='addEconomyCity'),  # 批量导入城市经济信息
    url('addcitypopulation', views.addPopulationCity, name='addPopulationCity'),  # 批量导入城市人口信息
    url('geteconomycity', views.geteconomydata_city, name='geteconomycity'),  # 请求城市经济表
    url('getpopulationcity', views.getpopulation_city, name='getpopulationcity'),  # 请求城市人口表
    url('getgarbagecity', views.getgarbage_city, name='getgarbageinfo'),  # 请求城市生活垃圾表
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
    url('addbasic', views.add_basic, name='addbasic'),  # 添加p_median项目basic表
    url('addts', views.add_ts, name='addts'),  # 添加p_median项目ts表
    url('addrrc', views.add_rrc, name='addrrc'),  # 添加p_median项目rrc表
    url('addcostmatrix', views.add_cost_matrix, name='addcostmatrix'),  # 添加p_median项目cost_matrix表
    url('getpmedianproject', views.getpmedianproject, name='getpmedianproject'),  # 请求p_median项目
    url('amendpmedianproject', views.amendpmedianproject, name='amendpmedianproject'),  # 修改p_median项目
    url('getplotlocation', views.getlocation, name='getlocation'),  # 集散厂位置优化
    url('getnationwaterpollution', views.get_water_pollution, name='getwaterpollution'),  # 爬取国内水体污染数据
    url('getnationpm', views.get_nation_pm, name='getnationpm'),  # 爬取国内空气污染数据
    url('getnationsolidpollution', views.get_nation_solid_pollution, name='getnationsolidpollution'),  # 爬取国内固废垃圾数据
    url('getworldpm', views.get_world_pm, name='getworldpm')  # 爬取世界空气污染数据


]
