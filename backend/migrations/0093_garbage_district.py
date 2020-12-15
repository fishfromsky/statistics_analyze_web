# Generated by Django 2.2.7 on 2020-12-14 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0092_testreport_choose_col'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garbage_District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=200)),
                ('garbage', models.CharField(default='', max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.District')),
            ],
        ),
    ]
