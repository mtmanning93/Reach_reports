from . import models
from django import forms
from datetime import date
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
import re


class CommentForm(forms.ModelForm):
    """
    A form for the comments, for authenticated users, found in report details.
    """
    class Meta:
        model = models.Comment
        fields = ('content',)


class CreateReportForm(forms.ModelForm):
    """
    The form for creating a report.
    Also used in the edit_report view with prepopulated fields.
    """
    class Meta:
        model = models.Report
        fields = [
            'title',
            'start_date',
            'end_date',
            'time_taken',
            'goal_reached',
            'height_in_meters',
            'overall_conditions',
            'activity_category',
            'description',
            'number_in_group',
            'number_on_route',
            'gps_map_link',
            'status',
        ]

    def __init__(self, *args, **kwargs):
        super(CreateReportForm, self).__init__(*args, **kwargs)

        self.fields['title'] = forms.CharField(
            label="Route Name", initial="e.g. Eiger, Heckmair")
        self.fields['goal_reached'].label = "Goal achieved?"
        self.fields['start_date'] = forms.DateField(
            widget=forms.DateInput(
                attrs={'type': 'date', 'max': str(date.today())}),
        )
        self.fields['end_date'] = forms.DateField(
            widget=forms.DateInput(
                attrs={'type': 'date', 'max': str(date.today())}),
        )
        self.fields['end_date'].validators.append(self.validate_end_date)
        self.fields['height_in_meters'].label = "Summit height (masl)"
        self.fields['status'].label = "Publish/ Draft"
        self.fields['gps_map_link'].required = False
        self.fields['time_taken'].validators.append(self.validate_time_taken)

    def validate_time_taken(self, time_taken):
        time_taken = self.data.get('time_taken')
        if not re.match(r'^\d{2}:\d{2}:\d{2}$', time_taken):
            raise forms.ValidationError("Invalid time format. Use hh:mm:ss.")

        return time_taken

    def validate_end_date(self, value):
        start_date = self.cleaned_data.get('start_date')
        if value and start_date and value < start_date:
            raise forms.ValidationError(
                "End date cannot be before start date.")
        return value


class ImageFileForm(forms.ModelForm):
    """
    The form to handle image file uploads within the create report template.
    """
    class Meta:
        model = models.ImageFile
        fields = ['image_file']


class UpdateAccountForm(UserChangeForm):
    """
    Form used for updated account information; username and email.
    """

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields.pop('password')
        self.fields['username'].label = "Update Username"
        self.fields['email'].label = "Update Email"
