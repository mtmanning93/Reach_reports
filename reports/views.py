from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Report


def get_landing_page(request):
    return render(request, 'index.html')


class ReportList(generic.ListView):
    model = Report
    queryset = Report.objects.filter(status=1).order_by('-start_date')
    template_name = 'reports.html'
    paginate_by = 10


def report_details(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'report_details.html', {'report': report})
