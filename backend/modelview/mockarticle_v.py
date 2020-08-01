
from backend.modelview import MockArticle
from django.http import JsonResponse
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ManyToManyField
import json
from rest_framework.authtoken.models import Token
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


########################################################################## MockArticle 开始##################################
@csrf_exempt
@require_http_methods(['GET'])
def article_list_get(request):
	response = {'code': 20000, 'message': 'success'}

	### 筛选的字段
	title = request.GET.get('title')
	importance = request.GET.get('importance')
	type = request.GET.get('type')

	sort = request.GET.get('sort')
	page = request.GET.get('page')
	limit = request.GET.get('limit')

	article_obj = MockArticle.objects.all()
	importance_list = [i.importance for i in article_obj]
	unique_importance = list(set(importance_list))

	type_list = [i.type for i in article_obj]
	unique_type = list(set(type_list))

	# 筛选    
	if title != None and title != '':
		article_obj = article_obj.filter(title=title)
	if importance != None and importance != '':
		article_obj = article_obj.filter(importance=importance)
	if type != None and type != '':
		article_obj = article_obj.filter(type=type)

	if sort == '-id':
		article_obj = article_obj.order_by("-id")

	# 分页
	paginator = Paginator(article_obj, limit)       # 分页
	article_obj_page = paginator.get_page(page)

	# 生成response，参考mockjs的内容
	article_list = [to_dict(i) for i in article_obj_page]
	keys = ['total', 'items', 'unique_importance', 'unique_type']
	values = [article_obj.count(), article_list, unique_importance, unique_type]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article_update_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)
	# post_id = post_info.get('id')
	MockArticle.objects.filter(id=post_id).update(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article_create_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)
	MockArticle.objects.create(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article_delete_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_id = json.loads(request.body)
	MockArticle.objects.filter(id=post_id).delete()
	return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def article_download_get(request):
	response = {'code': 20000, 'message': 'success'}
	title = request.GET.get('title')
	importance = request.GET.get('importance')
	type = request.GET.get('type')
	sort = request.GET.get('sort')
	article_obj = MockArticle.objects.all()
	# 筛选
	if title != None and title != '':
		article_obj = article_obj.filter(title=title)
	if importance != None and importance != '':
		article_obj = article_obj.filter(importance=importance)
	if type != None and type != '':
		article_obj = article_obj.filter(type=type)

	if sort == '-id':
		article_obj = article_obj.order_by("-id")

	article_list = [to_dict(i) for i in article_obj]
	keys = ['items']
	values = [article_list]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article_upload_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	# print(post_info)
	print(type(post_info))
	createsetlist=[]
	for i in post_info:
		obj_i = MockArticle(
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
	MockArticle.objects.bulk_create(createsetlist)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def article_clear_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)                        # 注意如果是根据项目删除需要根据条件筛选后再删除
	MockArticle.objects.all().delete()
	return JsonResponse(response, safe=False)
########################################################################## MockArticle 结束##################################