# Generated by Django 2.2.7 on 2020-09-01 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_lstm_result_sort'),
    ]

    operations = [
        migrations.CreateModel(
            name='multi_regression',
            fields=[
                ('project_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('table_size', models.IntegerField(default=0)),
                ('status', models.CharField(default='未运行', max_length=255)),
            ],
        ),
    ]
