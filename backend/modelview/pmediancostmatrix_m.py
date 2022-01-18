from django.db import models

class PmedianCostMatrix(models.Model):
	id = models.AutoField(verbose_name='序号',primary_key=True)
	project_id = models.CharField(verbose_name='项目编号',null=True,max_length=50)
	ts_name = models.CharField(verbose_name='中转站',null=True,max_length=50)
	rrc_name = models.CharField(verbose_name='集散场',null=True,max_length=50)
	cost = models.FloatField(verbose_name='成本(碳排放)',null=True)
	cost_unit = models.CharField(verbose_name='单位',null=True,max_length=50)
	
	class Meta: 
		app_label = 'backend'
