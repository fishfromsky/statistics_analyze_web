# Generated by Django 2.2.7 on 2020-11-06 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0079_garbage_clear'),
    ]

    operations = [
        migrations.AddField(
            model_name='garbage_clear',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.City'),
            preserve_default=False,
        ),
    ]
