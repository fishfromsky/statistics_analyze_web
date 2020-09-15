# Generated by Django 2.2.7 on 2020-09-01 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_multi_regression'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='multi_regression',
            new_name='multi_regression_project',
        ),
        migrations.CreateModel(
            name='multi_regression_parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resident_population', models.FloatField()),
                ('population_of_density', models.FloatField()),
                ('number_of_households', models.FloatField()),
                ('average_population_per_household', models.FloatField()),
                ('urban_residents_per_capita_disposable_income', models.FloatField()),
                ('consumer_expenditure', models.FloatField()),
                ('general_public_expenditure', models.FloatField()),
                ('investment_in_urban_infrastructure', models.FloatField()),
                ('urban_population_density', models.FloatField()),
                ('greening_coverage', models.FloatField()),
                ('gross_local_product', models.FloatField()),
                ('gross_domestic_product_per_capita', models.FloatField()),
                ('gross_domestic_product_of_the_first_industry', models.FloatField()),
                ('gross_value_of_secondary_industry', models.FloatField()),
                ('gross_value_of_the_tertiary_industry', models.FloatField()),
                ('investment_in_environmental_protection', models.FloatField()),
                ('number_of_college_students', models.FloatField()),
                ('level_of_education', models.FloatField()),
                ('municial_household_garbage', models.FloatField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.multi_regression_project')),
            ],
        ),
    ]