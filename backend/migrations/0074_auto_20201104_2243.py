# Generated by Django 2.2.7 on 2020-11-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0073_auto_20201104_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gargabe_deal_city',
            name='collect_factory_num',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='gargabe_deal_city',
            name='compost',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='gargabe_deal_city',
            name='else_num',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='gargabe_deal_city',
            name='factory_num_total',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='gargabe_deal_city',
            name='incineration',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='gargabe_deal_city',
            name='landFill',
            field=models.CharField(default='', max_length=255),
        ),
    ]
