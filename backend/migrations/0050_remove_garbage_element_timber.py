# Generated by Django 2.2.7 on 2020-09-28 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0049_auto_20200928_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garbage_element',
            name='timber',
        ),
    ]
