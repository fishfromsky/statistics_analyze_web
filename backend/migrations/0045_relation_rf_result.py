# Generated by Django 2.2.7 on 2020-09-22 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0044_auto_20200922_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='relation_RF_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('value', models.FloatField(max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('sort', models.IntegerField(default=1)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.relation_project')),
            ],
        ),
    ]
