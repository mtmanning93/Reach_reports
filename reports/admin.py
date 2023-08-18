from django.contrib import admin
from .models import Report, Comment, ImageFile
from django_summernote.admin import SummernoteModelAdmin


class ImageInline(admin.TabularInline):
    model = ImageFile


@admin.register(Report)
class ReportAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'activity_category',
        'author',
        'start_date'
    )
    search_fields = ['title', 'description']
    list_filter = ('overall_conditions', 'start_date', 'created_on')
    summernote_fields = ('description')
    inlines = [ImageInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'content',
        'report',
        'created_on',
        'approved',)
    list_filter = ('approved', 'created_on',)
    search_fields = ['name', 'email', 'content']
    actions = ['toggle_approval']

    def toggle_approval(self, request, queryset):
        queryset.update(approved=False)
