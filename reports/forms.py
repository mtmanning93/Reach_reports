from . import models
from django import forms
from datetime import date
from cloudinary.forms import CloudinaryFileField


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('content',)


class CreateReportForm(forms.ModelForm):

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
            'gps_map_link'
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


class ImageFileForm(forms.ModelForm):
    class Meta:
        model = models.ImageFile
        fields = ['image_file']
