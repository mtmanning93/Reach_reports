from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Report, Comment
from .forms import CommentForm, CreateReportForm, ImageFileForm


def get_landing_page(request):
    return render(request, 'index.html')


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
            return redirect('report_details', pk=pk)
    else:
        comment_form = CommentForm()

    return render(
        request,
        'report_details.html',
        {
            'report': report,
            'comments': comments,
            'commented': False,
            'likes_count': likes_count,
            'comment_form': comment_form,
        },
    )


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


def create_report(request):
    if request.method == 'POST':
        form = CreateReportForm(request.POST)
        image_form = ImageFileForm(request.POST, request.FILES)
        if form.is_valid():
            slug = slugify(form.cleaned_data['title'])
            report = form.save(commit=False)
            report.slug = slug
            report.author = request.user
            report.save()

            image_file = image_form.cleaned_data['image_file']
            ImageFile.objects.create(report=report, image_file=image_file)

            return redirect('report_details', pk=report.pk)
    else:
        form = CreateReportForm()
        image_form = ImageFileForm()

    return render(
        request,
        'create_report.html',
        {'report_form': form, 'image_form': image_form})
