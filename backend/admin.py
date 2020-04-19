from django.contrib import admin
from .models import ModelsList


@admin.register(ModelsList)
class ModelListAdmin(admin.ModelAdmin):
    list_display = ('modelname', 'create_time', 'author', 'reference', 'star')
