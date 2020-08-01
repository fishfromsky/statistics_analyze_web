
from backend.modelview import TianRecyclingPoint
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


########################################################################## TianRecyclingPoint 开始##################################
@csrf_exempt
@require_http_methods(['GET'])
def tianrecy1_list_get(request):
	response = {'code': 20000, 'message': 'success'}

	### 筛选的字段
	street_town_name = request.GET.get('street_town_name')
	point_no = request.GET.get('point_no')
	point_name = request.GET.get('point_name')
	village_name = request.GET.get('village_name')
	point_style = request.GET.get('point_style')
	service_person = request.GET.get('service_person')
	manager = request.GET.get('manager')
	
	sort = request.GET.get('sort')
	page = request.GET.get('page')
	limit = request.GET.get('limit')

	tianrecy1_obj = TianRecyclingPoint.objects.all()
	street_town_name_list = [i.street_town_name for i in tianrecy1_obj]
	unique_street_town_name = list(set(street_town_name_list))
	point_style_list = [i.point_style for i in tianrecy1_obj]
	unique_point_style = list(set(point_style_list))
	

	# 筛选
	if street_town_name != None and street_town_name != '':
		tianrecy1_obj = tianrecy1_obj.filter(street_town_name=street_town_name)
	if point_no != None and point_no != '':
		tianrecy1_obj = tianrecy1_obj.filter(point_no=point_no)
	if point_name != None and point_name != '':
		tianrecy1_obj = tianrecy1_obj.filter(point_name=point_name)
	if village_name != None and village_name != '':
		tianrecy1_obj = tianrecy1_obj.filter(village_name=village_name)
	if point_style != None and point_style != '':
		tianrecy1_obj = tianrecy1_obj.filter(point_style=point_style)
	if service_person != None and service_person != '':
		tianrecy1_obj = tianrecy1_obj.filter(service_person=service_person)
	if manager != None and manager != '':
		tianrecy1_obj = tianrecy1_obj.filter(manager=manager)
	
	if sort == '-id':
		tianrecy1_obj = tianrecy1_obj.order_by("-id")

	# 分页
	paginator = Paginator(tianrecy1_obj, limit)       # 分页
	tianrecy1_obj_page = paginator.get_page(page)

	# 生成response，参考mockjs的内容
	tianrecy1_list = [to_dict(i) for i in tianrecy1_obj_page]
	keys = ['total', 'items', 'unique_street_town_name', 'unique_point_style']
	values = [tianrecy1_obj.count(), tianrecy1_list, unique_street_town_name, unique_point_style]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def tianrecy1_update_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	post_id = post_info.get('id')
	TianRecyclingPoint.objects.filter(id=post_id).update(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def tianrecy1_create_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)
	TianRecyclingPoint.objects.create(**post_info)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def tianrecy1_delete_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_id = json.loads(request.body)
	TianRecyclingPoint.objects.filter(id=post_id).delete()
	return JsonResponse(response, safe=False)


@csrf_exempt
@require_http_methods(['GET'])
def tianrecy1_download_get(request):
	response = {'code': 20000, 'message': 'success'}
	street_town_name = request.GET.get('street_town_name')
	point_no = request.GET.get('point_no')
	point_name = request.GET.get('point_name')
	village_name = request.GET.get('village_name')
	point_style = request.GET.get('point_style')
	service_person = request.GET.get('service_person')
	manager = request.GET.get('manager')
	
	sort = request.GET.get('sort')
	tianrecy1_obj = TianRecyclingPoint.objects.all()
	# 筛选
	if street_town_name != None and street_town_name != '':
		tianrecy1_obj = tianrecy1_obj.filter(street_town_name=street_town_name)
	if point_no != None and point_no != '':
		tianrecy1_obj = tianrecy1_obj.filter(point_no=point_no)
	if point_name != None and point_name != '':
		tianrecy1_obj = tianrecy1_obj.filter(point_name=point_name)
	if village_name != None and village_name != '':
		tianrecy1_obj = tianrecy1_obj.filter(village_name=village_name)
	if point_style != None and point_style != '':
		tianrecy1_obj = tianrecy1_obj.filter(point_style=point_style)
	if service_person != None and service_person != '':
		tianrecy1_obj = tianrecy1_obj.filter(service_person=service_person)
	if manager != None and manager != '':
		tianrecy1_obj = tianrecy1_obj.filter(manager=manager)
	
	if sort == '-id':
		tianrecy1_obj = tianrecy1_obj.order_by("-id")

	tianrecy1_list = [to_dict(i) for i in tianrecy1_obj]
	keys = ['items']
	values = [tianrecy1_list]
	data_dict = dict(zip(keys, values))
	response['data'] = data_dict
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def tianrecy1_upload_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	# print(post_info)
	print(type(post_info))
	createsetlist=[]
	for i in post_info:
		obj_i = TianRecyclingPoint(
			id = i.get('id'), 
			street_town_name = i.get('所属街镇'), 
			point_no = i.get('回收点编号'), 
			point_name = i.get('回收点名称'), 
			point_figure = i.get('回收点图片'), 
			village_name = i.get('所属小区'), 
			housing_committee = i.get('所属居委'), 
			point_style = i.get('回收点类型'), 
			recycling_style = i.get('可回收物品种'), 
			detail_location = i.get('详细地址'), 
			longitude = i.get('回收点经度'), 
			latitude = i.get('回收点纬度'), 
			design_load = i.get('设计日回收量（吨）'), 
			household_served = i.get('服务户数'), 
			service_day = i.get('服务日期'), 
			service_time = i.get('服务时间'), 
			service_person = i.get('回收人员'), 
			service_person_phone = i.get('回收人电话'), 
			property_unit = i.get('产权单位'), 
			operation_unit = i.get('运营单位'), 
			manager = i.get('负责人'), 
			manager_phone = i.get('负责人电话'), 
			starting_running_time = i.get('开始运营时间'), 
			
			)
		createsetlist.append(obj_i)
	TianRecyclingPoint.objects.bulk_create(createsetlist)
	return JsonResponse(response, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def tianrecy1_clear_post(request):
	response = {'code': 20000, 'message': 'success'}
	post_info = json.loads(request.body)
	print(post_info)                        # 注意如果是根据项目删除需要根据条件筛选后再删除
	TianRecyclingPoint.objects.all().delete()
	return JsonResponse(response, safe=False)
########################################################################## TianRecyclingPoint 结束##################################