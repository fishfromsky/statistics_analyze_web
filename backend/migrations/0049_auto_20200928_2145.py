# Generated by Django 2.2.7 on 2020-09-28 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0048_garbage_element_city_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='garbage_element',
            old_name='clay',
            new_name='china',
        ),
    ]
