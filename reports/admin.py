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
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title', 'author', 'created_on',)}
    list_filter = ('overall_conditions', 'created_on', 'start_date')
    summernote_fields = ('description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'content',
        'report',
        'created_on')
    list_filter = ('approved', 'created_on',)
    search_fields = ['name', 'email', 'content']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
