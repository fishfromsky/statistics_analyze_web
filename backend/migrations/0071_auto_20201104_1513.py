# Generated by Django 2.2.7 on 2020-11-04 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0070_merge_20201104_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='garbage_info_city',
            name='rate_of_treated',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='garbage_info_city',
            name='collect_transport_garbage',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='garbage_info_city',
            name='total_garbage',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='garbage_info_city',
            name='volume_of_treated',
            field=models.CharField(default='', max_length=200),
        ),
    ]