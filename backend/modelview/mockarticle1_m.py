from django.db import models

class MockArticle1(models.Model):
	id = models.AutoField(verbose_name='序号',primary_key=True)
	timestamp = models.DateTimeField(verbose_name='时间戳',null=True)
	author = models.CharField(verbose_name='作者',null=True,max_length=100,default='i am author 001')
	reviewer = models.CharField(verbose_name='审核',max_length=100)
	title = models.CharField(verbose_name='标题',null=True,max_length=100)
	content_short = models.CharField(verbose_name='概要',null=True,max_length=100)
	content = models.CharField(verbose_name='内容',null=True,max_length=100)
	forecast = models.FloatField(verbose_name='预测',null=True)
	importance = models.IntegerField(verbose_name='重要性',null=True,default=4)
	type = models.CharField(verbose_name='类型',null=True,max_length=100)
	status = models.CharField(verbose_name='状态',null=True,max_length=100,default='draft')
	display_time = models.DateTimeField(verbose_name='展示时间',null=True)
	comment_disabled = models.BooleanField(verbose_name='可评论',null=True)
	pageviews = models.IntegerField(verbose_name='页码',null=True,default=0)
	image_uri = models.CharField(verbose_name='图片链接',max_length=100,default='https://wpimg.wallstcn.com/4c69009c-0fd4-4153-b112-6cb53d1cf943')
	platforms = models.CharField(verbose_name='平台',null=True,max_length=100)
	
	class Meta: 
		app_label = 'backend'
