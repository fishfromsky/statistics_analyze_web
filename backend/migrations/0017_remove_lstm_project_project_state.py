# Generated by Django 2.2.7 on 2020-08-29 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_remove_lstm_parameter_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lstm_project',
            name='project_state',
        ),
    ]
