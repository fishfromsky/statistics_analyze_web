# Generated by Django 2.2.7 on 2020-12-12 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0090_auto_20201212_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='testreport',
            name='algorithm',
            field=models.CharField(default='', max_length=255),
        ),
    ]
