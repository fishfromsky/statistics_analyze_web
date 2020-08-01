
from backend.modelview import PmedianBasic
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
def pemedianbs_list_get(request):
	response = {'code': 20000, 'message': 'success'}

	### 筛选的字段
	project_id = request.GET.get('project_id')
	name = request.GET.get('name')
	
	sort = request.GET.get('sort')
	page = request.GET.get('page')
	limit = request.GET.get('limit')

	pemedianbs_obj = PmedianBasic.objects.all()
	project_id_list = [i.project_id for i in pemedianbs_obj]
	unique_project_id = list(set(project_id_list))
	

	# 筛选
	if project_id != None and project_id != '':
		pemedianbs_obj = pemedianbs_obj.filter(project_id=project_id)
	if name != None and name != '':
		pemedianbs_obj = pemedianbs_obj.filter(name=name)
	
	if sort == '-id':
		pemedianbs_obj = pemedianbs_obj.order_by("-id")

	# 分页
	paginator = Paginator(pemedianbs_obj, limit)       # 分页
	pemedianbs_obj_page = paginator.get_page(page)

	# 生成response，参考mockjs的内容
	pemedianbs_list = [to_dict(i) for i in pemedianbs_obj_page]
	keys = ['total', 'items', 'unique_project_id']
	values = [pemedianbs_obj.count(), pemedianbs_list, unique_project_id]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def pemedianbs_update_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)
	# post_id = post_info.get('id')
	PmedianBasic.objects.filter(id=post_id).update(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def pemedianbs_create_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)
	PmedianBasic.objects.create(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def pemedianbs_delete_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_id = json.loads(request.body)
	PmedianBasic.objects.filter(id=post_id).delete()
	return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def pemedianbs_download_get(request):
	response = {'code': 20000, 'message': 'success'}
	project_id = request.GET.get('project_id')
	name = request.GET.get('name')
	
	sort = request.GET.get('sort')
	pemedianbs_obj = PmedianBasic.objects.all()
	# 筛选
	if project_id != None and project_id != '':
		pemedianbs_obj = pemedianbs_obj.filter(project_id=project_id)
	if name != None and name != '':
		pemedianbs_obj = pemedianbs_obj.filter(name=name)
	
	if sort == '-id':
		pemedianbs_obj = pemedianbs_obj.order_by("-id")

	pemedianbs_list = [to_dict(i) for i in pemedianbs_obj]
	keys = ['items']
	values = [pemedianbs_list]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def pemedianbs_upload_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	# print(post_info)
	print(type(post_info))
	createsetlist=[]
	for i in post_info:
		obj_i = PmedianBasic(
			project_id=i.get('project_id'), 
			name=i.get('name'), 
			value=i.get('value'), 
			unit=i.get('unit'), 
			note=i.get('note'), 
			
			)
		createsetlist.append(obj_i)
	PmedianBasic.objects.bulk_create(createsetlist)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def pemedianbs_clear_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)                        # 注意如果是根据项目删除需要根据条件筛选后再删除
	PmedianBasic.objects.all().delete()
	return JsonResponse(response, safe=False)
########################################################################## PmedianBasic 结束##################################