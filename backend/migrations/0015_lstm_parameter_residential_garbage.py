# Generated by Django 2.2.7 on 2020-08-21 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_lstm_parameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='lstm_parameter',
            name='residential_garbage',
            field=models.FloatField(default=0.0, max_length=255),
        ),
    ]
