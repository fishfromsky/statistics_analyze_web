# Generated by Django 2.2.7 on 2020-12-12 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0087_grey_relation_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='PearsonResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('relate', models.FloatField()),
                ('pvalue', models.FloatField()),
                ('sort', models.IntegerField(default=1)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.relation_project')),
            ],
        ),
    ]
