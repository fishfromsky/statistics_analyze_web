# Generated by Django 2.2.7 on 2020-09-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_multi_regression_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lstm_project',
            name='table_size',
            field=models.IntegerField(default=0),
        ),
    ]