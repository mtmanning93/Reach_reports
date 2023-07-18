from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

GRADE_CHOICES = [
    ("bad", "Bad", ),
    ("ok", "OK", ),
    ("good", "Good", ),
    ("perfect", "Perfect"),
]

CATEGORY_CHOICES = [
    ('alpine', 'Alpine'),
    ('hike', 'Hike'),
    ('skitour', 'Ski Tour'),
    ('iceclimbing', 'Ice Climbing'),
    ('multipitch', 'Multi-Pitch'),
    ('trad', 'Trad'),
    ('solo', 'Solo'),
    ('other', 'Other'),
]

STATUS = ((0, "Draft"), (1, "Published"))

# SUCCESS = [
#     ("yes", "Goal Reached"),
#     ("no", "Goal Not Reached"),
# ]


class Report(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reports")
    created_on = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    # goal_reached = models.CharField(max_length=17, choices=SUCCESS)
    # height_in_meters = models.PositiveIntegerField(
    #     default='',
    #     validators=[MinValueValidator(1), MaxValueValidator(9000)])
    time_taken = models.DurationField(
        null=True, blank=True,
        help_text="""
            If necessary (speed ascent) please use the following format:
            HH:MM:SS.
            """)
    overall_conditions = models.CharField(max_length=7, choices=GRADE_CHOICES)
    activity_category = models.CharField(
        max_length=12, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    number_in_group = models.IntegerField(default=1)
    number_on_route = models.IntegerField(default=1)
    gps_map_link = models.URLField(blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(
        User, related_name='report_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class ImageFile(models.Model):
    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, related_name='images')
    image_file = CloudinaryField('image', default='placeholder')


class Comment(models.Model):
    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.content} by {self.name}"
