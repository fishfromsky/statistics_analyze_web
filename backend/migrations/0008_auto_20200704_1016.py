# Generated by Django 2.2.7 on 2020-07-04 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_basic_cost_matrix_p_median_project_rrc_ts'),
    ]

    operations = [
        migrations.AddField(
            model_name='factorylist',
            name='type',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='factorylist',
            name='typeId',
            field=models.IntegerField(default=0),
        ),
    ]
