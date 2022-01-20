from django.db import models

class PmedianRecyclingCenter(models.Model):
	id = models.AutoField(verbose_name='序号',primary_key=True)
	project_id = models.CharField(verbose_name='项目编号',null=True,max_length=50)
	district = models.CharField(verbose_name='区',null=True,max_length=50)
	sub_district = models.CharField(verbose_name='街镇',null=True,max_length=50)
	location = models.CharField(verbose_name='位置',null=True,max_length=50)
	lng = models.FloatField(verbose_name='经度',null=True)
	lat = models.FloatField(verbose_name='纬度',null=True)
	max_load = models.FloatField(verbose_name='处理量',null=True)
	max_load_unit = models.CharField(verbose_name='单位',null=True,max_length=50)
	has_selected = models.BooleanField(verbose_name='已选择',null=True,default=0)
	
	class Meta: 
		app_label = 'backend'
