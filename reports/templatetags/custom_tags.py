from django import template
from django.contrib.auth.models import User
from reports.models import Comment

register = template.Library()


@register.simple_tag
def count_user_comments(user):
    return Comment.objects.filter(report__author=user).count()
