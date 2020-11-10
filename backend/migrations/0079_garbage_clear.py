# Generated by Django 2.2.7 on 2020-11-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0078_auto_20201106_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='garbage_clear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default='', max_length=200)),
                ('wet', models.CharField(default='', max_length=200)),
                ('dry', models.CharField(default='', max_length=200)),
                ('recycle', models.CharField(default='', max_length=200)),
                ('harm', models.CharField(default='', max_length=200)),
                ('total', models.CharField(default='', max_length=200)),
            ],
        ),
    ]