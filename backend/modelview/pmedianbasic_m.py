from django.db import models

class PmedianBasic(models.Model):
	id = models.AutoField(verbose_name='序号',primary_key=True)
	project_id = models.CharField(verbose_name='项目编号',null=True,max_length=50)
	name = models.CharField(verbose_name='参数名称',null=True,max_length=50)
	value = models.FloatField(verbose_name='参数值',null=True)
	unit = models.CharField(verbose_name='单位',null=True,max_length=50)
	note = models.CharField(verbose_name='备注',null=True,max_length=50)
	
	class Meta: 
		app_label = 'backend'
