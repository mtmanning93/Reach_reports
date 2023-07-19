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
    list_filter = ('overall_conditions', 'start_date')
    summernote_fields = ('description')
    inlines = [ImageInline]

    # Hide slug...
    exclude = ('slug',)

    # Save slug as...
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            slug = f"{slugify(obj.title)}-{slugify(obj.author)}-{obj.pk}"
            obj.slug = slug

        super().save_model(request, obj, form, change)


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
