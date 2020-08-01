from django.db import models

class NewTest000(models.Model):
	id = models.AutoField(verbose_name='序号',primary_key=True)
	timestamp1 = models.DateTimeField(verbose_name='时间戳',null=True)
	author1 = models.CharField(verbose_name='作者',null=True,max_length=100,default='i am author 001')
	reviewer1 = models.CharField(verbose_name='审核',max_length=100)
	title1 = models.CharField(verbose_name='标题',null=True,max_length=100)
	content_short1 = models.CharField(verbose_name='概要',null=True,max_length=100)
	content1 = models.CharField(verbose_name='内容',null=True,max_length=100)
	forecast1 = models.FloatField(verbose_name='预测',null=True)
	importance1 = models.IntegerField(verbose_name='重要性',null=True,default=4)
	type1 = models.CharField(verbose_name='类型',null=True,max_length=100)
	status1 = models.CharField(verbose_name='状态',null=True,max_length=100,default='draft')
	display_time1 = models.DateTimeField(verbose_name='展示时间',null=True)
	comment_disabled1 = models.BooleanField(verbose_name='可评论',null=True)
	pageviews1 = models.IntegerField(verbose_name='页码',null=True,default=0)
	image_uri1 = models.CharField(verbose_name='图片链接',max_length=100,default='https://wpimg.wallstcn.com/4c69009c-0fd4-4153-b112-6cb53d1cf943')
	platforms1 = models.CharField(verbose_name='平台',null=True,max_length=100)
	class Meta: 
		app_label = 'backend'
