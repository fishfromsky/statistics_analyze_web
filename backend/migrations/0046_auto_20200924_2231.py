# Generated by Django 2.2.7 on 2020-09-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0045_relation_rf_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='economy_info_city',
            old_name='unemployment_rate',
            new_name='gdp_first_industry',
        ),
        migrations.AddField(
            model_name='economy_info_city',
            name='gdp_second_industry',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='economy_info_city',
            name='gdp_third_industry',
            field=models.FloatField(null=True),
        ),
    ]
