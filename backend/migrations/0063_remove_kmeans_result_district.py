# Generated by Django 2.2.7 on 2020-10-21 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0062_kmeans_result_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kmeans_result',
            name='district',
        ),
    ]