from django.db import models

class PmedianTransferStation(models.Model):
	id = models.AutoField(verbose_name='序号',primary_key=True)
	project_id = models.CharField(verbose_name='项目编号',null=True,max_length=50)
	sub_names = models.CharField(verbose_name='所属街镇',null=True,max_length=50)
	weight_percentage = models.FloatField(verbose_name='产量权重因子',null=True)
	lng = models.FloatField(verbose_name='经度',null=True)
	lat = models.FloatField(verbose_name='维度',null=True)
	district = models.CharField(verbose_name='所属区',null=True,max_length=50)
	
	class Meta: 
		app_label = 'backend'
