# Generated by Django 2.2.7 on 2020-12-11 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0086_linearregression_linearregressionparameter_linearregressionresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grey_Relation_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('garbage_clear', models.FloatField()),
                ('population', models.FloatField()),
                ('ratio_city_rural', models.FloatField()),
                ('household', models.FloatField()),
                ('people_per_capita', models.FloatField()),
                ('ratio_sex', models.FloatField()),
                ('age_0_14', models.FloatField()),
                ('age_15_64', models.FloatField()),
                ('age_65', models.FloatField()),
                ('disposable_income', models.FloatField()),
                ('consume_cost', models.FloatField()),
                ('public_cost', models.FloatField()),
                ('gdp', models.FloatField()),
                ('gdp_first_industry', models.FloatField()),
                ('gdp_second_industry', models.FloatField()),
                ('gdp_third_industry', models.FloatField()),
                ('gnp', models.FloatField()),
                ('education', models.FloatField()),
                ('sort', models.IntegerField(default=1)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.relation_project')),
            ],
        ),
    ]