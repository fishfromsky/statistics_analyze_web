# Generated by Django 2.2.7 on 2020-10-19 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0056_auto_20201019_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img_url',
            field=models.ImageField(upload_to='static/img', verbose_name='图片'),
        ),
    ]