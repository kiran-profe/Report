# Generated by Django 4.2 on 2023-04-20 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_fitnessreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnessreport',
            name='id',
            field=models.CharField(max_length=128, primary_key=True, serialize=False),
        ),
    ]
