
from backend.modelview import MockArticle1
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


########################################################################## MockArticle1 开始##################################
@csrf_exempt
@require_http_methods(['GET'])
def article1_list_get(request):
	response = {'code': 20000, 'message': 'success'}

	### 筛选的字段
	title = request.GET.get('title')
	importance = request.GET.get('importance')
	type = request.GET.get('type')
	
	sort = request.GET.get('sort')
	page = request.GET.get('page')
	limit = request.GET.get('limit')

	article1_obj = MockArticle1.objects.all()
	importance_list = [i.importance for i in article1_obj]
	unique_importance = list(set(importance_list))
	type_list = [i.type for i in article1_obj]
	unique_type = list(set(type_list))
	

	# 筛选
	if title != None and title != '':
		article1_obj = article1_obj.filter(title=title)
	if importance != None and importance != '':
		article1_obj = article1_obj.filter(importance=importance)
	if type != None and type != '':
		article1_obj = article1_obj.filter(type=type)
	
	if sort == '-id':
		article1_obj = article1_obj.order_by("-id")

	# 分页
	paginator = Paginator(article1_obj, limit)       # 分页
	article1_obj_page = paginator.get_page(page)

	# 生成response，参考mockjs的内容
	article1_list = [to_dict(i) for i in article1_obj_page]
	keys = ['total', 'items', 'unique_importance', 'unique_type']
	values = [article1_obj.count(), article1_list, unique_importance, unique_type]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article1_update_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	post_id = post_info.get('id')
	MockArticle1.objects.filter(id=post_id).update(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article1_create_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)
	MockArticle1.objects.create(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article1_delete_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_id = json.loads(request.body)
	MockArticle1.objects.filter(id=post_id).delete()
	return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def article1_download_get(request):
	response = {'code': 20000, 'message': 'success'}
	title = request.GET.get('title')
	importance = request.GET.get('importance')
	type = request.GET.get('type')
	
	sort = request.GET.get('sort')
	article1_obj = MockArticle1.objects.all()
	# 筛选
	if title != None and title != '':
		article1_obj = article1_obj.filter(title=title)
	if importance != None and importance != '':
		article1_obj = article1_obj.filter(importance=importance)
	if type != None and type != '':
		article1_obj = article1_obj.filter(type=type)
	
	if sort == '-id':
		article1_obj = article1_obj.order_by("-id")

	article1_list = [to_dict(i) for i in article1_obj]
	keys = ['items']
	values = [article1_list]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article1_upload_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	# print(post_info)
	print(type(post_info))
	createsetlist=[]
	for i in post_info:
		obj_i = MockArticle1(
			# id = i.get('id'), 
			timestamp = i.get('时间戳'), 
			author = i.get('作者'), 
			reviewer = i.get('审核'), 
			title = i.get('标题'), 
			content_short = i.get('概要'), 
			content = i.get('内容'), 
			forecast = i.get('预测'), 
			importance = i.get('重要性'), 
			type = i.get('类型'), 
			status = i.get('状态'), 
			display_time = i.get('展示时间'), 
			comment_disabled = i.get('可评论'), 
			pageviews = i.get('页码'), 
			image_uri = i.get('图片链接'), 
			platforms = i.get('平台'), 
			
			)
		createsetlist.append(obj_i)
	MockArticle1.objects.bulk_create(createsetlist)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article1_clear_post(request):
	response = {'code': 20000, 'message': 'success'}
	post = request.get_full_path().split('?')[1]

	q_list = post.split('&')
	keys = []
	values =[]
	for q in q_list:
		keys.append(q.split('=')[0])
		values.append(q.split('=')[1])
	q_dict = dict(zip(keys, values))
	print(q_dict)

	title = q_dict.get('title')
	print(title, '........data')
	importance = q_dict.get('importance')
	print(importance, '........data')
	type = q_dict.get('type')
	print(type, '........data')
	


	article1_obj = MockArticle1.objects.all()

	### 筛选
	if title != None and title != '':
		print(title, 'clear_post..................title')
		article1_obj = article1_obj.filter(title=title)
	if importance != None and importance != '':
		print(importance, 'clear_post..................importance')
		article1_obj = article1_obj.filter(importance=importance)
	if type != None and type != '':
		print(type, 'clear_post..................type')
		article1_obj = article1_obj.filter(type=type)
	

	article1_obj.delete()

	return JsonResponse(response, safe=False)