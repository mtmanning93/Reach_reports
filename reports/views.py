from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib import messages
import cloudinary
from .models import Report, Comment, ImageFile
from .forms import CommentForm, CreateReportForm, ImageFileForm
import random


def get_random_images():

    images = [
        "/static/images/lagginhorn-header.jpg",
        "/static/images/steep_snow.jpg",
        "/static/images/ridge_scramble.jpg",
        "/static/images/hiking.jpg",
        "/static/images/ice_climbing.jpg",
        "/static/images/skiing.jpg",
        "/static/images/climbing.jpg",
    ]

    return random.choice(images)


def get_landing_page(request):
    random_image_url = get_random_images()

    return render(
        request, 'index.html', {'random_image_url': random_image_url})


class ReportList(generic.ListView):
    model = Report
    queryset = Report.objects.filter(status=1).order_by('-start_date')
    template_name = 'reports.html'
    paginate_by = 10


def report_details(request, pk):
    report = get_object_or_404(Report, pk=pk)
    comments = Comment.objects.filter(report=report).order_by('created_on')
    likes_count = report.likes.count()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.report = report
            comment.name = request.user.username
            comment.save()

            messages.add_message(
                request, messages.SUCCESS, 'Commented Succesfully')
            return redirect('report_details', pk=pk)
    else:
        comment_form = CommentForm()

    context = {
            'report': report,
            'comments': comments,
            'commented': False,
            'likes_count': likes_count,
            'comment_form': comment_form,
        }
    return render(request, 'report_details.html', context)


def like_report(request, pk):
    if request.method == 'POST':
        report = get_object_or_404(Report, pk=pk)

        if request.user.is_authenticated:
            if report.likes.filter(id=request.user.id).exists():
                report.likes.remove(request.user)
            else:
                report.likes.add(request.user)

    return HttpResponseRedirect(reverse('report_details', args=[pk]))


def account_view(request):
    context = {}

    if request.user.is_authenticated:
        user = request.user
        
        context = {
            'username': user.username,
            'email': user.email,
            'reports': Report.objects.filter(author=user),
        }

    return render(request, 'account.html', context)


def create_report_view(request):
    if request.method == 'POST':
        report_form = CreateReportForm(request.POST, request.FILES)

        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.author = request.user
            slug = f"{slugify(report.title)}\
                -{slugify(report.author)}-{report.pk}"
            report.slug = slug
            report.save()

            # Multiple image files using CloudinaryFileField
            images = request.FILES.getlist('images')

            for image in images:
                ImageFile.objects.create(
                    report=report,
                    image_file=image
                    )

            messages.add_message(
                request, messages.SUCCESS, 'Report created successfully!')

            return redirect('reports')

    else:
        report_form = CreateReportForm()

    return render(request, 'create_report.html', {'report_form': report_form})


def edit_report(request, pk):
    report = Report.objects.get(pk=pk)
    edit_form = None
    images = report.images.all()
    images_to_delete = []

    if request.method == 'POST':
        confirm_deletion = request.POST.get('confirm-deletion', 'false')

        if confirm_deletion == 'true':
            # Handle image deletions (confirmed by the user)
            for image in report.images.all():
                checkbox_name = f"delete_image_{image.id}"
                if request.POST.get(checkbox_name):
                    images_to_delete.append(image.id)
                    cloudinary.api.delete_resources(
                        [image.image_file.public_id])
                    image.delete()

            # Continue with form validation and saving
            edit_form = CreateReportForm(
                request.POST, request.FILES, instance=report)

            if edit_form.is_valid():
                report = edit_form.save()

                images = request.FILES.getlist('images')

                for image in images:
                    ImageFile.objects.create(
                        report=report,
                        image_file=image
                    )

                messages.add_message(
                    request, messages.INFO,
                    'Report updated successfully and images have been deleted!'
                    )

                return redirect('account')
            else:
                context = {
                    'edit_form': edit_form,
                    'images': images,
                    'show_modal': True,
                }
                return render(request, 'edit_report.html', context)

        # If confirm-deletion is not true
        edit_form = CreateReportForm(
            request.POST, request.FILES, instance=report)

        if edit_form.is_valid():
            report = edit_form.save()

            images = request.FILES.getlist('images')

            for image in images:
                ImageFile.objects.create(
                    report=report,
                    image_file=image
                )

            messages.add_message(
                request, messages.INFO, 'Report updated successfully!')

            return redirect('account')

    else:
        edit_form = CreateReportForm(instance=report)

    context = {
        'edit_form': edit_form,
        'images': images,
        'show_modal': False,  # Initially set to False
    }

    return render(request, 'edit_report.html', context)


def delete_report(request, pk):
    report = get_object_or_404(Report, pk=pk)

    if request.method == 'POST':
        report.delete()
        messages.add_message(
                request, messages.SUCCESS, 'Report deleted successfully!')
        return redirect('account')

    return redirect('account')


def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()

        messages.add_message(
                request, messages.SUCCESS, 'Account deleted successfully!')

        return redirect('home')

    return render(request, 'account.html')
