import urllib.parse as parse
from backend.modelview import PmedianBasic
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


########################################################################## PmedianBasic 开始##################################
@csrf_exempt
@require_http_methods(['GET'])
def pmedianbs_list_get(request):
    response = {'code': 20000, 'message': 'success'}

    ### 筛选的字段
    project_id = request.GET.get('project_id')
    name = request.GET.get('name')

    sort = request.GET.get('sort')
    page = request.GET.get('page')
    limit = request.GET.get('limit')

    pmedianbs_obj = PmedianBasic.objects.all()
    project_id_list = [i.project_id for i in pmedianbs_obj]
    unique_project_id = list(set(project_id_list))

    # 筛选
    if project_id != None and project_id != '':
        pmedianbs_obj = pmedianbs_obj.filter(project_id=project_id)
    if name != None and name != '':
        pmedianbs_obj = pmedianbs_obj.filter(name=name)

    if sort == '-id':
        pmedianbs_obj = pmedianbs_obj.order_by("-id")

    # 分页
    paginator = Paginator(pmedianbs_obj, limit)  # 分页
    pmedianbs_obj_page = paginator.get_page(page)

    # 生成response，参考mockjs的内容
    pmedianbs_list = [to_dict(i) for i in pmedianbs_obj_page]
    keys = ['total', 'items', 'unique_project_id']
    values = [pmedianbs_obj.count(), pmedianbs_list, unique_project_id]
    data_dict = dict(zip(keys, values))
    response['data'] = data_dict
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmedianbs_update_post(request):
    response = {'code': 20000, 'message': 'success'}
    post_info = json.loads(request.body)
    post_id = post_info.get('id')
    PmedianBasic.objects.filter(id=post_id).update(**post_info)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmedianbs_create_post(request):
    response = {'code': 20000, 'message': 'success'}
    post_info = json.loads(request.body)
    print(post_info)
    PmedianBasic.objects.create(**post_info)
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmedianbs_delete_post(request):
    response = {'code': 20000, 'message': 'success'}
    post_id = json.loads(request.body)
    project_id = PmedianBasic.objects.get(id=post_id).project_id
    project = p_median_project.objects.get(project_id=project_id)
    project.basic_size = project.basic_size - 1
    project.save()
    PmedianBasic.objects.filter(id=post_id).delete()
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def pmedianbs_download_get(request):
    response = {'code': 20000, 'message': 'success'}
    project_id = request.GET.get('project_id')
    name = request.GET.get('name')

    sort = request.GET.get('sort')
    pmedianbs_obj = PmedianBasic.objects.all()
    # 筛选
    if project_id != None and project_id != '':
        pmedianbs_obj = pmedianbs_obj.filter(project_id=project_id)
    if name != None and name != '':
        pmedianbs_obj = pmedianbs_obj.filter(name=name)

    if sort == '-id':
        pmedianbs_obj = pmedianbs_obj.order_by("-id")

    pmedianbs_list = [to_dict(i) for i in pmedianbs_obj]
    keys = ['items']
    values = [pmedianbs_list]
    data_dict = dict(zip(keys, values))
    response['data'] = data_dict
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmedianbs_upload_post(request):
    response = {'code': 20000, 'message': 'success'}
    data = json.loads(request.body)
    # print(post_info)
    createsetlist = []
    if data[0].__contains__('项目编号'):
        if p_median_project.objects.filter(project_id=data[0]['项目编号']).count() == 0:
            response['code'] = 50000
            response['message'] = '请先创建项目！'
        else:
            project = p_median_project.objects.get(project_id=data[0]['项目编号'])
            if project.basic_size != 0:
                response['code'] = 50000
                response['message'] = '该项目此表数据已存在！'
            else:
                for i in range(len(data)):
                    if data[i].__contains__('项目编号') and data[i].__contains__('参数名称') and data[i].__contains__(
                            '参数值') and data[i].__contains__('单位') and data[i].__contains__('备注'):
                        project_id = data[i]['项目编号']
                        name = data[i]['参数名称']
                        value = data[i]['参数值']
                        unit = data[i]['单位']
                        note = data[i]['备注']
                        list = PmedianBasic.objects.create(project_id=project_id, name=name,
                                                           value=value, unit=unit, note=note)
                        list.save()
                        project.basic_size = len(data)
                        project.save()
                    else:
                        response['code'] = 50000
                        response['message'] = '表头与数据不一致或者缺少数据！'
    return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmedianbs_clear_post(request):
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
    name = q_dict.get('name')
    pmedianbs_obj = PmedianBasic.objects.all()

    ### 筛选
    if project_id != None and project_id != '':
        pmedianbs_obj = pmedianbs_obj.filter(project_id=project_id)
    if name != None and name != '':
        pmedianbs_obj = pmedianbs_obj.filter(name=name)
    pmedianbs_obj.delete()
    projects = p_median_project.objects.all()
    for i in projects:
        i.basic_size = 0
        i.save()
    return JsonResponse(response, safe=False)