from . import models
from django import forms
from cloudinary.forms import CloudinaryFileField


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('content',)


class CreateReportForm(forms.ModelForm):

    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    images = CloudinaryFileField(
        options={
            'resource_type': 'image',
            'max_files': 10
        },
        required=False
    )

    class Meta:
        model = models.Report
        fields = fields = [
            'title',
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


class ImageFileForm(forms.ModelForm):
    class Meta:
        model = models.ImageFile
        fields = ['image_file']
