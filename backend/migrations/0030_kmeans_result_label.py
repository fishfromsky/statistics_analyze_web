# Generated by Django 2.2.7 on 2020-09-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0029_kmeans_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='kmeans_result',
            name='label',
            field=models.IntegerField(default=0),
        ),
    ]
