from . import models
from django import forms
from datetime import date
from cloudinary.forms import CloudinaryFileField
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
            'status'
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
        self.fields['height_in_meters'].label = "Summit height (masl)"
        self.fields['images'] = CloudinaryFileField(
            options={
                'resource_type': 'image',
                'max_files': 10
            },
            required=False,
            label="Custom Images Field"
        )
        self.fields['status'].label = "Publish/ Draft"
        self.fields['gps_map_link'].required = False


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
