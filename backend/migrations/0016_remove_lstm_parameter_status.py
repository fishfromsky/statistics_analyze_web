# Generated by Django 2.2.7 on 2020-08-21 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_lstm_parameter_residential_garbage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lstm_parameter',
            name='status',
        ),
    ]