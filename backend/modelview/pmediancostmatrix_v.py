import urllib.parse as parse
from backend.modelview import PmedianCostMatrix
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
	paginator = Paginator(pmediancstmtr_obj, limit)       # 分页
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
	post_info = json.loads(request.body)
	# print(post_info)
	print(type(post_info))
	createsetlist=[]
	for i in post_info:
		obj_i = PmedianCostMatrix(
			# id = i.get('id'), 
			project_id = i.get('项目编号'), 
			ts_name = i.get('中转站'), 
			rrc_name = i.get('集散场'), 
			cost = i.get('成本(碳排放)'), 
			cost_unit = i.get('单位'), 
			
			)
		createsetlist.append(obj_i)
	PmedianCostMatrix.objects.bulk_create(createsetlist)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def pmediancstmtr_clear_post(request):
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
	ts_name = q_dict.get('ts_name')
	print(ts_name, '........data')
	rrc_name = q_dict.get('rrc_name')
	print(rrc_name, '........data')
	


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
	

	pmediancstmtr_obj.delete()

	return JsonResponse(response, safe=False)