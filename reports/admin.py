from django.contrib import admin
from .models import Report
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Report)
class ReportAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
