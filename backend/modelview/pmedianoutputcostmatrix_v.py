import urllib.parse as parse
from backend.modelview import PmedianOutputCostMatrix
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


########################################################################## PmedianOutputCostMatrix 开始##################################
@csrf_exempt
@require_http_methods(['GET'])
def pmedianoutputcomx_list_get(request):
	response = {'code': 20000, 'message': 'success', 'unique_project_id': []}

	### 筛选的字段
	project_id = request.GET.get('project_id')
	p = request.GET.get('p')
	
	sort = request.GET.get('sort')
	page = request.GET.get('page')
	limit = request.GET.get('limit')

	pmedianoutputcomx_obj = PmedianOutputCostMatrix.objects.all()
	

	# 筛选
	if project_id != None and project_id != '':
		pmedianoutputcomx_obj = pmedianoutputcomx_obj.filter(project_id=project_id)
	if p != None and p != '':
		pmedianoutputcomx_obj = pmedianoutputcomx_obj.filter(p=p)
	
	if sort == '-id':
		pmedianoutputcomx_obj = pmedianoutputcomx_obj.order_by("-id")

	project_id_list = [i.project_id for i in pmedianoutputcomx_obj]
	unique_project_id = list(set(project_id_list))
	response['unique_project_id'] = unique_project_id
	# 分页
	paginator = Paginator(pmedianoutputcomx_obj, limit)       # 分页
	pmedianoutputcomx_obj_page = paginator.get_page(page)

	# 生成response，参考mockjs的内容
	pmedianoutputcomx_list = [to_dict(i) for i in pmedianoutputcomx_obj_page]
	keys = ['total', 'items']
	values = [pmedianoutputcomx_obj.count(), pmedianoutputcomx_list]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def pmedianoutputcomx_update_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	post_id = post_info.get('id')
	PmedianOutputCostMatrix.objects.filter(id=post_id).update(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def pmedianoutputcomx_create_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)
	PmedianOutputCostMatrix.objects.create(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def pmedianoutputcomx_delete_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_id = json.loads(request.body)
	PmedianOutputCostMatrix.objects.filter(id=post_id).delete()
	return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def pmedianoutputcomx_get_cost(request):
	response = {'code': 20000, 'message': 'success', 'transport_cost': [], 'scale_cost': [], 'p': []}
	project_id = request.GET.get('project_id')
	data = PmedianOutputCostMatrix.objects.filter(project_id=project_id)
	transport_cost = []
	scale_cost = []
	p = []
	for item in data:
		transport_cost.append(to_dict(item).get('transport_cost'))
		scale_cost.append(to_dict(item).get('scale_cost'))
		p.append(to_dict(item).get('p'))
	response['transport_cost'] = transport_cost
	response['scale_cost'] = scale_cost
	response['p'] = p
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['GET'])
def pmedianoutputcomx_download_get(request):
	response = {'code': 20000, 'message': 'success'}
	project_id = request.GET.get('project_id')
	p = request.GET.get('p')
	
	sort = request.GET.get('sort')
	pmedianoutputcomx_obj = PmedianOutputCostMatrix.objects.all()
	# 筛选
	if project_id != None and project_id != '':
		pmedianoutputcomx_obj = pmedianoutputcomx_obj.filter(project_id=project_id)
	if p != None and p != '':
		pmedianoutputcomx_obj = pmedianoutputcomx_obj.filter(p=p)
	
	if sort == '-id':
		pmedianoutputcomx_obj = pmedianoutputcomx_obj.order_by("-id")

	pmedianoutputcomx_list = [to_dict(i) for i in pmedianoutputcomx_obj]
	keys = ['items']
	values = [pmedianoutputcomx_list]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def pmedianoutputcomx_upload_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	# print(post_info)
	print(type(post_info))
	createsetlist=[]
	for i in post_info:
		obj_i = PmedianOutputCostMatrix(
			# id = i.get('id'), 
			project_id = i.get('项目编号'), 
			p = i.get('p值'), 
			transport_cost = i.get('交通成本'), 
			scale_cost = i.get('规模成本'), 
			total_cost = i.get('总成本'), 
			
			)
		createsetlist.append(obj_i)
	PmedianOutputCostMatrix.objects.bulk_create(createsetlist)
	return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['POST'])
def pmedianoutputcomx_clear_post(request):
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
	p = q_dict.get('p')
	print(p, '........data')
	


	pmedianoutputcomx_obj = PmedianOutputCostMatrix.objects.all()

	### 筛选
	if project_id != None and project_id != '':
		print(project_id, 'clear_post..................project_id')
		pmedianoutputcomx_obj = pmedianoutputcomx_obj.filter(project_id=project_id)
	if p != None and p != '':
		print(p, 'clear_post..................p')
		pmedianoutputcomx_obj = pmedianoutputcomx_obj.filter(p=p)
	

	pmedianoutputcomx_obj.delete()

	return JsonResponse(response, safe=False)