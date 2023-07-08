from . import views
from django.urls import path


urlpatterns = [
    path('reports/', views.ReportList.as_view(), name='reports'),
    path('report/<int:pk>/', views.report_details, name='report_details'),
]
