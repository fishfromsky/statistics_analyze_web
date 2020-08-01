from django.db import models
import django.utils.timezone as timezone

class MockArticle(models.Model):
	id = models.AutoField(verbose_name='序号', primary_key=True)
	timestamp = models.DateTimeField(null=True)
	author = models.CharField(null=True,max_length=100,default='i am author 001')
	reviewer = models.CharField(max_length=100)
	title = models.CharField(null=True,max_length=100)
	content_short = models.CharField(null=True,max_length=100)
	content = models.CharField(null=True,max_length=100)
	forecast = models.FloatField(null=True)
	importance = models.IntegerField(null=True,default=4)
	type = models.CharField(null=True,max_length=100)
	status = models.CharField(null=True,max_length=100,default='draft')
	display_time = models.DateTimeField(null=True)
	comment_disabled = models.BooleanField(null=True)
	pageviews = models.IntegerField(null=True,default=0)
	image_uri = models.CharField(max_length=100,default='https://wpimg.wallstcn.com/4c69009c-0fd4-4153-b112-6cb53d1cf943')
	platforms = models.CharField(null=True,max_length=100)
	
	class Meta: 
		app_label = 'backend'