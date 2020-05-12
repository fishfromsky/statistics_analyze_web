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
    url('addcitypopulation', views.addPopulationCity, name='addPopulationCity')
]