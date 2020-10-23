# Generated by Django 2.2.7 on 2020-10-20 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0060_delete_kmeans_parameter'),
    ]

    operations = [
        migrations.CreateModel(
            name='kmeans_parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=255)),
                ('en_name', models.CharField(max_length=255)),
                ('range', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('msw', models.FloatField()),
                ('pop', models.FloatField()),
                ('pup', models.FloatField()),
                ('hou', models.FloatField()),
                ('aph', models.FloatField()),
                ('gen', models.FloatField()),
                ('age1', models.FloatField()),
                ('age2', models.FloatField()),
                ('age3', models.FloatField()),
                ('inc', models.FloatField()),
                ('exp', models.FloatField()),
                ('bud', models.FloatField()),
                ('gdp', models.FloatField()),
                ('gdp1', models.FloatField()),
                ('gdp2', models.FloatField()),
                ('gdp3', models.FloatField()),
                ('pgdp', models.FloatField()),
                ('edu', models.FloatField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.kmeans_project')),
            ],
        ),
    ]
