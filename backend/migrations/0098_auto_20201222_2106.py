# Generated by Django 2.2.7 on 2020-12-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0097_modelfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelLSTMFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_url', models.FileField(upload_to='static/modelfile/lstm/%Y/%m/%d', verbose_name='文件')),
            ],
        ),
        migrations.DeleteModel(
            name='ModelFile',
        ),
    ]
