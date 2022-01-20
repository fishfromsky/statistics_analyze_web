from django.db import models

class PmedianOutputBuildScale(models.Model):
	id = models.AutoField(verbose_name='序号',primary_key=True)
	project_id = models.CharField(verbose_name='项目编号',null=True,max_length=50)
	p_value = models.IntegerField(verbose_name='p值',null=True)
	rrc = models.CharField(verbose_name='集散场',null=True,max_length=50)
	rrc_scale = models.FloatField(verbose_name='集散场规模',null=True)
	scale_unit = models.CharField(verbose_name='规模单位',null=True,max_length=50)
	
	class Meta: 
		app_label = 'backend'
