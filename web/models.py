from __future__ import unicode_literals
from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
import os
import uuid


class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    running_time = models.DateTimeField(auto_now_add=True)

    jogging_time = models.DateTimeField(auto_now_add=True)
    exercise_time = models.DateTimeField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'report'
        verbose_name = _('report')
        verbose_name_plural = _('reportes')

    def __str__(self):
        return self.id


class FitnessReport(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    date = models.CharField(max_length=128)
    running_time = models.CharField(max_length=128)

    jogging_time = models.CharField(max_length=128)
    exercise_time = models.CharField(max_length=128)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'fitness report'
        verbose_name = _('fitness report')
        verbose_name_plural = _('fitness reportes')

    def __str__(self):
        return self.id


class Fitness(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    date = models.DateTimeField()
    running_time = models.DateTimeField()

    jogging_time = models.DateTimeField()
    exercise_time = models.DateTimeField()

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'fitness'
        verbose_name = _('fitness')
        verbose_name_plural = _('fitness')

    def __str__(self):
        return self.id
