from django.contrib import admin
from .models import ModelsList, FactoryList


@admin.register(ModelsList)
class ModelListAdmin(admin.ModelAdmin):
    list_display = ('modelname', 'create_time', 'author', 'reference', 'star')


@admin.register(FactoryList)
class FactoryListAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'longitude', 'latitude', 'deal')
