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
    url('addcityeconomy', views.addEconomyCity, name='addEconomyCity'),
    url('addcitypopulation', views.addPopulationCity, name='addPopulationCity'),
    url('geteconomycity', views.geteconomydata_city, name='geteconomycity'),
    url('getpopulationcity', views.getpopulation_city, name='getpopulationcity'),
    url('amendcityeconomydata', views.amendeconomydata_city, name='amendcityeconomydata'),
    url('deletecityeconomydata', views.deleteeconomydata_city, name='deletecityeconomydata'),
    url('addsinglerowdata', views.addsinglerow_cityeconomy, name=''),
    url('addbatchgarbagecity', views.addbatchgarbagedata_city, name=''),
    url('getgarbagecity', views.getgarbagepropduction_city)
]