
from backend.modelview import NewTest000
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


########################################################################## NewTest000 开始##################################
@csrf_exempt
@require_http_methods(['GET'])
def test000_list_get(request):
	response = {'code': 20000, 'message': 'success'}

	### 筛选的字段
	title1 = request.GET.get('title1')
	importance1 = request.GET.get('importance1')
	type1 = request.GET.get('type1')
	
	sort = request.GET.get('sort')
	page = request.GET.get('page')
	limit = request.GET.get('limit')

	test000_obj = NewTest000.objects.all()
	importance1_list = [i.importance1 for i in test000_obj]
	unique_importance1 = list(set(importance1_list))
	type1_list = [i.type1 for i in test000_obj]
	unique_type1 = list(set(type1_list))
	

	# 筛选
	if title1 != None and title1 != '':
		test000_obj = test000_obj.filter(title1=title1)
	if importance1 != None and importance1 != '':
		test000_obj = test000_obj.filter(importance1=importance1)
	if type1 != None and type1 != '':
		test000_obj = test000_obj.filter(type1=type1)
	
	if sort == '-id':
		test000_obj = test000_obj.order_by("-id")

	# 分页
	paginator = Paginator(test000_obj, limit)       # 分页
	test000_obj_page = paginator.get_page(page)

	# 生成response，参考mockjs的内容
	test000_list = [to_dict(i) for i in test000_obj_page]
	keys = ['total', 'items', 'unique_importance1', 'unique_type1']
	values = [test000_obj.count(), test000_list, unique_importance1, unique_type1]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def test000_update_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	post_id = post_info.get('id')
	NewTest000.objects.filter(id=post_id).update(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def test000_create_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)
	NewTest000.objects.create(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def test000_delete_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_id = json.loads(request.body)
	NewTest000.objects.filter(id=post_id).delete()
	return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def test000_download_get(request):
	response = {'code': 20000, 'message': 'success'}
	title1 = request.GET.get('title1')
	importance1 = request.GET.get('importance1')
	type1 = request.GET.get('type1')
	
	sort = request.GET.get('sort')
	test000_obj = NewTest000.objects.all()
	# 筛选
	if title1 != None and title1 != '':
		test000_obj = test000_obj.filter(title1=title1)
	if importance1 != None and importance1 != '':
		test000_obj = test000_obj.filter(importance1=importance1)
	if type1 != None and type1 != '':
		test000_obj = test000_obj.filter(type1=type1)
	
	if sort == '-id':
		test000_obj = test000_obj.order_by("-id")

	test000_list = [to_dict(i) for i in test000_obj]
	keys = ['items']
	values = [test000_list]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def test000_upload_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	# print(post_info)
	print(type(post_info))
	createsetlist=[]
	for i in post_info:
		obj_i = NewTest000(
			timestamp1=i.get('timestamp1'), 
			author1=i.get('author1'), 
			reviewer1=i.get('reviewer1'), 
			title1=i.get('title1'), 
			content_short1=i.get('content_short1'), 
			content1=i.get('content1'), 
			forecast1=i.get('forecast1'), 
			importance1=i.get('importance1'), 
			type1=i.get('type1'), 
			status1=i.get('status1'), 
			display_time1=i.get('display_time1'), 
			comment_disabled1=i.get('comment_disabled1'), 
			pageviews1=i.get('pageviews1'), 
			image_uri1=i.get('image_uri1'), 
			platforms1=i.get('platforms1'), 
			
			)
		createsetlist.append(obj_i)
	NewTest000.objects.bulk_create(createsetlist)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def test000_clear_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)                        # 注意如果是根据项目删除需要根据条件筛选后再删除
	NewTest000.objects.all().delete()
	return JsonResponse(response, safe=False)
########################################################################## NewTest000 结束##################################