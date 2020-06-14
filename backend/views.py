from .models import UserProfile, ModelsList, FactoryList, Economy_Info_City, City, Population_Info_City, Garbage_Info_City,District,Town,Gargabe_Deal_City,Gargage_Deal_Capacity_City,Garbage_Deal_Volume_City

from django.http import JsonResponse
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ManyToManyField
import json
from rest_framework.authtoken.models import Token
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.core import serializers


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


@csrf_exempt
@require_http_methods(['GET'])
def getFacorty(request):
    response = {}
    response['data'] = []
    factorylist = FactoryList.objects.all()
    for factory in factorylist:
        response['data'].append(to_dict(factory))
    response['code'] = 20000
    response['message'] = 'success'
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def getFactoryById(request):
    response = {'code': 20000, 'message': 'success'}
    id = request.GET.get('id')
    response['data'] = []
    factory = FactoryList.objects.get(id=id)
    response['data'].append(to_dict(factory))
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
            response['message'] = "表头和数据不一致或者缺少数据！"
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
            response['message'] = "表头和数据不一致或缺少数据！"
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
            response['message'] = '表头和数据不一致或缺少数据'
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
            response['message'] = '表头和数据不一致或者缺少数据!'
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
            response['message'] = '表头和数据不一致或者缺少数据!'
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
            response['message'] = '表头和数据不一致或者缺少数据!'
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
            response['message'] = '表头和数据不一致或者缺少数据!'
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
            response['message'] = '表头与数据不一致或者缺少数据！'
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
            response['message'] = '表头与数据不一致或者缺少数据！'
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
    id = body.get('id')
    data = Population_Info_City.objects.get(id=id)
    data.year = body.get('year')
    data.population = body.get('population')
    data.population_density = body.get('population_density')
    data.population_rate = body.get('population_rate')
    data.households = body.get('households')
    data.average_per_person_household = body.get('average_person_per_household')
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
        response['message'] = '该年份数据已存在，请先删除'
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




@csrf_exempt
@require_http_methods(['GET'])
def getgarbagepropduction_city(request):
    response = {'code': 20000, 'message': 'success'}
    result = Garbage_Info_City.objects.all()
    response['data'] = []
    for list in result:
        response['data'].append(to_dict(list))
    return JsonResponse(response, safe=False)