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


class FactoryList(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    deal = models.IntegerField(default=0)


# 城市表
class City(models.Model):
    name = models.CharField(max_length=200)


# 区表
class District(models.Model):
    name = models.CharField(max_length=255)
    city_name = models.ForeignKey(to='City', on_delete=models.CASCADE)


# 城镇表
class Town(models.Model):
    name = models.CharField(max_length=255)
    district_name = models.ForeignKey(to='District', on_delete=models.CASCADE)


# 全市经济情况表
class Economy_Info_City(models.Model):
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)
    year = models.CharField(max_length=200)  # 年份
    gdp = models.CharField(max_length=200, null=True)
    gdp_per_capita = models.CharField(max_length=200, null=True)
    gdp_growth_rate = models.FloatField(null=True)
    unemployment_rate = models.FloatField(null=True)   # 失业率


# 全市人口信息表
class Population_Info_City(models.Model):
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    population = models.CharField(max_length=200, null=True)
    population_density = models.CharField(max_length=200, null=True)
    population_rate = models.FloatField(null=True)
    households = models.CharField(max_length=200, null=True)   # 户数
    average_person_per_household = models.CharField(max_length=200, null=True)  # 每户平均人口


# 全市生活垃圾表
class Garbage_Info_City(models.Model):
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    total_garbage = models.CharField(max_length=200)
    collect_transport_garbage = models.CharField(max_length=200)  # 生活垃圾清运量
    volume_of_treated = models.CharField(max_length=200)   # 生活垃圾处理量


# 全市无害化处理厂信息
class Gargabe_Deal_City(models.Model):
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    factory_num_total = models.IntegerField()
    landFill = models.IntegerField()  # 垃圾填埋厂数量
    incineration = models.IntegerField()  # 垃圾焚烧厂数量
    compost = models.IntegerField()  # 垃圾堆肥场数量
    else_num = models.IntegerField()  # 其他


# 全市无害化处理能力信息
class Gargage_Deal_Capacity_City(models.Model):
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    deal_num_total = models.CharField(max_length=200)
    landfill = models.CharField(max_length=200)
    incineration = models.CharField(max_length=200)
    compost = models.CharField(max_length=200)
    else_num = models.CharField(max_length=200)


# 全市无害化处理量表
class Garbage_Deal_Volume_City(models.Model):
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    deal_volume_total = models.CharField(max_length=200)
    landfill = models.CharField(max_length=200)
    incineration = models.CharField(max_length=200)
    compost = models.CharField(max_length=200)
    else_num = models.CharField(max_length=200)

class p_median_project(models.Model):
    project_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    basic_size = models.IntegerField()
    ts_size = models.IntegerField()
    rrc_size = models.IntegerField()
    cost_matrix_size = models.IntegerField()

class basic(models.Model):
    project_id = models.ForeignKey(to="p_median_project", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    value = models.FloatField()
    unit = models.CharField(max_length=200)
    note = models.CharField(max_length=200)


class ts(models.Model):
    project_id = models.ForeignKey(to="p_median_project", on_delete=models.CASCADE)
    sub_names = models.CharField(max_length=200)
    weight_percentage = models.FloatField()
    lng = models.FloatField()
    lat = models.FloatField()
    district = models.CharField(max_length=200)


class rrc(models.Model):
    project_id = models.ForeignKey(to="p_median_project", on_delete=models.CASCADE)
    district = models.CharField(max_length=200)
    sub_district = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    lng = models.FloatField()
    lat = models.FloatField()
    max_load = models.IntegerField()
    has_selected = models.IntegerField()
    district_no = models.IntegerField()


class cost_matrix(models.Model):
    project_id = models.ForeignKey(to="p_median_project", on_delete=models.CASCADE)
    Euclid_distance = models.FloatField()










