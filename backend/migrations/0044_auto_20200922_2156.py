# Generated by Django 2.2.7 on 2020-09-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0043_auto_20200922_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='population_info_city',
            name='average_person_per_household',
            field=models.FloatField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='population_info_city',
            name='households',
            field=models.FloatField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='population_info_city',
            name='population',
            field=models.FloatField(default=0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='population_info_city',
            name='population_density',
            field=models.FloatField(default=0, max_length=200, null=True),
        ),
    ]
