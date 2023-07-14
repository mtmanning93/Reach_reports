from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
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
    if request.user.is_authenticated:
        user = request.user
        context = {
            'username': user.username,
            'email': user.email,
        }

    if request.method == 'POST' and 'delete_account' in request.POST:
        user = request.user
        user.delete()
        return redirect(reverse('home'))  # Replace 'home' with the name of your home URL pattern

        return render(request, 'account.html', context)
