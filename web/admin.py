from __future__ import unicode_literals
from django.contrib import admin
from web.models import FitnessReport
from web.forms import FitnessForm
from import_export.admin import ImportExportModelAdmin


class FitnessAdmin(admin.ModelAdmin):
    list_display = ('is_deleted', 'running_time', 'jogging_time',
                    'exercise_time')


admin.site.register(FitnessReport, FitnessAdmin)
