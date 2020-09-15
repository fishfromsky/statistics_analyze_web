from .models import UserProfile, ModelsList, FactoryList, Economy_Info_City, City, Population_Info_City,\
    Garbage_Info_City,District,Town,Gargabe_Deal_City,Gargage_Deal_Capacity_City,Garbage_Deal_Volume_City,\
    p_median_project, basic, ts, rrc, cost_matrix, TransferFactoryList, CollectFactoryList, Crawl_Data_Record, \
    lstm_project, lstm_parameter, lstm_result, multi_regression_project, multi_regression_parameter, \
    multi_regression_result, kmeans_project, kmeans_result, kmeans_parameter, algorithm_project

from django.http import JsonResponse
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ManyToManyField
import json
import pandas as pd
from rest_framework.authtoken.models import Token
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import os
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
import threading


def to_dict(self, fields=None, exclude=None):
    data = {}
    for f in self._meta.concrete_fields + self._meta.many_to_many:
        value = f.value_from_object(self)

        if fields and f.name not in fields:
            continue

        if exclude and f.name in exclude:
            continue

        if isinstance(f, ManyToManyField):
            value = [i.id for i in value] if self.pk else None

        if isinstance(f, DateTimeField):
            value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None

        data[f.name] = value

    return data


@csrf_exempt
def login(request):
    response = {'status': 1, 'message': 'login failed!'}
    if request.method != 'POST':
        response['message'] = 'please use post method'
        return JsonResponse(response, safe=False)
    user_info = json.loads(request.body)
    username = user_info.get('username')
    password = user_info.get('password')
    if not username:
        response['message'] = 'please input your username'
        return JsonResponse(response, safe=False)
    if not password:
        response['message'] = 'please input your password'
        return JsonResponse(response, safe=False)
    user_count = UserProfile.objects.filter(username=username, password=password).count()
    if user_count == 0:
        response['message'] = '用户名或者密码错误'
        response['code'] = 20001
        return JsonResponse(response)
    else:
        user = UserProfile.objects.get(username=username, password=password)
        if Token.objects.filter(user=user):
            Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        user.token = str(token.key)
        user.save()
        data = {
            'username': user.username,
            'token': str(token.key),
            'roles': [user.role],
            'id': user.id
        }
        response['data'] = data
        response['status'] = 0
        response['message'] = 'success'
        response['code'] = 20000
        return JsonResponse(response)


@csrf_exempt
def getInfo(request):
    if request.method == 'GET':
        response = {'status': 0, 'message': 'success'}
        token = request.GET.get('token')
        user = Token.objects.filter(key=token)
        if user:
            user_id = user.first().user_id
            user_info = UserProfile.objects.filter(id=user_id).first()
            data = {
                'username': user_info.username,
                'roles': [user_info.role],
                'token': token,
                'id': user_info.id
            }
            response['data'] = data
            response['code'] = 20000
            return JsonResponse(response, safe=False)
        else:
            response['code'] = 20001
            response['status'] = 1
            response['res'] = '没有该用户'
            response['message'] = '登录超时，请重新登录'
            return JsonResponse(response, safe=False)
    else:
        response = {'status': '0', 'res': '只能使用get请求'}
        return JsonResponse(response, safe=False)


@csrf_exempt
def logout(request):
    response = {"status": 0}
    token = request.GET.get('token')
    if request.method == 'GET':
        response['res'] = "只能使用POST方法"
        response['status'] = 1
        return JsonResponse(response, safe=False)
    if Token.objects.filter(key=token).count():
        Token.objects.filter(key=token).delete()
        response['code'] = 20000
        return JsonResponse(response, safe=False)
    response['status'] = 1
    response['res'] = "请先登录"
    return JsonResponse(response, safe=False)


# 添加模型
@csrf_exempt
@require_http_methods(['GET'])
def addModel(request):
    response = {}
    modelname = request.GET.get('name')
    author = request.GET.get('author')
    star = request.GET.get('star')
    ModelsList.objects.create(modelname=modelname, author=author, star=star)
    response['code'] = 20000
    response['message'] = 'success'
    return JsonResponse(response, safe=False)


# 获取模型列表
@csrf_exempt
@require_http_methods(['GET'])
def getModel(request):
    response = {}
    modellist = ModelsList.objects.all()
    response['data'] = []
    for model in modellist:
        response['data'].append(to_dict(model))
    response['code'] = 20000
    response['message'] = 'success'
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def fetchModel(request):
    title = request.GET.get('title')
    star = request.GET.get('star')
    response = {'code': 20000, 'data':[]}
    if title is None and star is None:
        modellist = ModelsList.objects.all()
        for model in modellist:
            response['data'].append(to_dict(model))
        return JsonResponse(response, safe=False)
    elif star is None and title is not None:
        modellist = ModelsList.objects.filter(modelname__contains=title)
        for model in modellist:
            response['data'].append(to_dict(model))
        return JsonResponse(response, safe=False)
    elif star is not None and title is None:
        modellist = ModelsList.objects.filter(star=star)
        for model in modellist:
            response['data'].append(to_dict(model))
        return JsonResponse(response, safe=False)
    else:
        modellist = ModelsList.objects.filter(Q(modelname__contains=title) & Q(star=star))
        for model in modellist:
            response['data'].append(to_dict(model))
        return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def fetchsuperuser(request):
    response = {'code': 20000, 'data': []}
    superusers = UserProfile.objects.filter(role='超级管理员')
    for user in superusers:
        response['data'].append(to_dict(user))
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def filtersuperuser(request):
    response = {'code': 20000, 'data': []}
    name = request.GET.get('name')
    if name is None:
        superusers = UserProfile.objects.filter(role='超级管理员')
        for user in superusers:
            response['data'].append(to_dict(user))
        return JsonResponse(response, safe=False)
    else:
        superusers = UserProfile.objects.filter(username__contains=name)
        for user in superusers:
            response['data'].append(to_dict(user))
        return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def addsuperuser(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    name = body.get('name')
    password = body.get('password')
    email = body.get('email')
    phone = body.get('phone')
    UserProfile.objects.create(username=name, password=password, phone_number=phone, email=email, role='超级管理员')
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def amendmodel(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    name = body.get('name')
    author = body.get('author')
    star = body.get('star')
    if name != '':
        model = ModelsList.objects.get(id=id)
        model.modelname = name
        model.save()
    if author != '':
        model = ModelsList.objects.get(id=id)
        model.author = author
        model.save()
    if star != 0:
        model = ModelsList.objects.get(id=id)
        model.star = star
        model.save()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def deletemodel(request):
    response = {'code': 20000, 'message': 'success'}
    id = request.GET.get('id')
    print(id)
    if ModelsList.objects.filter(id=id).count() == 0:
        response['code'] = 50000
        response['message'] = '不存在该模型'
        return JsonResponse(response, safe=False)
    else:
        model = ModelsList.objects.get(id=id)
        model.delete()
        return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def deletesuperuser(request):
    response = {'code': 20000, 'message': 'success'}
    id = request.GET.get('id')
    if UserProfile.objects.filter(id=id).count() == 0:
        response['code'] = 50000
        response['message'] = '不存在该账号'
        return JsonResponse(response, safe=False)
    else:
        user = UserProfile.objects.get(id=id)
        user.delete()
        return JsonResponse(response, safe=False)


# 批量导入城市表
@csrf_exempt
@require_http_methods(['POST'])
def addCity(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    data = body.get('data')
    for i in range(len(data)):
        if data[i].__contains__('name'):
            name = data[i]['name']
            list = City.objects.create(name=name)
            list.save()
        else:
            response['code'] = 50000
            response['message'] = "表头和数据表不一致或者缺少数据！"
            break
    return JsonResponse(response,safe = False)

# 批量导入区表
@csrf_exempt
@require_http_methods(['POST'])
def addDistrict(request):
    response = {'code': 20000, 'message': 'success'}
    city_id = 1
    body = json.loads(request.body)
    data = body.get('data')
    for i in range(len(data)):
        if data[i].__contains__('name'):
            name = data[i]['name']
            list = District.objects.create(name=name, city_name=City(id=city_id))
            list.save()
        else:
            response['code'] = 50000
            response['message'] = "表头和数据表不一致或缺少数据！"
            break
    return JsonResponse(response, safe=False)

# 批量导入城镇表
@csrf_exempt
@require_http_methods(['POST'])
def addTown(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    data = body.get('data')
    for i in range(len(data)):
        if data[i].__contains__('name') and data[i].__contains__('district_name'):
            name = data[i]['name']
            district_name = data[i]['district_name']
            list = Town.objects.create(name=name, district_name=District(id=district_name))
            list.save()
        else:
            response['code'] = 50000
            response['message'] = '表头和数据表不一致或缺少数据'
            break
    return JsonResponse(response, safe=False)


# 批量导入城市经济表
@csrf_exempt
@require_http_methods(['POST'])
def addEconomyCity(request):
    response = {'code': 20000, 'message': 'success'}
    city_id = 1
    body = json.loads(request.body)
    data = body.get('data')
    for i in range(len(data)):
        if data[i].__contains__('year') and data[i].__contains__('gdp') and data[i].__contains__('gdp_per_capita') and data[i].__contains__('gdp_growth_rate') and data[i].__contains__('unemployment_rate'):
            if Economy_Info_City.objects.filter(year=data[i]['year']).count() != 0:
                response['code'] = 50000
                response['message'] = '该年份数据已存在，请先删除'
            else:
                year = data[i]['year']
                gdp = data[i]['gdp']
                gdp_per_capita = data[i]['gdp_per_capita']
                gdp_growth_rate = data[i]['gdp_growth_rate']
                unemployment_rate = data[i]['unemployment_rate']
                list = Economy_Info_City.objects.create(
                    city=City(id=city_id), year=year, gdp=gdp, gdp_per_capita=gdp_per_capita, gdp_growth_rate=gdp_growth_rate,
                    unemployment_rate=unemployment_rate)
                list.save()
        else:
            response['code'] = 50000
            response['message'] = '表头和数据表不一致或者缺少数据!'
            break
    return JsonResponse(response, safe=False)


# 批量导入城市人口表
@csrf_exempt
@require_http_methods(['POST'])
def addPopulationCity(request):
    response = {'code': 20000, 'message': 'success'}
    city_id = 1
    body = json.loads(request.body)
    data = body.get('data')
    for i in range(len(data)):
        if data[i].__contains__('year') and data[i].__contains__('population') and data[i].__contains__('population_density') and data[i].__contains__('population_rate') and data[i].__contains__('households') and data[i].__contains__('average_person_per_household'):
            if Population_Info_City.objects.filter(year=data[i]['year']).count() != 0:
                response['code'] = 50000
                response['message'] = '该年份数据已存在，请先删除'
            else:
                year = data[i]['year']
                population = data[i]['population']
                population_density = data[i]['population_density']
                population_rate = data[i]['population_rate']
                households = data[i]['households']
                average_person_per_household = data[i]['average_person_per_household']
                list = Population_Info_City.objects.create(city=City(id=city_id), year=year, population=population, population_density=population_density,
                                        population_rate=population_rate, households=households, average_person_per_household=average_person_per_household)
                list.save()
        else:
            response['code'] = 50000
            response['message'] = '表头和数据表不一致或者缺少数据!'
            break
    return JsonResponse(response, safe=False)

# 批量导入全市生活垃圾表
@csrf_exempt
@require_http_methods(['POST'])
def addbatchgarbagedata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    city_id = 1
    data = body.get('data')
    for i in range(len(data)):
        if data[i].__contains__('year') and data[i].__contains__('total_garbage') and data[i].__contains__('collect_transport_garbage') and data[i].__contains__('volume_of_treated'):
            year = data[i]['year']
            total_garbage = data[i]['total_garbage']
            collect_transport_garbage = data[i]['collect_transport_garbage']
            volume_of_treated = data[i]['volume_of_treated']
            if Garbage_Info_City.objects.filter(year=year).count() != 0:
                response['code'] = 50000
                response['message'] = '该年份数据已存在，请先删除'
                break
            else:
                list = Garbage_Info_City.objects.create(city=City(id=city_id), year=year, total_garbage=total_garbage,
                                                        collect_transport_garbage=collect_transport_garbage, volume_of_treated=volume_of_treated)
                list.save()
        else:
            response['code'] = 50000
            response['message'] = '表头和数据表不一致或者缺少数据!'
    return JsonResponse(response, safe=False)

# 批量导入全市无害化处理厂表
@csrf_exempt
@require_http_methods(['POST'])
def addGarbageDealCity(request):
    response = {'code':20000,'message':'success'}
    city_id = 1
    body = json.loads(request.body)
    data = body.get('data')
    for i in range(len(data)):
        if data[i].__contains__('year') and data[i].__contains__('factory_num_total') and data[i].__contains__('landFill') and data[i].__contains__('incineration') and data[i].__contains__('compost') and data[i].__contains__('else_num'):
            if Gargabe_Deal_City.objects.filter(year=data[i]['year']).count() != 0:
                response['code'] = 50000
                response['message'] = '该年份数据已存在，请先删除'
            else:
                year = data[i]['year']
                factory_num_total = data[i]['factory_num_total']
                landFill = data[i]['landFill']
                incineration = data[i]['incineration']
                compost = data[i]['compost']
                else_num = data[i]['else_num']
                list = Gargabe_Deal_City.objects.create(city=City(id=city_id), year=year, factory_num_total=factory_num_total, landFill=landFill,
                                                    incineration=incineration, compost=compost, else_num=else_num)
                list.save()
        else:
            response['code'] = 50000
            response['message'] = '表头和数据表不一致或者缺少数据!'
            break
    return JsonResponse(response, safe = False)

# 批量导入全市无害化处能力表
@csrf_exempt
@require_http_methods(['POST'])
def addGarbageDealCapacityCity(request):
    response = {'code': 20000, 'message': 'success'}
    city_id = 1
    body = json.loads(request.body)
    data = body.get('data')
    for i in range(len(data)):
        if data[i].__contains__('year') and data[i].__contains__('deal_num_total') and data[i].__contains__('landfill') and data[i].__contains__('incineration') and data[i].__contains__('compost') and data[i].__contains__('else_num'):
            if Gargage_Deal_Capacity_City.objects.filter(year=data[i]['year']).count() != 0:
                response['code'] = 50000
                response['message'] = '该年份数据已存在，请先删除'
            else:
                year = data[i]['year']
                deal_num_total = data[i]['deal_num_total']
                landfill = data[i]['landfill']
                incineration = data[i]['incineration']
                compost = data[i]['compost']
                else_num = data[i]['else_num']
                list = Gargage_Deal_Capacity_City.objects.create(city=City(id=city_id), year=year, deal_num_total=deal_num_total, landfill=landfill, incineration=incineration, compost=compost, else_num=else_num)
                list.save()
        else:
            response['code'] = 50000
            response['message'] = '表头与数据表不一致或者缺少数据！'
            break
    return JsonResponse(response, safe=False)

# 批量导入全市无害化处理量表
@csrf_exempt
@require_http_methods(['POST'])
def addGarbageDealVolumeCity(request):
    response = {'code': 20000, 'message': 'success'}
    city_id = 1
    body = json.loads(request.body)
    data = body.get('data')
    for i in range(len(data)):
        if data[i].__contains__('year') and data[i].__contains__('deal_volume_total') and data[i].__contains__('landfill') and data[i].__contains__('incineration') and data[i].__contains__('compost') and data[i].__contains__('else_num'):
            if Garbage_Deal_Volume_City.objects.filter(year=data[i]['year']).count() != 0:
                response['code'] = 50000
                response['message'] = '该年份数据已存在，请先删除'
            else:
                year = data[i]['year']
                deal_volume_total = data[i]['deal_volume_total']
                landfill = data[i]['landfill']
                incineration = data[i]['incineration']
                compost = data[i]['compost']
                else_num = data[i]['else_num']
                list = Garbage_Deal_Volume_City.objects.create(city=City(id=city_id), year=year, deal_volume_total=deal_volume_total, landfill=landfill, incineration=incineration, compost=compost, else_num=else_num)
                list.save()
        else:
            response['code'] = 50000
            response['message'] = '表头与数据表不一致或者缺少数据！'
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def addFactoryListCity(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    data = body.get('data')
    for i in range(len(data)):
        if data[i].__contains__('name') and data[i].__contains__('district') and data[i].__contains__('company') and data[i].__contains__('address') and data[i].__contains__('type') and data[i].__contains__('typeId') and data[i].__contains__('longitude') and data[i].__contains__('latitude') and data[i].__contains__('deal'):
            name = data[i]['name']
            district = data[i]['district']
            company = data[i]['company']
            address = data[i]['address']
            type = data[i]['type']
            typeId = data[i]['typeId']
            longitude = data[i]['longitude']
            latitude = data[i]['latitude']
            deal = data[i]['deal']
            list = FactoryList(name=name, district=district, address=address, company=company, type=type, typeId=typeId, longitude=longitude, latitude=latitude, deal=deal)
            list.save()
        else:
            response['code'] = 50000
            response['message'] = '表头与数据表不一致或缺少数据'
    return JsonResponse(response, safe=False)


# 批量导入垃圾中转站信息
@csrf_exempt
@require_http_methods(['POST'])
def addTransferFactory(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    data = body.get('data')
    for i in range(len(data)):
        if data[i].__contains__('district') and data[i].__contains__('name') and data[i].__contains__('address') and data[i].__contains__('longitude') and data[i].__contains__('latitude') and data[i].__contains__('capacity'):
            district = data[i]['district']
            name = data[i]['name']
            address = data[i]['address']
            longitude = data[i]['longitude']
            latitude = data[i]['latitude']
            capacity = data[i]['capacity']
            list = TransferFactoryList(district=district, name=name, address=address, longitude=longitude, latitude=latitude, capacity=capacity)
            list.save()
        else:
            response['code'] = 50000
            response['message'] = '表头与数据表不一致或者缺少数据'

    return JsonResponse(response, safe=False)


# 获取垃圾中转站信息
@csrf_exempt
@require_http_methods(['GET'])
def getTransferFactory(request):
    response = {'code': 20000, 'message': 'success'}
    data = TransferFactoryList.objects.all()
    response['data'] = []
    for list in data:
        response['data'].append(to_dict(list))

    return JsonResponse(response, safe=False)

# 修改中转站信息表
@csrf_exempt
@require_http_methods(['POST'])
def AmendTransferFactory(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    name = body.get('name')
    id = body.get('id')
    address = body.get('address')
    longitude = body.get('longitude')
    latitude = body.get('latitude')
    capacity = body.get('capacity')
    district = body.get('district')
    record = TransferFactoryList.objects.get(id=id)
    record.name = name
    record.address = address
    record.longitude = longitude
    record.latitude = latitude
    record.capacity = capacity
    record.district = district
    record.save()
    return JsonResponse(response, safe=False)

# 删除中转站信息
@csrf_exempt
@require_http_methods(['POST'])
def DeleteTransferFactory(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    record = TransferFactoryList.objects.get(id=id)
    record.delete()
    return JsonResponse(response, safe=False)


# 添加中转站信息
@csrf_exempt
@require_http_methods(['POST'])
def addtransferbyrow(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    print(body)
    name = body.get('name')
    address = body.get('address')
    longitude = body.get('longitude')
    latitude = body.get('latitude')
    capacity = body.get('capacity')
    district = body.get('district')
    record = TransferFactoryList(name=name, address=address, longitude=longitude, latitude=latitude, capacity=capacity, district=district)
    record.save()
    return JsonResponse(response, safe=False)


# 请求无害化处理厂信息
@csrf_exempt
@require_http_methods(['GET'])
def getfacotylist(request):
    response = {'code': 20000, 'message': 'success'}
    data = FactoryList.objects.all()
    response['data'] = []
    for list in data:
        response['data'].append(to_dict(list))

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def addfactorylistbyrow(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    name = body.get('name')
    address = body.get('address')
    longitude = body.get('longitude')
    latitude = body.get('latitude')
    deal = body.get('deal')
    type = body.get('type')
    typeId = body.get('typeId')
    company = body.get('company')
    district = body.get('district')
    record = FactoryList(name=name, address=address, longitude=longitude, latitude=latitude, deal=deal, type=type, typeId=typeId, company=company, district=district)
    record.save()
    return JsonResponse(response, safe=False)


# 删除指定无害化处理厂信息
@csrf_exempt
@require_http_methods(['POST'])
def deletefactorylist(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    record = FactoryList.objects.get(id=id)
    record.delete()
    return JsonResponse(response, safe=False)


# 修改无害化处理信息表
@csrf_exempt
@require_http_methods(['POST'])
def amendfactorylist(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    name = body.get('name')
    address = body.get('address')
    longitude = body.get('longitude')
    latitude = body.get('latitude')
    deal = body.get('deal')
    type = body.get('type')
    typeId = body.get('typeId')
    company = body.get('company')
    district = body.get('district')
    record = FactoryList.objects.get(id=id)
    record.name = name
    record.address = address
    record.longitude = longitude
    record.latitude = latitude
    record.deal = deal
    record.type = type
    record.typeId = typeId
    record.company = company
    record.district = district
    record.save()
    return JsonResponse(response, safe=False)


# 批量导入垃收集点信息
@csrf_exempt
@require_http_methods(['POST'])
def AddCollectFactory(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    data = body.get('data')
    for i in range(len(data)):
        if data[i].__contains__('district') and data[i].__contains__('address') and data[i].__contains__('longitude') and data[i].__contains__('latitude'):
            district = data[i]['district']
            address = data[i]['address']
            longitude = data[i]['longitude']
            latitude = data[i]['latitude']
            list = CollectFactoryList(district=district, address=address, longitude=longitude, latitude=latitude)
            list.save()
        else:
            response['code'] = 50000
            response['message'] = '表头与数据表不一致或者缺少数据'

    return JsonResponse(response, safe=False)


# 根据区域获取指定区域内收集点信息
@csrf_exempt
@require_http_methods(['GET'])
def GetCollectFactoryByArea(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    district = request.GET.get('district')
    factory_list = CollectFactoryList.objects.filter(district=district)
    for list in factory_list:
        response['data'].append(to_dict(list))

    return JsonResponse(response, safe=False)


# 请求城市经济表数据
@csrf_exempt
@require_http_methods(['GET'])
def geteconomydata_city(request):
    response = {'code': 20000, 'message': 'success'}
    data = Economy_Info_City.objects.all()
    response['data'] = []
    for list in data:
        response['data'].append(to_dict(list))
    return JsonResponse(response, safe=False)

# 请求城市人口表数据
@csrf_exempt
@require_http_methods(['GET'])
def getpopulation_city(request):
    response = {'code': 20000, 'message': 'success'}
    data = Population_Info_City.objects.all()
    response['data'] = []
    for list in data:
        response['data'].append(to_dict(list))
    return JsonResponse(response, safe=False)

# 请求城市生活垃圾表数据
@csrf_exempt
@require_http_methods(['GET'])
def getgarbage_city(request):
    response = {'code': 20000, 'message': 'success'}
    data = Garbage_Info_City.objects.all()
    response['data'] = []
    for list in data:
        response['data'].append(to_dict(list))
    return JsonResponse(response, safe=False)

# 请求城市无害化处理厂表数据
@csrf_exempt
@require_http_methods(['GET'])
def getgarbagedeal_city(request):
    response = {'code': 20000, 'message': 'success'}
    data = Gargabe_Deal_City.objects.all()
    response['data'] = []
    for list in data:
        response['data'].append(to_dict(list))
    return JsonResponse(response, safe=False)

# 请求城市无害化处理能力表数据
@csrf_exempt
@require_http_methods(['GET'])
def getgarbagecapacity_city(request):
    response = {'code': 20000, 'message': 'success'}
    data = Gargage_Deal_Capacity_City.objects.all()
    response['data'] = []
    for list in data:
        response['data'].append(to_dict(list))
    return JsonResponse(response, safe=False)

# 请求城市无害化处理量表数据
@csrf_exempt
@require_http_methods(['GET'])
def getgarbagevolume_city(request):
    response = {'code': 20000, 'message': 'success'}
    data = Garbage_Deal_Volume_City.objects.all()
    response['data'] = []
    for list in data:
        response['data'].append(to_dict(list))
    return JsonResponse(response, safe=False)



# 请求p_median项目
@csrf_exempt
@require_http_methods(['GET'])
def getpmedianproject(request):
    response = {'code': 20000, 'message': 'success'}
    data = p_median_project.objects.all()
    response['data'] = []
    for list in data:
        response['data'].append(to_dict(list))
    return JsonResponse(response, safe=False)

# 修改p_median项目
@csrf_exempt
@require_http_methods(['POST'])
def amendpmedianproject(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    print(body)
    project_id = body.get('project_id')
    data = p_median_project.objects.get(project_id=project_id)
    data.project_id = body.get('project_id')
    data.name = body.get('name')
    data.basic_size = body.get('basic_size')
    data.ts_size = body.get('ts_size')
    data.rrc_size = body.get('rrc_size')
    data.cost_matrix_size = body.get('cost_matrix_size')
    data.save()
    return JsonResponse(response, safe=False)

# 修改经济表数据
@csrf_exempt
@require_http_methods(['POST'])
def amendeconomydata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    year = body.get('year')
    gdp = body.get('gdp')
    gdp_per_capita = body.get('gdp_per_capita')
    gdp_growth_rate = body.get('gdp_growth_rate')
    unemployment_rate = body.get('unemployment_rate')
    data = Economy_Info_City.objects.get(id=id)
    data.year = year
    data.gdp = gdp
    data.gdp_per_capita = gdp_per_capita
    data.gdp_growth_rate = gdp_growth_rate
    data.unemployment_rate = unemployment_rate
    data.save()
    return JsonResponse(response, safe=False)

# 删除经济表数据
@csrf_exempt
@ require_http_methods(['POST'])
def deleteeconomydata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    data = Economy_Info_City.objects.get(id=id)
    data.delete()
    return JsonResponse(response, safe=False)

# 修改人口表数据
@csrf_exempt
@require_http_methods(['POST'])
def amendpopulationdata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    print(body)
    id = body.get('id')
    data = Population_Info_City.objects.get(id=id)
    data.year = body.get('year')
    data.population = body.get('population')
    data.population_density = body.get('population_density')
    data.population_rate = body.get('population_rate')
    data.households = body.get('households')
    data.average_person_per_household = body.get('average_person_per_household')
    data.save()
    return JsonResponse(response, safe=False)

# 删除人口表数据
@csrf_exempt
@require_http_methods(['POST'])
def deletepopulationdata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    data = Population_Info_City.objects.get(id=id)
    data.delete()
    return JsonResponse(response, safe=False)

# 修改生活垃圾表数据
@csrf_exempt
@require_http_methods(['POST'])
def amendgarbagedata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    data = Garbage_Info_City.objects.get(id=id)
    data.year = body.get('year')
    data.total_garbage = body.get('total_garbage')
    data.collect_transport_garbage = body.get('collect_transport_garbage')
    data.volume_of_treated = body.get('volume_of_treated')
    data.save()
    return JsonResponse(response, safe=False)

# 删除生活垃圾表数据
@csrf_exempt
@require_http_methods(['POST'])
def deletegarbagedata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    data = Garbage_Info_City.objects.get(id=id)
    data.delete()
    return JsonResponse(response, safe=False)

# 修改无害化处理厂表数据
@csrf_exempt
@require_http_methods(['POST'])
def amendgarbagedealdata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    data = Gargabe_Deal_City.objects.get(id=id)
    data.year = body.get('year')
    data.factory_num_total = body.get('factory_num_total')
    data.landFill = body.get('landFill')
    data.incineration = body.get('incineration')
    data.compost = body.get('compost')
    data.else_num = body.get('else_num')
    data.save()
    return JsonResponse(response, safe=False)

# 删除无害化处理厂表数据
@csrf_exempt
@require_http_methods(['POST'])
def deletegarbagedealdata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    data = Gargabe_Deal_City.objects.get(id=id)
    data.delete()
    return JsonResponse(response, safe=False)

# 修改无害化处理能力表数据
@csrf_exempt
@require_http_methods(['POST'])
def amendgarbagecapacitydata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    data = Gargage_Deal_Capacity_City.objects.get(id=id)
    data.year = body.get('year')
    data.deal_num_total = body.get('deal_num_total')
    data.landfill = body.get('landfill')
    data.incineration = body.get('incineration')
    data.compost = body.get('compost')
    data.else_num = body.get('else_num')
    data.save()
    return JsonResponse(response, safe=False)

# 删除无害化处理能力表数据
@csrf_exempt
@require_http_methods(['POST'])
def deletegarbagecapacitydata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    data = Gargage_Deal_Capacity_City.objects.get(id=id)
    data.delete()
    return JsonResponse(response, safe=False)

# 修改无害化处理量表数据
@csrf_exempt
@require_http_methods(['POST'])
def amendgarbagevolumedata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    data = Garbage_Deal_Volume_City.objects.get(id=id)
    data.year = body.get('year')
    data.deal_volume_total = body.get('deal_volume_total')
    data.landfill = body.get('landfill')
    data.incineration = body.get('incineration')
    data.compost = body.get('compost')
    data.else_num = body.get('else_num')
    data.save()
    return JsonResponse(response, safe=False)

# 删除无害化处理量表数据
@csrf_exempt
@require_http_methods(['POST'])
def deletegarbagevolumedata_city(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('id')
    data = Garbage_Deal_Volume_City.objects.get(id=id)
    data.delete()
    return JsonResponse(response, safe=False)


# 添加一条经济表数据
@csrf_exempt
@require_http_methods(['POST'])
def addsinglerow_cityeconomy(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    city_id = 1
    year = body.get('year')
    gdp = body.get('gdp')
    gdp_per_capita = body.get('gdp_per_capita')
    gdp_growth_rate = body.get('gdp_growth_rate')
    unemployment_rate = body.get('unemployment_rate')
    if Economy_Info_City.objects.filter(year=year).count() != 0:
        response['code'] = 50000
        response['message'] = '该年份数据已存在，请先删除'
    else:
        data = Economy_Info_City.objects.create(city=City(id=city_id),  year=year, gdp=gdp, gdp_per_capita=gdp_per_capita, gdp_growth_rate=gdp_growth_rate, unemployment_rate=unemployment_rate)
        data.save()
    return JsonResponse(response, safe=False)

# 添加一条人口表数据
@csrf_exempt
@require_http_methods(['POST'])
def addsinglepopulation(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    city_id = 1
    year = body.get('year')
    population = body.get('population')
    population_density = body.get("population_density")
    population_rate = body.get("population_rate")
    households = body.get("households")
    average_person_per_household = body.get("average_person_per_household")
    if Population_Info_City.objects.filter(year=year).count() != 0:
        response['code'] = 50000
        response['message'] = '该年份数据已存在，请先删除'
    else:
        data = Population_Info_City.objects.create(city=City(id=city_id), year=year, population=population, population_density=population_density,
                                                   population_rate=population_rate, households=households, average_person_per_household=average_person_per_household)
        data.save()
    return JsonResponse(response, safe=False)

# 添加一条生活垃圾表数据
@csrf_exempt
@require_http_methods(['POST'])
def addsinglegarbageinfocity(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    city_id = 1
    year = body.get('year')
    total_garbage = body.get('total_garbage')
    collect_transport_garbage = body.get('collect_transport_garbage')
    volume_of_treated = body.get('volume_of_treated')
    if Garbage_Info_City.objects.filter(year=year).count() != 0:
        response['code'] = 50000
        response['message'] = '该年份数据已存在，请先删除！'
    else:
        data = Garbage_Info_City.objects.create(city=City(id=city_id), year=year, total_garbage=total_garbage, collect_transport_garbage=collect_transport_garbage, volume_of_treated=volume_of_treated)
        data.save()
    return JsonResponse(response, safe=False)


# 添加一条无害化处理厂表数据
@csrf_exempt
@require_http_methods(['POST'])
def addsinglegarbagedealcity(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    city_id = 1
    year = body.get('year')
    factory_num_total = body.get('factory_num_total')
    landFill = body.get('landFill')
    incineration = body.get('incineration')
    compost = body.get('compost')
    else_num = body.get('else_num')
    if Gargabe_Deal_City.objects.filter(year=year).count() != 0:
        response['code'] = 50000
        response['message'] = '该年份数据已存在，请先删除'
    else:
        data = Gargabe_Deal_City.objects.create(city=City(id=city_id), year=year, factory_num_total=factory_num_total, landFill=landFill, incineration=incineration, compost=compost, else_num=else_num)
        data.save()
    return JsonResponse(response, safe=False)

# 添加一条无害化处理能力表数据
@csrf_exempt
@require_http_methods(['POST'])
def addsinglegarbagedealcapacity(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    city_id = 1
    year = body.get('year')
    deal_num_total = body.get('deal_num_total')
    landfill = body.get('landfill')
    incineration = body.get('incineration')
    compost = body.get('compost')
    else_num = body.get('else_num')
    if Gargage_Deal_Capacity_City.objects.filter(year=year).count() != 0:
        response['code'] = 50000
        response['message'] = '该年份数据已存在，请先删除'
    else:
        data = Gargage_Deal_Capacity_City.objects.create(city=City(id=city_id), year=year, deal_num_total=deal_num_total, landfill=landfill, incineration=incineration, compost=compost, else_num=else_num)
        data.save()
    return JsonResponse(response, safe=False)

# 添加一条无害化处理量表数据
@csrf_exempt
@require_http_methods(['POST'])
def addsinglegarbagedealvolume(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    city_id = 1
    year = body.get('year')
    deal_volume_total = body.get('deal_volume_total')
    landfill = body.get('landfill')
    incineration = body.get('incineration')
    compost = body.get('compost')
    else_num = body.get('else_num')
    if Garbage_Deal_Volume_City.objects.filter(year=year).count() != 0:
        response['code'] = 50000
        response['message'] = '该年份数据已存在，请先删除'
    else:
        data = Garbage_Deal_Volume_City.objects.create(city=City(id=city_id), year=year, deal_volume_total=deal_volume_total, landfill=landfill, incineration=incineration, compost=compost, else_num=else_num)
        data.save()
    return JsonResponse(response, safe=False)


# 添加一个p_median项目
@csrf_exempt
@require_http_methods(['POST'])
def add_p_median_project(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    project_id = body.get('project_id')
    name = body.get('name')
    if p_median_project.objects.filter(project_id=project_id).count() != 0:
        response['code'] = 50000
        response['message'] = '该项目已存在，请先删除！'
    else:
        data = p_median_project.objects.create(name=name, basic_size=0, ts_size=0, rrc_size=0, cost_matrix_size=0, project_id=project_id)
        data.save()
    return JsonResponse(response, safe=False)

# 启动集散厂优化模型
@csrf_exempt
@require_http_methods(['POST'])
def start_p_median_project(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    project_id = body.get('project_id')
    project = p_median_project.objects.get(project_id=project_id)
    if project.basic_size != 0 and project.ts_size != 0 and project.rrc_size != 0:
        project.project_state = '正在运行'
        project.save()
        os.system('python backend/p-median-new/main.py' + ' ' + str(project_id))
    else:
        response['code'] = 5000
        response['message'] = '请先导入相关表格'
    project.project_state = '已运行'
    project.save()
    return JsonResponse(response, safe=False)

# 爬取国内水体污染实时数据
@csrf_exempt
@require_http_methods(['POST'])
def get_water_pollution(request):
    response = {'code': 20000, 'message': 'success'}
    os.system('python backend/start_crawl.py ' + 'nation_water')
    date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    path = os.path.join("static/国内水体污染数据/" + date + '国内水体污染实时数据.xlsx')
    os.renames("static/国内水体污染数据/国内水体污染实时数据.xlsx", path)
    response['excel_url'] = 'http://127.0.0.1:8000/' + path
    table_type = '国内水体污染数据'
    dateTime = str(date)
    hour = dateTime[8:10]
    minute = dateTime[10:12]
    second = dateTime[12:]
    time = hour + ':' + minute + ':' + second
    key_words = '-'
    file_location = path
    data = Crawl_Data_Record.objects.create(table_type=table_type, time=time, key_words=key_words, file_location=file_location)
    data.save()
    return JsonResponse(response, safe=False)


# 爬取国内空气污染实时数据
@csrf_exempt
@require_http_methods(['POST'])
def get_nation_pm(request):
    response = {'code': 20000, 'message': 'success'}
    os.system('python backend/start_crawl.py ' + 'nation_pm')
    date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    path = os.path.join("static/国内空气污染数据/" + date + '国内空气污染实时数据.xlsx')
    os.renames("static/国内空气污染数据/国内空气污染实时数据.xlsx", path)
    response['excel_url'] = 'http://127.0.0.1:8000/' + path
    table_type = '国内空气污染数据'
    dateTime = str(date)
    hour = dateTime[8:10]
    minute = dateTime[10:12]
    second = dateTime[12:]
    time = hour + ':' + minute + ':' + second
    key_words = '-'
    city = '-'
    file_location = path
    data = Crawl_Data_Record.objects.create(table_type=table_type, time=time, key_words=key_words, city=city,
                                            file_location=file_location)
    data.save()
    return JsonResponse(response, safe=False)

# 爬取国内固体废弃物数据
@csrf_exempt
@require_http_methods(['POST'])
def get_nation_solid_pollution(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    key_word = body.get('key_word')
    count = body.get('count')
    startYear = int(body.get('startYear')[0:4])+1
    endYear = int(body.get('endYear')[0:4])+1
    district = body.get('district')
    date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    os.system('python backend/start_crawl.py ' + 'nation_solid_pollution ' + count + " " + key_word + " " + district + " " + str(startYear) + " " + str(endYear))
    path = os.path.join("static/国内固体废物数据/" + date + '国内固体废物实时数据.xlsx')
    os.renames("static/国内固体废物数据/国内固体废物实时数据.xlsx", path)
    response['excel_url'] = 'http://127.0.0.1:8000/' + path
    table_type = '国内固体废物数据'
    dateTime = str(date)
    hour = dateTime[8:10]
    minute = dateTime[10:12]
    second = dateTime[12:]
    time = hour + ':' + minute + ':' + second
    key_words = key_word
    file_location = path
    city = district
    data = Crawl_Data_Record.objects.create(table_type=table_type, time=time, key_words=key_words, city=city,
                                            file_location=file_location)
    data.save()
    return JsonResponse(response, safe=False)


# 爬取世界空气污染数据
@csrf_exempt
@require_http_methods(['POST'])
def get_world_pm(request):
    response = {'code': 20000, 'message': 'success'}
    date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    os.system('python backend/start_crawl.py ' + 'world_pm')
    path = os.path.join("static/世界空气污染数据/" + date + '世界空气污染实时数据.xlsx')
    os.renames("static/世界空气污染实时数据.xlsx", path)
    response['excel_url'] = 'http://127.0.0.1:8000/' + path
    table_type = '世界空气污染数据'
    dateTime = str(date)

    hour = dateTime[8:10]
    minute = dateTime[10:12]
    second = dateTime[12:]
    time = hour + ':' + minute + ':' + second
    key_words = '-'
    city = '-'
    file_location = path
    data = Crawl_Data_Record.objects.create(table_type=table_type, time=time, key_words=key_words, city=city,
                                            file_location=file_location)
    data.save()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def getgarbagepropduction_city(request):
    response = {'code': 20000, 'message': 'success'}
    result = Garbage_Info_City.objects.all()
    response['data'] = []
    for list in result:
        response['data'].append(to_dict(list))
    return JsonResponse(response, safe=False)

# 获取历史爬虫数据
@csrf_exempt
@require_http_methods(['GET'])
def get_crawl_record(request):
    response = {'code': 20000, 'message': 'success', 'data': [], 'unique_year_list': [], 'unique_kw_list': [], 'unique_city_list':[]}
    table_type = request.GET.get('type')
    data = Crawl_Data_Record.objects.filter(table_type=table_type)
    for item in data:
        dic = {'id': '', 'date': '', 'time': '', 'table_type': '', 'key_words': '', 'file_location': '', 'city': ''}
        dic['id'] = to_dict(item)['id']
        dic['date'] = to_dict(item)['date']
        dic['time'] = to_dict(item)['time']
        dic['table_type'] = to_dict(item)['table_type']
        dic['key_words'] = to_dict(item)['key_words']
        dic['city'] = to_dict(item)['city']
        dic['file_location'] = 'http://127.0.0.1:8000/' + to_dict(item)['file_location']
        response['data'].append(dic)
    year_list = [str(i.date)[0:4] for i in data]
    unique_year_list = list(set(year_list))
    response['unique_year_list'] = unique_year_list

    kw_list = [i.key_words for i in data]
    unique_kw_list = list(set(kw_list))
    response['unique_kw_list'] = unique_kw_list

    city_list = [i.city for i in data]
    unique_city_list = list(set(city_list))
    response['unique_city_list'] = unique_city_list
    return JsonResponse(response, safe=False)

# 筛选爬虫历史数据
@csrf_exempt
@require_http_methods(['GET'])
def get_crawl_record_select(request):
    response = {'code': 20000, 'message': 'success', 'data': [], 'unique_year_list': [], 'unique_kw_list': [], 'unique_city_list':[]}
    table_type = request.GET.get('table_type')
    year = request.GET.get('year')
    key_words = request.GET.get('key_words')
    city = request.GET.get('city')

    obj = Crawl_Data_Record.objects.all()

    if table_type != None and table_type != '':
        obj = obj.filter(table_type=table_type)
    if year != None and year != '':
        obj = obj.filter(date__year=year)
    if table_type == '国内固体废物数据':
        obj = obj.filter(key_words=str(key_words))
        obj = obj.filter(city=str(city))
    year_list = [str(i.date)[0:4] for i in obj]
    unique_year_list = list(set(year_list))
    response['unique_year_list'] = unique_year_list

    kw_list = [i.key_words for i in obj]
    unique_kw_list = list(set(kw_list))
    response['unique_kw_list'] = unique_kw_list

    city_list = [i.city for i in obj]
    unique_city_list = list(set(city_list))
    response['unique_city_list'] = unique_city_list

    for item in obj:
        dic = {'id': '', 'date': '', 'time': '', 'table_type': '', 'key_words': '', 'file_location': '', 'city': ''}
        dic['id'] = to_dict(item)['id']
        dic['date'] = to_dict(item)['date']
        dic['time'] = to_dict(item)['time']
        dic['table_type'] = to_dict(item)['table_type']
        dic['key_words'] = to_dict(item)['key_words']
        dic['city'] = to_dict(item)['city']
        dic['file_location'] = 'http://127.0.0.1:8000/' + to_dict(item)['file_location']
        response['data'].append(dic)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def delete_crawl_data(request):
    response = {'code': 20000, 'message': 'success'}
    id = request.GET.get('id')
    data = Crawl_Data_Record.objects.get(id=id)
    print(data.file_location)
    os.remove(data.file_location)
    data.delete()
    return JsonResponse(response, safe=False)

# 获取lstm项目
@csrf_exempt
@require_http_methods(['GET'])
def get_lstm_project(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    data = lstm_project.objects.all()
    for item in data:
        response['data'].append(to_dict(item))
    return JsonResponse(response, safe=False)


# 添加lstm项目
@csrf_exempt
@require_http_methods(['POST'])
def add_lstm_project(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    project_id = body.get('project_id')
    name = body.get('name')
    if lstm_project.objects.filter(project_id=project_id).count() != 0:
        response['code'] = 50000
        response['message'] = '已存在该项目编号'
    else:
        data = lstm_project.objects.create(project_id=project_id, name=name, table_size=0, status='未运行')
        data.save()
    return JsonResponse(response, safe=False)


def crawl_water_pollution_data():
    os.system('python backend/start_crawl.py ' + 'nation_water')
    date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    path = os.path.join("static/国内水体污染数据/" + date + '国内水体污染实时数据.xlsx')
    os.renames("static/国内水体污染数据/国内水体污染实时数据.xlsx", path)
    table_type = '国内水体污染数据'
    dateTime = str(date)
    hour = dateTime[8:10]
    minute = dateTime[10:12]
    second = dateTime[12:]
    time = hour + ':' + minute + ':' + second
    key_words = '-'
    file_location = path
    city = '-'
    data = Crawl_Data_Record.objects.create(table_type=table_type, time=time, key_words=key_words, city=city,
                                            file_location=file_location)
    data.save()


def crawl_nation_air_pllution_data():
    os.system('python backend/start_crawl.py ' + 'nation_pm')
    date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    path = os.path.join("static/国内空气污染数据/" + date + '国内空气污染实时数据.xlsx')
    os.renames("static/国内空气污染数据/国内空气污染实时数据.xlsx", path)
    table_type = '国内空气污染数据'
    dateTime = str(date)
    hour = dateTime[8:10]
    minute = dateTime[10:12]
    second = dateTime[12:]
    time = hour + ':' + minute + ':' + second
    key_words = '-'
    file_location = path
    city = '-'
    data = Crawl_Data_Record.objects.create(table_type=table_type, time=time, key_words=key_words, city=city,
                                            file_location=file_location)
    data.save()


@csrf_exempt
@require_http_methods(['GET'])
def lstm_project_id(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    data = lstm_project.objects.values('project_id').all()
    for item in data:
        response['data'].append(item)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def get_parameter_lstm(request):
    id = request.GET.get('project_id')
    response = {'code': 20000, 'message': 'success', 'data': []}
    data = lstm_parameter.objects.filter(project_id=lstm_project(project_id=id))
    for item in data:
        response['data'].append(to_dict(item))
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def input_lstm_parameter(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    data = body.get('data')
    id = body.get('project_id')
    if lstm_parameter.objects.filter(project_id=lstm_project(project_id=id)).count() != 0:
        response['code'] = 50000
        response['message'] = '数据库中存在该项目的参数，请先删除'
    else:
        for i in range(len(data)):
            if data[i].__contains__('year') and data[i].__contains__('population') and data[i].__contains__('population_density')  and data[i].__contains__('total_households') \
                    and data[i].__contains__('average_person_per_household') and data[i].__contains__('gdp') \
                    and data[i].__contains__('per_capita_gdp') and data[i].__contains__('residential_garbage'):
                if lstm_parameter.objects.filter(year=data[i]['year'], project_id=lstm_project(project_id=id)).count() != 0:
                    response['code'] = 50000
                    response['message'] = '存在重复年份数据，请先删除该数据'
                else:
                    parameter = lstm_parameter.objects.create(project_id=lstm_project(project_id=id), year=data[i]['year'],
                                                              population=data[i]['population'],
                                                              population_density=data[i]['population_density'],
                                                              total_households=data[i]['total_households'],
                                                              average_person_per_household=data[i][
                                                                  'average_person_per_household'], gdp=data[i]['gdp'],
                                                              per_capita_gdp=data[i]['per_capita_gdp'],
                                                              residential_garbage=data[i]['residential_garbage'])
                    parameter.save()
            else:
                response['code'] = 50000
                response['message'] = '表头与数据不一致或者缺少数据'

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def amend_lstm_project(request):
    response = {'message': 'success', 'code': 20000}
    body = json.loads(request.body)
    project_id = body.get('project_id')
    name = body.get('name')
    model = lstm_project.objects.get(project_id=project_id)
    model.name = name
    model.save()
    return JsonResponse(response, safe=False)


def lstm_thread(id):
    os.system('python backend/LSTM/predict_garbage.py %s' % id)


@csrf_exempt
@require_http_methods(['POST'])
def experiment_lstm_start(request):
    response = {'message': 'success', 'code': 20000}
    body = json.loads(request.body)
    id = body.get('project_id')
    if lstm_parameter.objects.filter(project_id=lstm_project(project_id=id)).count() == 0:
        response['code'] = 50000
        response['message'] = '该项目缺少数据，无法实验'
    else:
        model = lstm_project.objects.get(project_id=id)
        model.status = '正在运行'
        model.save()
        task = threading.Thread(target=lstm_thread, args=(id,))
        task.start()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def experiment_lstm_finish(request):
    response = {'message': 'success', 'code': 20000}
    body = json.loads(request.body)
    id = body.get('project_id')
    model = lstm_project.objects.get(project_id=id)
    model.status = '未运行'
    model.save()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def save_lstm_result(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('project_id')
    data = body.get('data')
    if lstm_result.objects.filter(project_id=lstm_project(project_id=id)).count() != 0:
        last_sort = lstm_result.objects.filter(project_id=lstm_project(project_id=id)).order_by('-id')[:1]
        sort = last_sort.get().sort + 1
    else:
        sort = 1
    for i in range(len(data)):
        year = data[i]['year']
        pred = data[i]['pred']
        real = data[i]['real']
        model = lstm_result.objects.create(project_id=lstm_project(project_id=id), year=year, real=real, pred=pred, sort=sort)
        model.save()

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def get_lstm_result(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    id = request.GET.get('project_id')
    data = lstm_result.objects.filter(project_id=lstm_project(project_id=id))
    for item in data:
        response['data'].append(to_dict(item))

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def get_regression_programe(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    data = multi_regression_project.objects.all()
    for item in data:
        response['data'].append(to_dict(item))

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def add_regression_programe(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    project_id = body.get('project_id')
    name = body.get('name')
    if multi_regression_project.objects.filter(project_id=project_id).count() != 0:
        response['code'] = 50000
        response['message'] = '已存在该编号的项目'
    else:
        model = multi_regression_project.objects.create(project_id=project_id, name=name)
        model.save()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def amend_regression_programe(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    project_id = body.get('project_id')
    name = body.get('name')
    model = multi_regression_project.objects.get(project_id=project_id)
    model.name = name
    model.save()

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def add_regression_parameter(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('project_id')
    data = body.get('data')
    if multi_regression_parameter.objects.filter(project_id=multi_regression_project(project_id=id)).count() != 0:
        response['code'] = 50000
        response['message'] = '数据库中存在该项目参数，请先删除'
    else:
        for i in range(len(data)):
            if data[i].__contains__('resident_population') and data[i].__contains__('population_of_density') and \
                data[i].__contains__('number_of_households') and data[i].__contains__('average_population_per_household') \
                and data[i].__contains__('urban_residents_per_capita_disposable_income') and data[i].__conains__('consumer_expenditure') \
                and data[i].__contains__('general_public_expenditure') and data[i].__contains__('investment_in_urban_infrastructure') \
                and data[i].__contains__('urban_population_density') and data[i].__contains__('greening_coverage') and \
                data[i].__contains__('gross_local_product') and data[i].__contains__('gross_domestic_product_per_capita') \
                and data[i].__contains__('gross_domestic_product_of_the_first_industry') and data[i].__contains__('gross_value_of_secondary_industry') \
                and data[i].__contains__('gross_value_of_the_tertiary_industry') and data[i].__contains__('investment_in_environmental_protection') \
                and data[i].__contains__('number_of_college_students') and data[i].__contains__('level_of_education') and \
                data[i].__contains__('municial_household_garbage'):
                model = multi_regression_parameter.objects.create(project_id=multi_regression_project(project_id=id),
                                                                  resident_population=data[i]['resident_population'],
                                                                  population_of_density=data[i]['population_of_density'],
                                                                  number_of_households=data[i]['number_of_households'],
                                                                  average_population_per_household=data[i]['average_population_per_household'],
                                                                  urban_residents_per_capita_disposable_income=data[i]['urban_residents_per_capita_disposable_income'],
                                                                  consumer_expenditure=data[i]['consumer_expenditure'],
                                                                  general_public_expenditure=data[i]['general_public_expenditure'],
                                                                  investment_in_urban_infrastructure=data[i]['investment_in_urban_infrastructure'],
                                                                  urban_population_density=data[i]['urban_population_density'],
                                                                  greening_coverage=data[i]['greening_coverage'],
                                                                  gross_local_product=data[i]['gross_local_product'],
                                                                  gross_domestic_product_per_capita=data[i]['gross_domestic_product_per_capita'],
                                                                  gross_domestic_product_of_the_first_industry=data[i]['gross_domestic_product_of_the_first_industry'],
                                                                  gross_value_of_secondary_industry=data[i]['gross_value_of_secondary_industry'],
                                                                  gross_value_of_the_tertiary_industry=data[i]['gross_value_of_the_tertiary_industry'],
                                                                  investment_in_environmental_protection=data[i]['investment_in_environmental_protection'],
                                                                  number_of_college_students=data[i]['number_of_college_students'],
                                                                  level_of_education=data[i]['level_of_education'],
                                                                  municial_household_garbage=data[i]['municial_household_garbage'])
                model.save()
            else:
                response['code'] = 50000
                response['message'] = '表头与数据不一致或者缺少数据'

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def regression_idlist(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    data = multi_regression_project.objects.values('project_id').all()
    for item in data:
        response['data'].append(item)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def parameter_regression(request):
    id = request.GET.get('project_id')
    response = {'code': 20000, 'message': 'success', 'data': []}
    data = multi_regression_parameter.objects.filter(project_id=multi_regression_project(project_id=id))
    for item in data:
        response['data'].append(to_dict(item))
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def save_regression_result(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('project_id')
    data = body.get('data')
    if multi_regression_result.objects.filter(project_id=multi_regression_project(project_id=id)).count() != 0:
        last_sort = multi_regression_result.objects.filter(project_id=multi_regression_project(project_id=id)).order_by('-id')[:1]
        sort = last_sort.get().sort + 1
    else:
        sort = 1
    for i in range(len(data)):
        pred = data[i]['pred']
        real = data[i]['real']
        model = multi_regression_result.objects.create(project_id=multi_regression_project(project_id=id),
                                                       real=real, pred=pred, sort=sort)
        model.save()

    return JsonResponse(response, safe=False)


def thread_regression(id):
    os.system('python backend/multi_regression/newpredict.py %s' % id)


@csrf_exempt
@require_http_methods(['POST'])
def start_regression_experiment(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('project_id')
    if multi_regression_parameter.objects.filter(project_id=multi_regression_project(project_id=id)).count() == 0:
        response['code'] = 50000
        response['message'] = '该项目缺少数据，无法实验'
    else:
        model = multi_regression_project.objects.get(project_id=id)
        model.status = '正在运行'
        model.save()
        task = threading.Thread(target=thread_regression, args=(id,))
        task.start()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def finish_regression_experiment(request):
    response = {'message': 'success', 'code': 20000}
    body = json.loads(request.body)
    id = body.get('project_id')
    model = multi_regression_project.objects.get(project_id=id)
    model.status = '未运行'
    model.save()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def get_regression_result(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    id = request.GET.get('project_id')
    data = multi_regression_result.objects.filter(project_id=multi_regression_project(project_id=id))
    for item in data:
        response['data'].append(to_dict(item))

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def add_kmeans_project(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    project_id = body.get('project_id')
    name = body.get('name')
    if kmeans_project.objects.filter(project_id=project_id).count() != 0:
        response['code'] = 50000
        response['message'] = '已存在该编号的项目'
    else:
        model = kmeans_project.objects.create(project_id=project_id, name=name)
        model.save()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def get_kmeans_project(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    data = kmeans_project.objects.all()
    for item in data:
        response['data'].append(to_dict(item))
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def amend_kmeans_project(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    project_id = body.get('project_id')
    name = body.get('name')
    model = kmeans_project.objects.get(project_id=project_id)
    model.name = name
    model.save()

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def save_result_kmeans(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('project_id')
    data = body.get('data')
    if kmeans_result.objects.filter(project_id=kmeans_project(project_id=id)).count() != 0:
        last_sort = kmeans_result.objects.filter(project_id=kmeans_project(project_id=id)).order_by(
            '-id')[:1]
        sort = last_sort.get().sort + 1
    else:
        sort = 1
    for i in range(len(data)):
        xaxis = data[i]['xaxis']
        yaxis = data[i]['yaxis']
        label = data[i]['label']
        model = kmeans_result.objects.create(project_id=kmeans_project(project_id=id),
                                             xaxis=xaxis, yaxis=yaxis, label=label, sort=sort)
        model.save()

    return JsonResponse(response, safe=False)


def thread_kmeans(id):
    os.system('python backend/KMeans/kmeans.py %s' % id)


@csrf_exempt
@require_http_methods(['POST'])
def start_kmeans(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('project_id')
    if kmeans_parameter.objects.filter(project_id=kmeans_project(project_id=id)).count() == 0:
        response['code'] = 50000
        response['message'] = '该项目缺少数据无法实验，请先补充数据'
    else:
        model = kmeans_project.objects.get(project_id=id)
        model.status = '正在运行'
        model.save()
        task = threading.Thread(target=thread_kmeans, args=(id,))
        task.start()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def stop_kmeans(request):
    response = {'message': 'success', 'code': 20000}
    body = json.loads(request.body)
    id = body.get('project_id')
    model = kmeans_project.objects.get(project_id=id)
    model.status = '未运行'
    model.save()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def get_result_kmeans(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    id = request.GET.get('project_id')
    data = kmeans_result.objects.filter(project_id=kmeans_project(project_id=id))
    for item in data:
        response['data'].append(to_dict(item))

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def get_idlist_kmeans(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    data = kmeans_project.objects.values('project_id').all()
    for item in data:
        response['data'].append(item)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def input_parameter_kmeans(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('project_id')
    data = body.get('data')
    if kmeans_parameter.objects.filter(project_id=kmeans_project(project_id=id)).count() != 0:
        response['code'] = 50000
        response['message'] = '数据库中存在该项目参数，请先删除'
    else:
        for i in range(len(data)):
            if data[i].__contains__('resident_population') and data[i].__contains__('population_of_density') and \
                    data[i].__contains__('number_of_households') and data[i].__contains__(
                'average_population_per_household') \
                    and data[i].__contains__('urban_residents_per_capita_disposable_income') and data[i].__conains__(
                'consumer_expenditure') \
                    and data[i].__contains__('general_public_expenditure') and data[i].__contains__(
                'investment_in_urban_infrastructure') \
                    and data[i].__contains__('urban_population_density') and data[i].__contains__(
                'greening_coverage') and \
                    data[i].__contains__('gross_local_product') and data[i].__contains__(
                'gross_domestic_product_per_capita') \
                    and data[i].__contains__('gross_domestic_product_of_the_first_industry') and data[i].__contains__(
                'gross_value_of_secondary_industry') \
                    and data[i].__contains__('gross_value_of_the_tertiary_industry') and data[i].__contains__(
                'investment_in_environmental_protection') \
                    and data[i].__contains__('number_of_college_students') and data[i].__contains__(
                'level_of_education') and \
                    data[i].__contains__('municial_household_garbage'):
                model = kmeans_parameter.objects.create(project_id=kmeans_project(project_id=id),
                                                        resident_population=data[i]['resident_population'],
                                                        population_of_density=data[i]['population_of_density'],
                                                        number_of_households=data[i]['number_of_households'],
                                                        average_population_per_household=data[i][
                                                              'average_population_per_household'],
                                                        urban_residents_per_capita_disposable_income=data[i][
                                                              'urban_residents_per_capita_disposable_income'],
                                                        consumer_expenditure=data[i]['consumer_expenditure'],
                                                        general_public_expenditure=data[i][
                                                              'general_public_expenditure'],
                                                        investment_in_urban_infrastructure=data[i][
                                                              'investment_in_urban_infrastructure'],
                                                        urban_population_density=data[i][
                                                              'urban_population_density'],
                                                        greening_coverage=data[i]['greening_coverage'],
                                                        gross_local_product=data[i]['gross_local_product'],
                                                        gross_domestic_product_per_capita=data[i][
                                                              'gross_domestic_product_per_capita'],
                                                        gross_domestic_product_of_the_first_industry=data[i][
                                                              'gross_domestic_product_of_the_first_industry'],
                                                        gross_value_of_secondary_industry=data[i][
                                                              'gross_value_of_secondary_industry'],
                                                        gross_value_of_the_tertiary_industry=data[i][
                                                              'gross_value_of_the_tertiary_industry'],
                                                        investment_in_environmental_protection=data[i][
                                                              'investment_in_environmental_protection'],
                                                        number_of_college_students=data[i][
                                                              'number_of_college_students'],
                                                        level_of_education=data[i]['level_of_education'],
                                                        municial_household_garbage=data[i][
                                                              'municial_household_garbage'])
                model.save()
            else:
                response['code'] = 50000
                response['message'] = '表头与数据不一致或者缺少数据'

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def get_parameter_kmeans(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    data = kmeans_parameter.objects.all()
    for item in data:
        response['data'].append(to_dict(item))

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def get_algorithm_list(request):
    response = {'code': 20000, 'message': 'success', 'data': []}
    data = algorithm_project.objects.all()
    for item in data:
        response['data'].append(to_dict(item))

    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def add_algorithm_list(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('project_id')
    name = body.get('name')
    describe = body.get('describe')
    if algorithm_project.objects.filter(project_id=id).count() != 0:
        response['code'] = 50000
        response['message'] = '已存在该编号的项目'
    else:
        model = algorithm_project.objects.create(project_id=id, name=name, describe=describe)
        model.save()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def delete_algorithm_list(request):
    response = {'code': 20000, 'message': 'success'}
    body = json.loads(request.body)
    id = body.get('project_id')
    item = algorithm_project.objects.get(project_id=id)
    item.delete()

    return JsonResponse(response, safe=False)


scheduler = BackgroundScheduler()
scheduler.add_job(crawl_water_pollution_data, 'cron', day_of_week='mon-sun', hour='11', minute='27', second='40')
scheduler.add_job(crawl_nation_air_pllution_data, 'cron', day_of_week='mon-sun', hour='10', minute='10', second='10')
scheduler.start()



