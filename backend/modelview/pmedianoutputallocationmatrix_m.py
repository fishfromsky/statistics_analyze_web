from django.db import models

class PmedianOutputAllocationMatrix(models.Model):
	id = models.AutoField(verbose_name='序号',primary_key=True)
	project_id = models.CharField(verbose_name='项目编号',null=True,max_length=50)
	ts = models.CharField(verbose_name='集散场',null=True,max_length=50)
	rrc = models.CharField(verbose_name='中转站',null=True,max_length=50)
	
	class Meta: 
		app_label = 'backend'
