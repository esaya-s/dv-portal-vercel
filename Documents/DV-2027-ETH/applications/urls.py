from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/', views.application_form_view, name='create'),
    path('apply/simple/', views.ApplicationCreateView.as_view(), name='create_simple'),
    path('success/', views.ApplicationSuccessView.as_view(), name='success'),
    path('status/', views.ApplicationStatusView.as_view(), name='status'),
    path('status/result/', views.ApplicationStatusResultView.as_view(), name='status_result'),
]