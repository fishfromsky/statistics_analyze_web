import urllib.parse as parse
from backend.modelview import PmedianRecyclingCenter
from django.http import JsonResponse
from backend.models import p_median_project
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ManyToManyField
import json
# from rest_framework.authtoken.models import Token
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage


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


########################################################################## PmedianRecyclingCenter 开始##################################
@csrf_exempt
@require_http_methods(['GET'])
def pmedianreccen_list_get(request):
    response = {'code': 20000, 'message': 'success'}

    ### 筛选的字段
    project_id = request.GET.get('project_id')
    district = request.GET.get('district')
    location = request.GET.get('location')

    sort = request.GET.get('sort')
    page = request.GET.get('page')
    limit = request.GET.get('limit')

    pmedianreccen_obj = PmedianRecyclingCenter.objects.all()
    project_id_list = [i.project_id for i in pmedianreccen_obj]
    unique_project_id = list(set(project_id_list))
    district_list = [i.district for i in pmedianreccen_obj]
    unique_district = list(set(district_list))

    # 筛选
    if project_id != None and project_id != '':
        pmedianreccen_obj = pmedianreccen_obj.filter(project_id=project_id)
    if district != None and district != '':
        pmedianreccen_obj = pmedianreccen_obj.filter(district=district)
    if location != None and location != '':
        pmedianreccen_obj = pmedianreccen_obj.filter(location=location)

    if sort == '-id':
        pmedianreccen_obj = pmedianreccen_obj.order_by("-id")

    # 分页
    paginator = Paginator(pmedianreccen_obj, limit)  # 分页
    pmedianreccen_obj_page = paginator.get_page(page)

    # 生成response，参考mockjs的内容
    pmedianreccen_list = [to_dict(i) for i in pmedianreccen_obj_page]
    keys = ['total', 'items', 'unique_project_id', 'unique_district']
    values = [pmedianreccen_obj.count(), pmedianreccen_list, unique_project_id, unique_district]
    data_dict = dict(zip(keys, values))
    response['data'] = data_dict
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmedianreccen_update_post(request):
    response = {'code': 20000, 'message': 'success'}
    post_info = json.loads(request.body)
    post_id = post_info.get('id')
    PmedianRecyclingCenter.objects.filter(id=post_id).update(**post_info)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmedianreccen_create_post(request):
    response = {'code': 20000, 'message': 'success'}
    post_info = json.loads(request.body)
    print(post_info)
    PmedianRecyclingCenter.objects.create(**post_info)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmedianreccen_delete_post(request):
    response = {'code': 20000, 'message': 'success'}
    post_id = json.loads(request.body)
    project_id = PmedianRecyclingCenter.objects.get(id=post_id).project_id
    project = p_median_project.objects.get(project_id=project_id)
    project.rrc_size = project.rrc_size - 1
    project.save()
    PmedianRecyclingCenter.objects.filter(id=post_id).delete()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def pmedianreccen_download_get(request):
    response = {'code': 20000, 'message': 'success'}
    project_id = request.GET.get('project_id')
    district = request.GET.get('district')
    location = request.GET.get('location')

    sort = request.GET.get('sort')
    pmedianreccen_obj = PmedianRecyclingCenter.objects.all()
    # 筛选
    if project_id != None and project_id != '':
        pmedianreccen_obj = pmedianreccen_obj.filter(project_id=project_id)
    if district != None and district != '':
        pmedianreccen_obj = pmedianreccen_obj.filter(district=district)
    if location != None and location != '':
        pmedianreccen_obj = pmedianreccen_obj.filter(location=location)

    if sort == '-id':
        pmedianreccen_obj = pmedianreccen_obj.order_by("-id")

    pmedianreccen_list = [to_dict(i) for i in pmedianreccen_obj]
    keys = ['items']
    values = [pmedianreccen_list]
    data_dict = dict(zip(keys, values))
    response['data'] = data_dict
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmedianreccen_upload_post(request):
    response = {'code': 20000, 'message': 'success'}
    data = json.loads(request.body)
    if data[0].__contains__('项目编号'):
        if p_median_project.objects.filter(project_id=data[0]['项目编号']).count() == 0:
            response['code'] = 50000
            response['message'] = '请先创建项目！'
        else:
            project = p_median_project.objects.get(project_id=data[0]['项目编号'])
            if project.ts_size != 0:
                response['code'] = 50000
                response['message'] = '该项目此表数据已存在！'
            else:
                for i in range(len(data)):
                    if data[i].__contains__('项目编号') and data[i].__contains__('区') and data[
                        i].__contains__('街镇') and data[i].__contains__('位置') and data[i].__contains__(
                        '经度') and data[i].__contains__('纬度') and data[i].__contains__('处理量') and data[i].__contains__('单位') and data[i].__contains__('已选择'):
                        project_id = data[i]['项目编号']
                        district = data[i]['区']
                        sub_district = data[i]['街镇']
                        location = data[i]['位置']
                        lng = data[i]['经度']
                        lat = data[i]['纬度']
                        max_load = data['处理量']
                        max_load_unit = data['单位']
                        has_selected = data[i]['已选择']
                        list = PmedianRecyclingCenter.objects.create(project_id=project_id,
                                                                     district=district,
                                                                     sub_district=sub_district,
                                                                     location=location,
                                                                     lng=lng,
                                                                     lat=lat,
                                                                     max_load=max_load,
                                                                     max_load_unit=max_load_unit,
                                                                     has_selected=has_selected
                                                              )
                        list.save()
                        project.ts_size = len(data)
                        project.save()
                    else:
                        response['code'] = 50000
                        response['message'] = '表头与数据不一致或者缺少数据！'
    else:
        response['code'] = 50000
        response['message'] = '表头与数据不一致或者缺少数据！'
    return JsonResponse(response, safe=False)




@csrf_exempt
@require_http_methods(['POST'])
def pmedianreccen_clear_post(request):
    response = {'code': 20000, 'message': 'success'}
    post = request.get_full_path().split('?')[1]

    q_list = post.split('&')
    keys = []
    values = []
    for q in q_list:
        keys.append(q.split('=')[0])
        values.append(parse.unquote(q.split('=')[1]))
    q_dict = dict(zip(keys, values))
    print(q_dict)

    project_id = q_dict.get('project_id')
    print(project_id, '........data')
    district = q_dict.get('district')
    print(district, '........data')
    location = q_dict.get('location')
    print(location, '........data')

    pmedianreccen_obj = PmedianRecyclingCenter.objects.all()

    ### 筛选
    if project_id != None and project_id != '':
        print(project_id, 'clear_post..................project_id')
        pmedianreccen_obj = pmedianreccen_obj.filter(project_id=project_id)
    if district != None and district != '':
        print(district, 'clear_post..................district')
        pmedianreccen_obj = pmedianreccen_obj.filter(district=district)
    if location != None and location != '':
        print(location, 'clear_post..................location')
        pmedianreccen_obj = pmedianreccen_obj.filter(location=location)
    projects = p_median_project.objects.all()
    for i in projects:
        i.rrc_size = 0
        i.save()
    pmedianreccen_obj.delete()

    return JsonResponse(response, safe=False)