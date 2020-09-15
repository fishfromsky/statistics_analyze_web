# Generated by Django 2.2.7 on 2020-09-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0027_auto_20200902_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='kmeans_project',
            fields=[
                ('project_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='未运行', max_length=255)),
            ],
        ),
    ]