import urllib.parse as parse
from backend.modelview import PmedianCostMatrix
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


########################################################################## PmedianCostMatrix 开始##################################
@csrf_exempt
@require_http_methods(['GET'])
def pmediancstmtr_list_get(request):
    response = {'code': 20000, 'message': 'success'}

    ### 筛选的字段
    project_id = request.GET.get('project_id')
    ts_name = request.GET.get('ts_name')
    rrc_name = request.GET.get('rrc_name')

    sort = request.GET.get('sort')
    page = request.GET.get('page')
    limit = request.GET.get('limit')

    pmediancstmtr_obj = PmedianCostMatrix.objects.all()
    project_id_list = [i.project_id for i in pmediancstmtr_obj]
    unique_project_id = list(set(project_id_list))
    ts_name_list = [i.ts_name for i in pmediancstmtr_obj]
    unique_ts_name = list(set(ts_name_list))
    rrc_name_list = [i.rrc_name for i in pmediancstmtr_obj]
    unique_rrc_name = list(set(rrc_name_list))

    # 筛选
    if project_id != None and project_id != '':
        pmediancstmtr_obj = pmediancstmtr_obj.filter(project_id=project_id)
    if ts_name != None and ts_name != '':
        pmediancstmtr_obj = pmediancstmtr_obj.filter(ts_name=ts_name)
    if rrc_name != None and rrc_name != '':
        pmediancstmtr_obj = pmediancstmtr_obj.filter(rrc_name=rrc_name)

    if sort == '-id':
        pmediancstmtr_obj = pmediancstmtr_obj.order_by("-id")

    # 分页
    paginator = Paginator(pmediancstmtr_obj, limit)  # 分页
    pmediancstmtr_obj_page = paginator.get_page(page)

    # 生成response，参考mockjs的内容
    pmediancstmtr_list = [to_dict(i) for i in pmediancstmtr_obj_page]
    keys = ['total', 'items', 'unique_project_id', 'unique_ts_name', 'unique_rrc_name']
    values = [pmediancstmtr_obj.count(), pmediancstmtr_list, unique_project_id, unique_ts_name, unique_rrc_name]
    data_dict = dict(zip(keys, values))
    response['data'] = data_dict
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmediancstmtr_update_post(request):
    response = {'code': 20000, 'message': 'success'}
    post_info = json.loads(request.body)
    post_id = post_info.get('id')
    PmedianCostMatrix.objects.filter(id=post_id).update(**post_info)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmediancstmtr_create_post(request):
    response = {'code': 20000, 'message': 'success'}
    post_info = json.loads(request.body)
    print(post_info)
    PmedianCostMatrix.objects.create(**post_info)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmediancstmtr_delete_post(request):
    response = {'code': 20000, 'message': 'success'}
    post_id = json.loads(request.body)
    project_id = PmedianCostMatrix.objects.get(id=post_id).project_id
    project = p_median_project.objects.get(project_id=project_id)
    project.basic_size = project.basic_size - 1
    project.save()
    PmedianCostMatrix.objects.filter(id=post_id).delete()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def pmediancstmtr_download_get(request):
    response = {'code': 20000, 'message': 'success'}
    project_id = request.GET.get('project_id')
    ts_name = request.GET.get('ts_name')
    rrc_name = request.GET.get('rrc_name')

    sort = request.GET.get('sort')
    pmediancstmtr_obj = PmedianCostMatrix.objects.all()
    # 筛选
    if project_id != None and project_id != '':
        pmediancstmtr_obj = pmediancstmtr_obj.filter(project_id=project_id)
    if ts_name != None and ts_name != '':
        pmediancstmtr_obj = pmediancstmtr_obj.filter(ts_name=ts_name)
    if rrc_name != None and rrc_name != '':
        pmediancstmtr_obj = pmediancstmtr_obj.filter(rrc_name=rrc_name)

    if sort == '-id':
        pmediancstmtr_obj = pmediancstmtr_obj.order_by("-id")

    pmediancstmtr_list = [to_dict(i) for i in pmediancstmtr_obj]
    keys = ['items']
    values = [pmediancstmtr_list]
    data_dict = dict(zip(keys, values))
    response['data'] = data_dict
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmediancstmtr_upload_post(request):
    response = {'code': 20000, 'message': 'success'}
    data = json.loads(request.body)
    if data[0].__contains__('项目编号'):
        if p_median_project.objects.filter(project_id=data[0]['项目编号']) == 0:
            response['code'] = 50000
            response['message'] = '请先创建项目！'
        else:
            project = p_median_project.objects.get(project_id=data[0]['项目编号'])
            if project.cost_matrix_size != 0:
                response['code'] = 50000
                response['message'] = '该项目此表数据已存在'
            else:
                for i in range(len(data)):
                    if data[i].__contains__('项目编号') and data[i].__contains__('中转站') and data[i].__contains__('集散厂') and \
                            data[i].__contains__('成本(碳排放)') and data[i].__contains__('单位'):
                        project_id = data[i]['项目编号']
                        ts_name = data[i]['中转站']
                        rrc_name = data[i]['集散厂']
                        cost = data[i]['成本(碳排放)']
                        cost_unit = data[i]['单位']
                        list = PmedianCostMatrix.objects.create(project_id=project_id, ts_name=ts_name,
                                                                rrc_name=rrc_name, cost=cost, cost_unit=cost_unit)
                        list.save()
                        project.cost_matrix_size = len(data)
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
def pmediancstmtr_clear_post(request):
    response = {'code': 20000, 'message': 'success'}
    post = request.get_full_path().split('?')[1]

    q_list = post.split('&')
    keys = []
    values = []
    for q in q_list:
        keys.append(q.split('=')[0])
        values.append(parse.unquote(q.split('=')[1]))
    q_dict = dict(zip(keys, values))

    project_id = q_dict.get('project_id')

    ts_name = q_dict.get('ts_name')

    rrc_name = q_dict.get('rrc_name')

    pmediancstmtr_obj = PmedianCostMatrix.objects.all()

    ### 筛选
    if project_id != None and project_id != '':
        print(project_id, 'clear_post..................project_id')
        pmediancstmtr_obj = pmediancstmtr_obj.filter(project_id=project_id)
    if ts_name != None and ts_name != '':
        print(ts_name, 'clear_post..................ts_name')
        pmediancstmtr_obj = pmediancstmtr_obj.filter(ts_name=ts_name)
    if rrc_name != None and rrc_name != '':
        print(rrc_name, 'clear_post..................rrc_name')
        pmediancstmtr_obj = pmediancstmtr_obj.filter(rrc_name=rrc_name)
    projects = p_median_project.objects.all()
    for i in projects:
        i.cost_matrix_size = 0
        i.save()

    pmediancstmtr_obj.delete()

    return JsonResponse(response, safe=False)