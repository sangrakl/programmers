# Generated by Django 2.0 on 2018-02-17 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_auto_20180217_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='endTime',
            field=models.IntegerField(choices=[(0, '오전'), (1, '오후')]),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startTime',
            field=models.IntegerField(choices=[(0, '오전'), (1, '오후')]),
        ),
    ]
