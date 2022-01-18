import urllib.parse as parse
from backend.modelview import PmedianOutputBuildScale
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


########################################################################## PmedianOutputBuildScale 开始##################################
@csrf_exempt
@require_http_methods(['GET'])
def dianoutputbuilds_list_get(request):
	response = {'code': 20000, 'message': 'success'}

	### 筛选的字段
	project_id = request.GET.get('project_id')
	p_value = request.GET.get('p_value')
	
	sort = request.GET.get('sort')
	page = request.GET.get('page')
	limit = request.GET.get('limit')

	dianoutputbuilds_obj = PmedianOutputBuildScale.objects.all()
	project_id_list = [i.project_id for i in dianoutputbuilds_obj]
	unique_project_id = list(set(project_id_list))
	

	# 筛选
	if project_id != None and project_id != '':
		dianoutputbuilds_obj = dianoutputbuilds_obj.filter(project_id=project_id)
	if p_value != None and p_value != '':
		dianoutputbuilds_obj = dianoutputbuilds_obj.filter(p_value=p_value)
	
	if sort == '-id':
		dianoutputbuilds_obj = dianoutputbuilds_obj.order_by("-id")

	# 分页
	paginator = Paginator(dianoutputbuilds_obj, limit)       # 分页
	dianoutputbuilds_obj_page = paginator.get_page(page)

	# 生成response，参考mockjs的内容
	dianoutputbuilds_list = [to_dict(i) for i in dianoutputbuilds_obj_page]
	keys = ['total', 'items', 'unique_project_id']
	values = [dianoutputbuilds_obj.count(), dianoutputbuilds_list, unique_project_id]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def dianoutputbuilds_update_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	post_id = post_info.get('id')
	PmedianOutputBuildScale.objects.filter(id=post_id).update(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def dianoutputbuilds_create_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)
	PmedianOutputBuildScale.objects.create(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def dianoutputbuilds_delete_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_id = json.loads(request.body)
	PmedianOutputBuildScale.objects.filter(id=post_id).delete()
	return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def dianoutputbuilds_download_get(request):
	response = {'code': 20000, 'message': 'success'}
	project_id = request.GET.get('project_id')
	p_value = request.GET.get('p_value')
	
	sort = request.GET.get('sort')
	dianoutputbuilds_obj = PmedianOutputBuildScale.objects.all()
	# 筛选
	if project_id != None and project_id != '':
		dianoutputbuilds_obj = dianoutputbuilds_obj.filter(project_id=project_id)
	if p_value != None and p_value != '':
		dianoutputbuilds_obj = dianoutputbuilds_obj.filter(p_value=p_value)
	
	if sort == '-id':
		dianoutputbuilds_obj = dianoutputbuilds_obj.order_by("-id")

	dianoutputbuilds_list = [to_dict(i) for i in dianoutputbuilds_obj]
	keys = ['items']
	values = [dianoutputbuilds_list]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def dianoutputbuilds_upload_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	# print(post_info)
	print(type(post_info))
	createsetlist=[]
	for i in post_info:
		obj_i = PmedianOutputBuildScale(
			# id = i.get('id'), 
			project_id = i.get('项目编号'), 
			p_value = i.get('p值'), 
			rrc = i.get('集散场'), 
			rrc_scale = i.get('集散场规模'), 
			scale_unit = i.get('规模单位'), 
			
			)
		createsetlist.append(obj_i)
	PmedianOutputBuildScale.objects.bulk_create(createsetlist)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def dianoutputbuilds_clear_post(request):
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
	p_value = q_dict.get('p_value')
	print(p_value, '........data')
	


	dianoutputbuilds_obj = PmedianOutputBuildScale.objects.all()

	### 筛选
	if project_id != None and project_id != '':
		print(project_id, 'clear_post..................project_id')
		dianoutputbuilds_obj = dianoutputbuilds_obj.filter(project_id=project_id)
	if p_value != None and p_value != '':
		print(p_value, 'clear_post..................p_value')
		dianoutputbuilds_obj = dianoutputbuilds_obj.filter(p_value=p_value)
	

	dianoutputbuilds_obj.delete()

	return JsonResponse(response, safe=False)