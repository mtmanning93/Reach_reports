from .models import Report, Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class CreateReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = fields = [
            'title',
            'slug',
            'start_date',
            'end_date',
            'time_taken',
            'overall_conditions',
            'activity_category',
            'description',
            'number_in_group',
            'number_on_route',
            'gps_map_link'
        ]
