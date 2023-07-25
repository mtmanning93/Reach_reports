from django import template
from django.contrib.auth.models import User
from reports.models import Comment, ImageFile

register = template.Library()

STATUS_CHOICES = {
    0: 'draft',
    1: 'published',
}


@register.simple_tag
def count_user_comments(user):
    return Comment.objects.filter(report__author=user).count()


@register.simple_tag
def count_user_images(user):
    return ImageFile.objects.filter(report__author=user).count()


@register.filter
def display_status(value):
    return STATUS_CHOICES.get(value, '')
