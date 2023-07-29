from . import views
from django.urls import path


urlpatterns = [
    path('reports/', views.ReportList.as_view(), name='reports'),
    path('report/<int:pk>/', views.report_details, name='report_details'),
    path('account/', views.account_view, name='account'),
    path('create_report/', views.create_report_view, name='create_report'),
    path('edit_report/<int:pk>/', views.edit_report, name='edit_report'),
    path('delete/<int:pk>/', views.delete_report, name='delete'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('like/<int:pk>/', views.like_report, name='like_report'),
    path('update_account/', views.UpdateAccountView.as_view(), name='update_account'),
]
