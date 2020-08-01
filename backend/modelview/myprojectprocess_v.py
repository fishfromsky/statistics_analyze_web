import urllib.parse as parse
from backend.modelview import MyProjectProcess
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


########################################################################## MyProjectProcess 开始##################################
@csrf_exempt
@require_http_methods(['GET'])
def myprojectpr_list_get(request):
	response = {'code': 20000, 'message': 'success'}

	### 筛选的字段
	project_name = request.GET.get('project_name')
	project_id = request.GET.get('project_id')
	
	sort = request.GET.get('sort')
	page = request.GET.get('page')
	limit = request.GET.get('limit')

	myprojectpr_obj = MyProjectProcess.objects.all()
	project_name_list = [i.project_name for i in myprojectpr_obj]
	unique_project_name = list(set(project_name_list))
	

	# 筛选
	if project_name != None and project_name != '':
		myprojectpr_obj = myprojectpr_obj.filter(project_name=project_name)
	if project_id != None and project_id != '':
		myprojectpr_obj = myprojectpr_obj.filter(project_id=project_id)
	
	if sort == '-id':
		myprojectpr_obj = myprojectpr_obj.order_by("-id")

	# 分页
	paginator = Paginator(myprojectpr_obj, limit)       # 分页
	myprojectpr_obj_page = paginator.get_page(page)

	# 生成response，参考mockjs的内容
	myprojectpr_list = [to_dict(i) for i in myprojectpr_obj_page]
	keys = ['total', 'items', 'unique_project_name']
	values = [myprojectpr_obj.count(), myprojectpr_list, unique_project_name]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def myprojectpr_update_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	post_id = post_info.get('id')
	MyProjectProcess.objects.filter(id=post_id).update(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def myprojectpr_create_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)
	MyProjectProcess.objects.create(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def myprojectpr_delete_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_id = json.loads(request.body)
	MyProjectProcess.objects.filter(id=post_id).delete()
	return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def myprojectpr_download_get(request):
	response = {'code': 20000, 'message': 'success'}
	project_name = request.GET.get('project_name')
	project_id = request.GET.get('project_id')
	
	sort = request.GET.get('sort')
	myprojectpr_obj = MyProjectProcess.objects.all()
	# 筛选
	if project_name != None and project_name != '':
		myprojectpr_obj = myprojectpr_obj.filter(project_name=project_name)
	if project_id != None and project_id != '':
		myprojectpr_obj = myprojectpr_obj.filter(project_id=project_id)
	
	if sort == '-id':
		myprojectpr_obj = myprojectpr_obj.order_by("-id")

	myprojectpr_list = [to_dict(i) for i in myprojectpr_obj]
	keys = ['items']
	values = [myprojectpr_list]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def myprojectpr_upload_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	# print(post_info)
	print(type(post_info))
	createsetlist=[]
	for i in post_info:
		obj_i = MyProjectProcess(
			# id = i.get('id'), 
			project_name = i.get('项目名称'), 
			project_id = i.get('项目编号'), 
			process_status_integer = i.get('项目状态'), 
			process_status_char = i.get('项目状态说明'), 
			process_percent = i.get('项目进度'), 
			algorithm_feedback = i.get('算法反馈'), 
			other_para001 = i.get('预留字段1'), 
			other_para002 = i.get('预留字段2'), 
			other_para003 = i.get('预留字段3'), 
			other_para004 = i.get('预留字段4'), 
			
			)
		createsetlist.append(obj_i)
	MyProjectProcess.objects.bulk_create(createsetlist)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def myprojectpr_clear_post(request):
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

	project_name = q_dict.get('project_name')
	print(project_name, '........data')
	project_id = q_dict.get('project_id')
	print(project_id, '........data')
	


	myprojectpr_obj = MyProjectProcess.objects.all()

	### 筛选
	if project_name != None and project_name != '':
		print(project_name, 'clear_post..................project_name')
		myprojectpr_obj = myprojectpr_obj.filter(project_name=project_name)
	if project_id != None and project_id != '':
		print(project_id, 'clear_post..................project_id')
		myprojectpr_obj = myprojectpr_obj.filter(project_id=project_id)
	

	myprojectpr_obj.delete()

	return JsonResponse(response, safe=False)