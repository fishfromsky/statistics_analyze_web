
from backend.modelview import MockArticle2
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


########################################################################## MockArticle2 开始##################################
@csrf_exempt
@require_http_methods(['GET'])
def article2_list_get(request):
	response = {'code': 20000, 'message': 'success'}

	### 筛选的字段
	title = request.GET.get('title')
	importance = request.GET.get('importance')
	type = request.GET.get('type')
	
	sort = request.GET.get('sort')
	page = request.GET.get('page')
	limit = request.GET.get('limit')

	article2_obj = MockArticle2.objects.all()
	importance_list = [i.importance for i in article2_obj]
	unique_importance = list(set(importance_list))
	type_list = [i.type for i in article2_obj]
	unique_type = list(set(type_list))
	

	# 筛选
	if title != None and title != '':
		article2_obj = article2_obj.filter(title=title)
	if importance != None and importance != '':
		article2_obj = article2_obj.filter(importance=importance)
	if type != None and type != '':
		article2_obj = article2_obj.filter(type=type)
	
	if sort == '-id':
		article2_obj = article2_obj.order_by("-id")

	# 分页
	paginator = Paginator(article2_obj, limit)       # 分页
	article2_obj_page = paginator.get_page(page)

	# 生成response，参考mockjs的内容
	article2_list = [to_dict(i) for i in article2_obj_page]
	keys = ['total', 'items', 'unique_importance', 'unique_type']
	values = [article2_obj.count(), article2_list, unique_importance, unique_type]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article2_update_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	post_id = post_info.get('id')
	MockArticle2.objects.filter(id=post_id).update(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article2_create_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)
	MockArticle2.objects.create(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article2_delete_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_id = json.loads(request.body)
	MockArticle2.objects.filter(id=post_id).delete()
	return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def article2_download_get(request):
	response = {'code': 20000, 'message': 'success'}
	title = request.GET.get('title')
	importance = request.GET.get('importance')
	type = request.GET.get('type')
	
	sort = request.GET.get('sort')
	article2_obj = MockArticle2.objects.all()
	# 筛选
	if title != None and title != '':
		article2_obj = article2_obj.filter(title=title)
	if importance != None and importance != '':
		article2_obj = article2_obj.filter(importance=importance)
	if type != None and type != '':
		article2_obj = article2_obj.filter(type=type)
	
	if sort == '-id':
		article2_obj = article2_obj.order_by("-id")

	article2_list = [to_dict(i) for i in article2_obj]
	keys = ['items']
	values = [article2_list]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article2_upload_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	# print(post_info)
	print(type(post_info))
	createsetlist=[]
	for i in post_info:
		obj_i = MockArticle2(
			timestamp=i.get('timestamp'), 
			author=i.get('author'), 
			reviewer=i.get('reviewer'), 
			title=i.get('title'), 
			content_short=i.get('content_short'), 
			content=i.get('content'), 
			forecast=i.get('forecast'), 
			importance=i.get('importance'), 
			type=i.get('type'), 
			status=i.get('status'), 
			display_time=i.get('display_time'), 
			comment_disabled=i.get('comment_disabled'), 
			pageviews=i.get('pageviews'), 
			image_uri=i.get('image_uri'), 
			platforms=i.get('platforms'), 
			
			)
		createsetlist.append(obj_i)
	MockArticle2.objects.bulk_create(createsetlist)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article2_clear_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)                        # 注意如果是根据项目删除需要根据条件筛选后再删除
	MockArticle2.objects.all().delete()
	return JsonResponse(response, safe=False)
########################################################################## MockArticle2 结束##################################