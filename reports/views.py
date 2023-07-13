from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Report, Comment
from .forms import CommentForm


def get_landing_page(request):
    return render(request, 'index.html')


class ReportList(generic.ListView):
    model = Report
    queryset = Report.objects.filter(status=1).order_by('-start_date')
    template_name = 'reports.html'
    paginate_by = 10


def report_details(request, pk):
    report = get_object_or_404(Report, pk=pk)
    comments = Comment.objects.filter(report=report)
    likes_count = report.likes.count()
    return render(
        request,
        'report_details.html',
        {
            'report': report,
            'comments': comments,
            'likes_count': likes_count,
            'comment_form': CommentForm()
        },
    )
