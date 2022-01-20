import urllib.parse as parse
from backend.modelview import PmedianOutputAllocationMatrix, PmedianTransferStation, PmedianRecyclingCenter, PmedianOutputBuildScale
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


########################################################################## PmedianOutputAllocationMatrix 开始##################################

@csrf_exempt
@require_http_methods(['GET'])
def getalllist_utputallocation(request):
	response = {'code': 20000, 'message': 'success', 'data': []}
	project_id = request.GET.get('project_id')
	p_value = request.GET.get('p_value')

	data = PmedianOutputAllocationMatrix.objects.filter(project_id=project_id, p_value=p_value)

	for item in data:
		item = to_dict(item)
		ts_info = PmedianTransferStation.objects.get(sub_names=item['ts'])
		item['ts_lng'] = ts_info.lng
		item['ts_lat'] = ts_info.lat
		item['ts_district'] = ts_info.district
		rrc_info = PmedianRecyclingCenter.objects.get(sub_district=item['rrc'])
		rrc_deal = PmedianOutputBuildScale.objects.get(p_value=p_value, rrc=item['rrc']).rrc_scale
		item['rrc_lng'] = rrc_info.lng
		item['rrc_lat'] = rrc_info.lat
		item['rrc_district'] = rrc_info.district
		item['rrc_deal'] = rrc_deal
		response['data'].append(item)

	return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def utputallocation_list_get(request):
	response = {'code': 20000, 'message': 'success'}

	### 筛选的字段
	project_id = request.GET.get('project_id')
	ts = request.GET.get('ts')
	
	sort = request.GET.get('sort')
	page = request.GET.get('page')
	limit = request.GET.get('limit')

	utputallocation_obj = PmedianOutputAllocationMatrix.objects.all()
	project_id_list = [i.project_id for i in utputallocation_obj]
	unique_project_id = list(set(project_id_list))
	

	# 筛选
	if project_id != None and project_id != '':
		utputallocation_obj = utputallocation_obj.filter(project_id=project_id)
	if ts != None and ts != '':
		utputallocation_obj = utputallocation_obj.filter(ts=ts)
	
	if sort == '-id':
		utputallocation_obj = utputallocation_obj.order_by("-id")

	# 分页
	paginator = Paginator(utputallocation_obj, limit)       # 分页
	utputallocation_obj_page = paginator.get_page(page)

	# 生成response，参考mockjs的内容
	utputallocation_list = [to_dict(i) for i in utputallocation_obj_page]
	keys = ['total', 'items', 'unique_project_id']
	values = [utputallocation_obj.count(), utputallocation_list, unique_project_id]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def utputallocation_update_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	post_id = post_info.get('id')
	PmedianOutputAllocationMatrix.objects.filter(id=post_id).update(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def utputallocation_create_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	PmedianOutputAllocationMatrix.objects.create(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def utputallocation_delete_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_id = json.loads(request.body)
	PmedianOutputAllocationMatrix.objects.filter(id=post_id).delete()
	return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def utputallocation_download_get(request):
	response = {'code': 20000, 'message': 'success'}
	project_id = request.GET.get('project_id')
	ts = request.GET.get('ts')
	
	sort = request.GET.get('sort')
	utputallocation_obj = PmedianOutputAllocationMatrix.objects.all()
	# 筛选
	if project_id != None and project_id != '':
		utputallocation_obj = utputallocation_obj.filter(project_id=project_id)
	if ts != None and ts != '':
		utputallocation_obj = utputallocation_obj.filter(ts=ts)
	
	if sort == '-id':
		utputallocation_obj = utputallocation_obj.order_by("-id")

	utputallocation_list = [to_dict(i) for i in utputallocation_obj]
	keys = ['items']
	values = [utputallocation_list]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def utputallocation_upload_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	# print(post_info)
	print(type(post_info))
	createsetlist=[]
	for i in post_info:
		obj_i = PmedianOutputAllocationMatrix(
			# id = i.get('id'), 
			project_id = i.get('项目编号'), 
			ts = i.get('集散场'), 
			rrc = i.get('中转站'), 
			
			)
		createsetlist.append(obj_i)
	PmedianOutputAllocationMatrix.objects.bulk_create(createsetlist)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def utputallocation_clear_post(request):
	response = {'code': 20000, 'message': 'success'}
	post = request.get_full_path().split('?')[1]

	q_list = post.split('&')
	keys = []
	values =[]
	for q in q_list:
		keys.append(q.split('=')[0])
		values.append(parse.unquote(q.split('=')[1]))
	q_dict = dict(zip(keys, values))
	print(q_dict)

	project_id = q_dict.get('project_id')
	print(project_id, '........data')
	ts = q_dict.get('ts')
	print(ts, '........data')
	


	utputallocation_obj = PmedianOutputAllocationMatrix.objects.all()

	### 筛选
	if project_id != None and project_id != '':
		print(project_id, 'clear_post..................project_id')
		utputallocation_obj = utputallocation_obj.filter(project_id=project_id)
	if ts != None and ts != '':
		print(ts, 'clear_post..................ts')
		utputallocation_obj = utputallocation_obj.filter(ts=ts)
	

	utputallocation_obj.delete()

	return JsonResponse(response, safe=False)