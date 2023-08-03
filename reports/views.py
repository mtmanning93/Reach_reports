from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, UpdateView
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
import cloudinary
import random
from . import forms
from .models import Report, Comment, ImageFile


def get_random_images():
    """
    Stores the images to be used on the landing page 'index.html'.
    Randomises the image returned, each time function is run.
    """

    images = [
        "images/lagginhorn-header.jpg",
        "images/steep_snow.jpg",
        "images/ridge_scramble.jpg",
        "images/hiking.jpg",
        "images/ice_climbing.jpg",
        "images/skiing.jpg",
        "images/climbing.jpg",
    ]

    return random.choice(images)


def get_landing_page(request):
    """
    Renders landing page template and random image to display
    """

    random_image_url = get_random_images()

    return render(
        request, 'index.html', {'random_image_url': random_image_url})


class ReportList(ListView):
    """
    Renders entire reports list in pages of 10 reports.
    """

    model = Report
    template_name = 'reports.html'
    paginate_by = 10

    def get_queryset(self):
        """
        Filters reports list to display reports in selected category.
        """
        queryset = super().get_queryset()
        selected_activity = self.request.GET.get('activity', 'all')
        selected_grade = self.request.GET.get('grade', 'all')

        if selected_activity == 'all' and selected_grade == 'all':
            queryset = queryset.filter(
                status=1
                ).order_by('-start_date')
        elif selected_activity == 'all':
            queryset = queryset.filter(
                status=1,
                overall_conditions=selected_grade
                ).order_by('-start_date')
        elif selected_grade == 'all':
            queryset = queryset.filter(
                status=1,
                activity_category=selected_activity
                ).order_by('-start_date')
        else:
            queryset = queryset.filter(
                status=1,
                activity_category=selected_activity,
                overall_conditions=selected_grade
                ).order_by('-start_date')

        return queryset


def report_details(request, pk):
    """
    Renders selected report details.
    Displays comment form below details and enables commenting and liking.
    """
    report = get_object_or_404(Report, pk=pk)
    comments = Comment.objects.filter(report=report).order_by('created_on')
    likes_count = report.likes.count()

    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.report = report
            comment.name = request.user.username
            comment.save()

            messages.add_message(
                request, messages.SUCCESS, 'Commented Succesfully')
            return redirect('report_details', pk=pk)
    else:
        comment_form = forms.CommentForm()

    context = {
            'report': report,
            'comments': comments,
            'commented': False,
            'likes_count': likes_count,
            'comment_form': comment_form,
        }
    return render(request, 'report_details.html', context)


def like_report(request, pk):
    """
    Provides like and unlike functionality on each report.
    """
    if request.method == 'POST':
        report = get_object_or_404(Report, pk=pk)

        if request.user.is_authenticated:
            if report.likes.filter(id=request.user.id).exists():
                report.likes.remove(request.user)
            else:
                report.likes.add(request.user)

    return HttpResponseRedirect(reverse('report_details', args=[pk]))


def delete_comment(request, pk):
    """
    Deletes selected comment from database and displays confirmation.
    """
    comment = get_object_or_404(Comment, pk=pk)
    report_pk = comment.report.pk

    if request.method == 'POST':
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Comment deleted successfully!')

        return redirect('report_details', pk=report_pk)


@login_required
def account_view(request):
    """
    Renders account.html template for authenticated users.
    Context is relevant to user instance.
    """
    context = {}

    if request.user.is_authenticated:
        user = request.user

        context = {
            'username': user.username,
            'email': user.email,
            'reports': Report.objects.filter(author=user),
            'image_count': ImageFile.objects.filter(
                report__author=user).count(),
        }

    return render(request, 'account.html', context)


class UpdateAccountView(UpdateView):
    """
    Updates account information, username, email.
    """
    template_name = 'update_account.html'
    form_class = forms.UpdateAccountForm
    success_url = reverse_lazy('account')

    def get_object(self):
        """
        Gets correct user instance.
        """
        return self.request.user

    def form_valid(self, form):
        """
        Provides success message when valid UpdateView form.
        """
        messages.success(self.request, 'Your account has been updated!')
        return super().form_valid(form)


def create_report_view(request):
    """
    Renders create report template and form.
    Populates the slug field with title, author and report.pk.
    Allows for multiple image file uploads.
    On form submission, displays success message if form is valid.
    """
    if request.method == 'POST':

        report_form = forms.CreateReportForm(request.POST, request.FILES)
        # input file multiple name
        images = request.FILES.getlist('images')

        if validate_report_creation(images, report_form):
            report = report_form.save(commit=False)
            report.author = request.user
            slug = generate_slug(report.title, report.author, report.pk)
            report.slug = slug
            report.save()

            create_new_images(report, images)

            messages.add_message(
                request, messages.SUCCESS, 'Report created successfully!')

            return redirect('reports')
    else:
        report_form = forms.CreateReportForm()

    return render(request, 'create_report.html', {'report_form': report_form})


def validate_report_creation(images, report_form):
    if len(images) <= 12 and report_form.is_valid():
        return True
    else:
        if len(images) > 12:
            error_msg = "Invalid Input: You can upload a maximum of 12 images."
            report_form.add_error(None, error_msg)
        return False


def generate_slug(title, author, pk):
    return f"{slugify(title)}-{slugify(author)}-{pk}"


def create_new_images(report, new_images):
    """
    Creates new ImageFile object and uploads to cloudinary
    """
    for image in new_images:
        ImageFile.objects.create(
            report=report,
            image_file=image
        )


def edit_report(request, pk):
    """
    Updates report details with valid form. Redirects to 'account'.
    Handles Image updates, deletions, and additions from db.
    """
    report = Report.objects.get(pk=pk)
    curr_images = report.images.all()

    if request.method == 'POST':
        edit_form = forms.CreateReportForm(
            request.POST, request.FILES, instance=report)
        confirm_deletion = request.POST.get('confirm-deletion', 'false')
        new_images = request.FILES.getlist('images')
        delete_these = []

        # Image deletions (confirmed by the user)
        if confirm_deletion == 'true':
            for image in curr_images:
                checkbox_name = f"delete_image_{image.id}"
                if request.POST.get(checkbox_name):
                    delete_these.append(image)
                    delete_image(image)

        if validate_edit_report_image_data(
                new_images, curr_images, delete_these, edit_form):
            report = edit_form.save()
            create_new_images(report, new_images)

            messages.add_message(
                request, messages.INFO, 'Report updated successfully!')
            return redirect('account')
    else:
        edit_form = forms.CreateReportForm(instance=report)

    context = {
        'edit_form': edit_form,
        'images': curr_images,
        'show_modal': False,  # Initially set to False
    }

    return render(request, 'edit_report.html', context)


def validate_edit_report_image_data(
        new_images, curr_images, delete_these, edit_form):

    if (len(new_images) + len(curr_images)) - len(delete_these) > 12:
        error_msg = """
        Invalid Input: You can upload a maximum of 12 images per report."""
        edit_form.add_error(None, error_msg)

        return False

    elif edit_form.is_valid():
        return True

    return False


def delete_image(image):
    """
    Deletes images from cloudinary and db
    """
    cloudinary.api.delete_resources([image.image_file.public_id])
    image.delete()


def delete_report(request, pk):
    """
    Deletes report instances and displays success message.
    Redirects to account page.
    """
    report = get_object_or_404(Report, pk=pk)

    if request.method == 'POST':
        report.delete()
        messages.add_message(
                request, messages.SUCCESS, 'Report deleted successfully!')
        return redirect('account')


def delete_account(request):
    """
    Deletes user instance.
    Displays successful deletion message.
    Redirects user to landing page.
    """
    if request.method == 'POST':
        user = request.user
        user.delete()

        messages.add_message(
                request, messages.SUCCESS, 'Account deleted successfully!')

        return redirect('home')

    return render(request, 'account.html')
