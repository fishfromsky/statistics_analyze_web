# Generated by Django 2.2.7 on 2020-10-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0050_remove_garbage_element_timber'),
    ]

    operations = [
        migrations.AddField(
            model_name='lstm_parameter',
            name='gdp_growth_rate',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='lstm_parameter',
            name='natural_growth_rate',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='lstm_parameter',
            name='unemployment_rate',
            field=models.FloatField(default=0, max_length=255),
        ),
    ]
