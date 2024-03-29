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


# 垃圾处理厂具体信息
class FactoryList(models.Model):
    name = models.CharField(max_length=255, null=False)
    district = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    company = models.CharField(max_length=255, default='')
    type = models.CharField(max_length=255, null=False, default='')
    typeId = models.IntegerField(null=False, default=0)
    longitude = models.FloatField()
    latitude = models.FloatField()
    deal = models.FloatField(default=0)


# 垃圾中转站信息
class TransferFactoryList(models.Model):
    district = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)
    capacity = models.FloatField()


# 垃圾收集点信息
class CollectFactoryList(models.Model):
    district = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)


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
    gdp_first_industry = models.FloatField(null=True)
    gdp_second_industry = models.FloatField(null=True)
    gdp_third_industry = models.FloatField(null=True)


# 全市人口信息表
class Population_Info_City(models.Model):
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    population = models.FloatField(max_length=200, null=True, default=0)
    population_density = models.FloatField(max_length=200, null=True, default=0)
    population_rate = models.FloatField(null=True)
    households = models.FloatField(max_length=200, null=True, default=0)   # 户数
    average_person_per_household = models.FloatField(max_length=200, null=True, default=0)  # 每户平均人口

# 全市垃圾产量信息表
class Garbage_City_Production(models.Model):
    year = models.CharField(max_length=250)
    production=models.CharField(max_length=250)

# 全市生活垃圾表
class Garbage_Info_City(models.Model):
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    collect_transport_garbage = models.CharField(max_length=200, default='')  # 生活垃圾清运量
    volume_of_treated = models.CharField(max_length=200, default='')   # 生活垃圾处理量
    rate_of_treated = models.CharField(max_length=200, default='')   # 生活垃圾处理率


# 全市无害化处理厂信息
class Gargabe_Deal_City(models.Model):
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    collect_factory_num = models.CharField(max_length=255, default='')
    factory_num_total = models.CharField(max_length=255, default='')  # 无害化处理厂数量
    landFill = models.CharField(max_length=255, default='')  # 垃圾填埋厂数量
    incineration = models.CharField(max_length=255, default='')  # 垃圾焚烧厂数量
    compost = models.CharField(max_length=255, default='')  # 垃圾堆肥场数量
    else_num = models.CharField(max_length=255, default='')  # 其他


# 全市无害化处理能力信息
class Gargage_Deal_Capacity_City(models.Model):
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    deal_num_total = models.CharField(max_length=200, default='')
    landfill = models.CharField(max_length=200, default='')
    incineration = models.CharField(max_length=200, default='')
    compost = models.CharField(max_length=200, default='')
    else_num = models.CharField(max_length=200, default='')


# 全市无害化处理量表
class Garbage_Deal_Volume_City(models.Model):
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    deal_volume_total = models.CharField(max_length=200, default='')
    landfill = models.CharField(max_length=200, default='')
    incineration = models.CharField(max_length=200, default='')
    compost = models.CharField(max_length=200, default='')
    else_num = models.CharField(max_length=200, default='')


# 危险废弃物产生数据
class Dangerous_Garbage_City(models.Model):
    city = models.ForeignKey(to="City", on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    production = models.CharField(max_length=200, default='')
    deal = models.CharField(max_length=200, default='')
    use = models.CharField(max_length=200, default='')
    store = models.CharField(max_length=200, default='')


class Crawl_Data_Record(models.Model):
    table_type = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    time = models.CharField(max_length=200, default='08:30:00')
    key_words = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default='-')
    file_location = models.CharField(max_length=200)


class p_median_project(models.Model):
    project_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    basic_size = models.IntegerField()
    ts_size = models.IntegerField()
    rrc_size = models.IntegerField()
    project_state = models.CharField(max_length=200, default='未运行')
    cost_matrix_size = models.IntegerField()


class lstm_project(models.Model):
    project_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    table_size = models.IntegerField(default=0)
    status = models.CharField(max_length=255, default='未运行')


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


class lstm_result(models.Model):
    project_id = models.ForeignKey(to='lstm_project', on_delete=models.CASCADE)
    year = models.CharField(max_length=255, null=False)
    real = models.FloatField(null=False)
    pred = models.FloatField(null=False)
    time = models.DateTimeField(auto_now_add=True)
    sort = models.IntegerField(default=1)


class cost_matrix(models.Model):
    project_id = models.ForeignKey(to="p_median_project", on_delete=models.CASCADE)
    Euclid_distance = models.FloatField()


class multi_regression_project(models.Model):
    project_id = models.CharField(max_length=255, null=False, primary_key=True)
    name = models.CharField(max_length=255, null=False)
    table_size = models.IntegerField(default=0)
    status = models.CharField(max_length=255, default='未运行')


class multi_regression_result(models.Model):
    project_id = models.ForeignKey(to="multi_regression_project", on_delete=models.CASCADE)
    pred = models.FloatField(null=False)
    real = models.FloatField(null=False)
    time = models.DateTimeField(auto_now_add=True)
    sort = models.IntegerField(default=1)


class kmeans_project(models.Model):
    project_id = models.CharField(max_length=255, null=False, primary_key=True)
    name = models.CharField(max_length=255, null=False)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='未运行')

class svm_project(models.Model):
    project_id = models.CharField(max_length=255, null=False, primary_key=True)
    name = models.CharField(max_length=255, null=False)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='未运行')

class xgboost_project(models.Model):
    project_id = models.CharField(max_length=255, null=False, primary_key=True)
    name = models.CharField(max_length=255, null=False)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='未运行')


class kmeans_result(models.Model):
    project_id = models.ForeignKey(to="kmeans_project", on_delete=models.CASCADE)
    xaxis = models.FloatField(null=False)
    yaxis = models.FloatField(null=False)
    label = models.IntegerField(null=False, default=0)
    district = models.CharField(max_length=255, default='')
    time = models.DateTimeField(auto_now_add=True)
    sort = models.IntegerField(default=1)

class svm_result(models.Model):
    project_id = models.ForeignKey(to="svm_project", on_delete=models.CASCADE)
    xaxis = models.FloatField(null=False)
    yaxis = models.FloatField(null=False)
    label = models.IntegerField(null=False, default=0)
    district = models.CharField(max_length=255, default='')
    time = models.DateTimeField(auto_now_add=True)
    sort = models.IntegerField(default=1)

class xgboost_result(models.Model):
    project_id = models.ForeignKey(to="xgboost_project", on_delete=models.CASCADE)
    xaxis = models.FloatField(null=False)
    yaxis = models.FloatField(null=False)
    label = models.IntegerField(null=False, default=0)
    district = models.CharField(max_length=255, default='')
    time = models.DateTimeField(auto_now_add=True)
    sort = models.IntegerField(default=1)


class relation_project(models.Model):
    project_id = models.CharField(max_length=255, primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='未运行')


class model_table(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    sort_Id = models.IntegerField(default=0)
    pic_url = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')


class algorithm_project(models.Model):
    project_id = models.IntegerField(default=1, primary_key=True)
    name = models.CharField(max_length=255, null=False)
    time = models.IntegerField(default=0)
    describe = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to="UserProfile", on_delete=models.CASCADE)


class selected_algorithm_table(models.Model):
    model = models.ForeignKey(to="model_table", on_delete=models.CASCADE)
    user = models.ForeignKey(to="UserProfile", on_delete=models.CASCADE)
    algorithm = models.ForeignKey(to="algorithm_project", on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='未运行')


class relation_hot_matrix_result(models.Model):
    project_id = models.ForeignKey(to="relation_project", on_delete=models.CASCADE)
    label = models.CharField(max_length=255, null=False)
    year = models.FloatField(max_length=255, default=0)
    garbage_clear = models.FloatField()
    population = models.FloatField()
    ratio_city_rural = models.FloatField()
    household = models.FloatField()
    people_per_capita = models.FloatField()
    ratio_sex = models.FloatField()
    age_0_14 = models.FloatField()
    age_15_64 = models.FloatField()
    age_65 = models.FloatField()
    disposable_income = models.FloatField()
    consume_cost = models.FloatField()
    public_cost = models.FloatField()
    gdp = models.FloatField()
    gdp_first_industry = models.FloatField()
    gdp_second_industry = models.FloatField()
    gdp_third_industry = models.FloatField()
    gnp = models.FloatField()
    education = models.FloatField()
    sort = models.IntegerField(default=1)
    time = models.DateTimeField(auto_now_add=True)


class relation_RF_result(models.Model):
    project_id = models.ForeignKey(to="relation_project", on_delete=models.CASCADE)
    label = models.CharField(max_length=255, null=False)
    value = models.FloatField(max_length=255, null=False)
    time = models.DateTimeField(auto_now_add=True)
    sort = models.IntegerField(default=1)


class garbage_element(models.Model):
    year = models.CharField(max_length=255)
    cook = models.CharField(max_length=200, default='')
    paper = models.CharField(max_length=200, default='')
    plastic = models.CharField(max_length=200, default='')
    clothe = models.CharField(max_length=200, default='')
    wood = models.CharField(max_length=200, default='')
    ash = models.CharField(max_length=200, default='')
    china = models.CharField(max_length=200, default='')
    glass = models.CharField(max_length=200, default='')
    metal = models.CharField(max_length=200, default='')
    other = models.CharField(max_length=200, default='')
    city_id = models.ForeignKey(to="City", on_delete=models.CASCADE)


class garbage_clear(models.Model):
    year = models.CharField(max_length=200, default='')
    wet = models.CharField(max_length=200, default='')
    dry = models.CharField(max_length=200, default='')
    recycle = models.CharField(max_length=200, default='')
    harm = models.CharField(max_length=200, default='')
    total = models.CharField(max_length=200, default='')
    city = models.ForeignKey(to="City", on_delete=models.CASCADE)


class Img(models.Model):
    img_url = models.ImageField("图片", upload_to="static/img")


class File(models.Model):
    file_url = models.FileField("文件", upload_to="static/file/%Y/%m/%d")


class ModelLSTMFile(models.Model):
    file_url = models.FileField("文件", upload_to="static/modelfile/lstm/%Y/%m/%d")


class ModelLinearRegressionFile(models.Model):
    file_url = models.FileField("文件", upload_to="static/modelfile/linearregression/%Y/%m/%d")


class ModelRegressionFile(models.Model):
    file_url = models.FileField("文件", upload_to="static/modelfile/regression/%Y/%m/%d")


class ModelKmeansFile(models.Model):
    file_url = models.FileField("文件", upload_to="static/modelfile/kmeans/%Y/%m/%d")

class ModelsvmFile(models.Model):
    file_url = models.FileField("文件", upload_to="static/modelfile/svm/%Y/%m/%d")

class ModelxgboostFile(models.Model):
    file_url = models.FileField("文件", upload_to="static/modelfile/xgboost/%Y/%m/%d")

class ModelRelationFile(models.Model):
    file_url = models.FileField("文件", upload_to="static/modelfile/relation/%Y/%m/%d")


class TestFile(models.Model):
    file_url = models.FileField("文件", upload_to="static/testfile/%Y/%m/%d")


class Experiment_Result_Excel(models.Model):
    user = models.ForeignKey(to="UserProfile", on_delete=models.CASCADE)
    url = models.CharField(max_length=255, default='')


class GarbageIron(models.Model):
    city = models.ForeignKey(to="City", on_delete=models.CASCADE)
    year = models.CharField(max_length=255, default='')
    produce = models.CharField(max_length=255, default='')


class Garbage_Info_Country(models.Model):
    name = models.CharField(max_length=255, default='', null=False)
    production = models.CharField(max_length=255, default='', null=False)
    district = models.ForeignKey(to="District", on_delete=models.CASCADE)
    year = models.CharField(max_length=255, null=False)
    longitude = models.FloatField()
    latitude = models.FloatField()


class Economy_Info_District(models.Model):
    year = models.CharField(max_length=255, null=False)
    gdp = models.CharField(max_length=255, default='')
    gdp_first_industry = models.CharField(max_length=255, default='')
    gdp_second_industry = models.CharField(max_length=255, default='')
    gdp_third_industry = models.CharField(max_length=255, default='')
    district = models.ForeignKey(to="District", on_delete=models.CASCADE)


class Population_Info_District(models.Model):
    year = models.CharField(max_length=255, null=False)
    population = models.CharField(max_length=255, null=False)
    population_density = models.CharField(max_length=255, null=False)
    district = models.ForeignKey(to="District", on_delete=models.CASCADE)


class LinearRegression(models.Model):
    project_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    table_size = models.IntegerField(default=0)
    status = models.CharField(max_length=255, default='未运行')


class LinearRegressionResult(models.Model):
    project_id = models.ForeignKey(to="LinearRegression", on_delete=models.CASCADE)
    pred = models.FloatField(null=False)
    real = models.FloatField(null=False)
    time = models.DateTimeField(auto_now_add=True)
    sort = models.IntegerField(default=1)


class Grey_Relation_Result(models.Model):
    project_id = models.ForeignKey(to="relation_project", on_delete=models.CASCADE)
    label = models.CharField(max_length=255, null=False)
    garbage_clear = models.FloatField()
    population = models.FloatField()
    ratio_city_rural = models.FloatField()
    household = models.FloatField()
    people_per_capita = models.FloatField()
    ratio_sex = models.FloatField()
    age_0_14 = models.FloatField()
    age_15_64 = models.FloatField()
    age_65 = models.FloatField()
    disposable_income = models.FloatField()
    consume_cost = models.FloatField()
    public_cost = models.FloatField()
    gdp = models.FloatField()
    gdp_first_industry = models.FloatField()
    gdp_second_industry = models.FloatField()
    gdp_third_industry = models.FloatField()
    gnp = models.FloatField()
    education = models.FloatField()
    sort = models.IntegerField(default=1)
    time = models.DateTimeField(auto_now_add=True)


class PearsonResult(models.Model):
    project_id = models.ForeignKey(to="relation_project", on_delete=models.CASCADE)
    label = models.CharField(max_length=255, null=False)
    relate = models.FloatField()
    pvalue = models.FloatField()
    sort = models.IntegerField(default=1)
    time = models.DateTimeField(auto_now_add=True)


class TestReport(models.Model):
    algorithm = models.CharField(max_length=255, default='', null=False)
    project_id = models.CharField(max_length=200, default='', null=False)
    sort = models.IntegerField(default=1, null=False)
    formula = models.TextField(default='')
    r_square = models.CharField(max_length=255, default='')
    mse = models.CharField(max_length=255, default='')
    rmse = models.CharField(max_length=255, default='')
    mae = models.CharField(max_length=255, default='')
    choose_col = models.TextField(default='')


class Garbage_District(models.Model):
    year = models.CharField(max_length=200)
    garbage = models.CharField(max_length=255, default='', null=False)
    district = models.ForeignKey(to="District", on_delete=models.CASCADE)


