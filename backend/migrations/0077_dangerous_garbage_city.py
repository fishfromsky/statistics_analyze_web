# Generated by Django 2.2.7 on 2020-11-05 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0076_auto_20201105_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dangerous_Garbage_City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=200)),
                ('production', models.CharField(default='', max_length=200)),
                ('deal', models.CharField(default='', max_length=200)),
                ('use', models.CharField(default='', max_length=200)),
                ('store', models.CharField(default='', max_length=200)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.City')),
            ],
        ),
    ]