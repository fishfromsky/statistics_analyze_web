from django.db import models

class PmedianOutputCostMatrix(models.Model):
	id = models.AutoField(verbose_name='序号',primary_key=True)
	project_id = models.CharField(verbose_name='项目编号',null=True,max_length=50)
	p = models.IntegerField(verbose_name='p值',null=True)
	transport_cost = models.FloatField(verbose_name='交通成本',null=True)
	scale_cost = models.FloatField(verbose_name='规模成本',null=True)
	total_cost = models.FloatField(verbose_name='总成本',null=True)
	
	class Meta: 
		app_label = 'backend'
