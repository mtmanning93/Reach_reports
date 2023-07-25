from django import template
from django.contrib.auth.models import User
from reports.models import Comment
from reports.models import ImageFile

register = template.Library()


@register.simple_tag
def count_user_comments(user):
    return Comment.objects.filter(report__author=user).count()


@register.simple_tag
def count_user_images(user):
    return ImageFile.objects.filter(report__author=user).count()
