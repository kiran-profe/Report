# Generated by Django 4.2 on 2023-04-20 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_fitnessreport_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnessreport',
            name='date',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='fitnessreport',
            name='exercise_time',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='fitnessreport',
            name='jogging_time',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='fitnessreport',
            name='running_time',
            field=models.CharField(max_length=128),
        ),
    ]
