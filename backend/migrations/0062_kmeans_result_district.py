# Generated by Django 2.2.7 on 2020-10-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0061_kmeans_parameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='kmeans_result',
            name='district',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
