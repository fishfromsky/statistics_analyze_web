# Generated by Django 2.2.7 on 2020-08-30 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_delete_lstm_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='lstm_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=255)),
                ('real', models.FloatField()),
                ('pred', models.FloatField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.lstm_project')),
            ],
        ),
    ]