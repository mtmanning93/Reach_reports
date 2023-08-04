from django.contrib import admin
from django.test import TestCase

from reports.models import Comment
from reports.admin import CommentAdmin


class CommentAdminTest(TestCase):

    def setUp(self):

        self.admin = CommentAdmin(Comment, admin.site)

    def test_approve_comments(self):

        queryset = Comment.objects.none()

        self.admin.approve_comments(None, queryset)
        self.assertFalse(queryset.filter(approved=True).exists())
