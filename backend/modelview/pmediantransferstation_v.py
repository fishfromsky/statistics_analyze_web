import urllib.parse as parse
from backend.modelview import PmedianTransferStation
from backend.models import p_median_project
from django.http import JsonResponse
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


########################################################################## PmedianTransferStation 开始##################################
@csrf_exempt
@require_http_methods(['GET'])
def pmediants_list_get(request):
    response = {'code': 20000, 'message': 'success'}

    ### 筛选的字段
    project_id = request.GET.get('project_id')
    sub_names = request.GET.get('sub_names')

    sort = request.GET.get('sort')
    page = request.GET.get('page')
    limit = request.GET.get('limit')

    pmediants_obj = PmedianTransferStation.objects.all()
    project_id_list = [i.project_id for i in pmediants_obj]
    unique_project_id = list(set(project_id_list))

    # 筛选
    if project_id != None and project_id != '':
        pmediants_obj = pmediants_obj.filter(project_id=project_id)
    if sub_names != None and sub_names != '':
        pmediants_obj = pmediants_obj.filter(sub_names=sub_names)

    if sort == '-id':
        pmediants_obj = pmediants_obj.order_by("-id")

    # 分页
    paginator = Paginator(pmediants_obj, limit)  # 分页
    pmediants_obj_page = paginator.get_page(page)

    # 生成response，参考mockjs的内容
    pmediants_list = [to_dict(i) for i in pmediants_obj_page]
    keys = ['total', 'items', 'unique_project_id']
    values = [pmediants_obj.count(), pmediants_list, unique_project_id]
    data_dict = dict(zip(keys, values))
    response['data'] = data_dict
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmediants_update_post(request):
    response = {'code': 20000, 'message': 'success'}
    post_info = json.loads(request.body)
    post_id = post_info.get('id')
    PmedianTransferStation.objects.filter(id=post_id).update(**post_info)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmediants_create_post(request):
    response = {'code': 20000, 'message': 'success'}
    post_info = json.loads(request.body)
    print(post_info)
    PmedianTransferStation.objects.create(**post_info)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmediants_delete_post(request):
    response = {'code': 20000, 'message': 'success'}
    post_id = json.loads(request.body)
    project_id = PmedianTransferStation.objects.get(id=post_id).project_id
    project = p_median_project.objects.get(project_id=project_id)
    project.basic_size = project.basic_size - 1
    project.save()
    PmedianTransferStation.objects.filter(id=post_id).delete()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def pmediants_download_get(request):
    response = {'code': 20000, 'message': 'success'}
    project_id = request.GET.get('project_id')
    sub_names = request.GET.get('sub_names')

    sort = request.GET.get('sort')
    pmediants_obj = PmedianTransferStation.objects.all()
    # 筛选
    if project_id != None and project_id != '':
        pmediants_obj = pmediants_obj.filter(project_id=project_id)
    if sub_names != None and sub_names != '':
        pmediants_obj = pmediants_obj.filter(sub_names=sub_names)

    if sort == '-id':
        pmediants_obj = pmediants_obj.order_by("-id")

    pmediants_list = [to_dict(i) for i in pmediants_obj]
    keys = ['items']
    values = [pmediants_list]
    data_dict = dict(zip(keys, values))
    response['data'] = data_dict
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmediants_upload_post(request):
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
                    if data[i].__contains__('项目编号') and data[i].__contains__('所属街镇') and data[
                        i].__contains__('产量权重因子') and data[i].__contains__('经度') and data[i].__contains__(
                        '纬度') and data[i].__contains__('所属区'):
                        project_id = data[i]['项目编号']
                        sub_names = data[i]['所属街镇']
                        weight_percentage = data[i]['产量权重因子']
                        lng = data[i]['经度']
                        lat = data[i]['纬度']
                        district = data[i]['所属区']
                        list = PmedianTransferStation.objects.create(project_id=project_id,
                                                                     sub_names=sub_names,
                                                                     weight_percentage=weight_percentage, lng=lng,
                                                                     lat=lat,
                                                                     district=district)
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
def pmediants_clear_post(request):
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
    sub_names = q_dict.get('sub_names')
    print(sub_names, '........data')

    pmediants_obj = PmedianTransferStation.objects.all()

    ### 筛选
    if project_id != None and project_id != '':
        print(project_id, 'clear_post..................project_id')
        pmediants_obj = pmediants_obj.filter(project_id=project_id)
    if sub_names != None and sub_names != '':
        print(sub_names, 'clear_post..................sub_names')
        pmediants_obj = pmediants_obj.filter(sub_names=sub_names)
    projects = p_median_project.objects.all()
    for i in projects:
        i.ts_size = 0
        i.save()

    pmediants_obj.delete()

    return JsonResponse(response, safe=False)