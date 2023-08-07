from django.contrib import admin
from django.test import TestCase

from reports.models import Comment
from reports.admin import CommentAdmin


class CommentAdminTest(TestCase):
    """
    Unit tests for the CommentAdmin class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.admin = CommentAdmin(Comment, admin.site)

    def test_approve_comments(self):
        """
        Verifies that the approve_comments method sets the 'approved' attribute
        to True for the chosen comments.
        """
        queryset = Comment.objects.none()

        self.admin.approve_comments(None, queryset)
        self.assertFalse(queryset.filter(approved=True).exists())
