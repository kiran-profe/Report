# Generated by Django 4.2 on 2023-04-20 08:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('running_time', models.DateTimeField(auto_now_add=True)),
                ('jogging_time', models.DateTimeField(auto_now_add=True)),
                ('exercise_time', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'report',
                'verbose_name_plural': 'reportes',
                'db_table': 'report',
            },
        ),
    ]
