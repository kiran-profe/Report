# Generated by Django 4.2 on 2023-04-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_fitnessreport_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('running_time', models.DateTimeField(auto_now_add=True)),
                ('jogging_time', models.DateTimeField(auto_now_add=True)),
                ('exercise_time', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'fitness',
                'verbose_name_plural': 'fitness',
                'db_table': 'fitness',
            },
        ),
    ]