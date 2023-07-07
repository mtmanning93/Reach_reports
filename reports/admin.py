from django.contrib import admin
from .models import Report, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Report)
class ReportAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'activity_category',
        'author',
        'start_date',
        'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', 'author', 'created_on',)}
    list_filter = ('overall_conditions', 'created_on', 'start_date')
    summernote_fields = ('description')



