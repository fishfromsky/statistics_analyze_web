from django.db import models

class TianRecyclingPoint(models.Model):
	id = models.AutoField(verbose_name='序号',primary_key=True)
	street_town_name = models.CharField(verbose_name='所属街镇',null=True,max_length=20)
	point_no = models.CharField(verbose_name='回收点编号',null=True,max_length=20)
	point_name = models.CharField(verbose_name='回收点名称',null=True,max_length=20)
	point_figure = models.CharField(verbose_name='回收点图片',null=True,max_length=100)
	village_name = models.CharField(verbose_name='所属小区',null=True,max_length=20)
	housing_committee = models.CharField(verbose_name='所属居委',null=True,max_length=20)
	point_style = models.CharField(verbose_name='回收点类型',null=True,max_length=20)
	recycling_style = models.CharField(verbose_name='可回收物品种',null=True,max_length=20)
	detail_location = models.CharField(verbose_name='详细地址',null=True,max_length=50)
	longitude = models.FloatField(verbose_name='回收点经度',null=True)
	latitude = models.FloatField(verbose_name='回收点纬度',null=True)
	design_load = models.FloatField(verbose_name='设计日回收量（吨）',null=True)
	household_served = models.FloatField(verbose_name='服务户数',null=True)
	service_day = models.CharField(verbose_name='服务日期',null=True,max_length=20)
	service_time = models.CharField(verbose_name='服务时间',null=True,max_length=20)
	service_person = models.CharField(verbose_name='回收人员',null=True,max_length=20)
	service_person_phone = models.CharField(verbose_name='回收人电话',null=True,max_length=20)
	property_unit = models.CharField(verbose_name='产权单位',null=True,max_length=20)
	operation_unit = models.CharField(verbose_name='运营单位',null=True,max_length=20)
	manager = models.CharField(verbose_name='负责人',null=True,max_length=20)
	manager_phone = models.CharField(verbose_name='负责人电话',null=True,max_length=20)
	starting_running_time = models.CharField(verbose_name='开始运营时间',null=True,max_length=20)
	
	class Meta: 
		app_label = 'backend'