# Generated by Django 2.2.7 on 2020-09-07 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0030_kmeans_result_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='kmeans_parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resident_population', models.FloatField(default=None)),
                ('population_of_density', models.FloatField(default=None)),
                ('number_of_households', models.FloatField(default=None)),
                ('average_population_per_household', models.FloatField(default=None)),
                ('urban_residents_per_capita_disposable_income', models.FloatField(default=None)),
                ('consumer_expenditure', models.FloatField(default=None)),
                ('general_public_expenditure', models.FloatField(default=None)),
                ('investment_in_urban_infrastructure', models.FloatField(default=None)),
                ('urban_population_density', models.FloatField(default=None)),
                ('greening_coverage', models.FloatField(default=None)),
                ('gross_local_product', models.FloatField(default=None)),
                ('gross_domestic_product_per_capita', models.FloatField(default=None)),
                ('gross_domestic_product_of_the_first_industry', models.FloatField(default=None)),
                ('gross_value_of_secondary_industry', models.FloatField(default=None)),
                ('gross_value_of_the_tertiary_industry', models.FloatField(default=None)),
                ('investment_in_environmental_protection', models.FloatField(default=None)),
                ('number_of_college_students', models.FloatField(default=None)),
                ('level_of_education', models.FloatField(default=None)),
                ('municial_household_garbage', models.FloatField(default=None)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.kmeans_project')),
            ],
        ),
    ]