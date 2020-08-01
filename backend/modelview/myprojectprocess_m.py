from django.db import models

class MyProjectProcess(models.Model):
	id = models.AutoField(verbose_name='序号',primary_key=True)
	project_name = models.CharField(verbose_name='项目名称',null=True,max_length=50)
	project_id = models.CharField(verbose_name='项目编号',null=True,max_length=50)
	process_status_integer = models.IntegerField(verbose_name='项目状态',null=True)
	process_status_char = models.CharField(verbose_name='项目状态说明',null=True,max_length=50)
	process_percent = models.IntegerField(verbose_name='项目进度',null=True)
	algorithm_feedback = models.CharField(verbose_name='算法反馈',null=True,max_length=50)
	other_para001 = models.CharField(verbose_name='预留字段1',null=True,max_length=50)
	other_para002 = models.CharField(verbose_name='预留字段2',null=True,max_length=50)
	other_para003 = models.CharField(verbose_name='预留字段3',null=True,max_length=50)
	other_para004 = models.CharField(verbose_name='预留字段4',null=True,max_length=50)
	
	class Meta: 
		app_label = 'backend'
