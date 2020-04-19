from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    role = models.CharField(max_length=10, default="普通用户")
    token = models.CharField(max_length=100, verbose_name="token", default='')
    phone_number = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.username


class ModelsList(models.Model):
    modelname = models.CharField(max_length=100, null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255, default='')
    reference = models.IntegerField(default=0)
    star = models.IntegerField(default=0)
