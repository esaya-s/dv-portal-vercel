from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # Dashboard temporarily shows demo message
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/success/', views.ContactSuccessView.as_view(), name='contact_success'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('instructions/', views.InstructionsView.as_view(), name='instructions'),
    path('eligibility/', views.EligibilityView.as_view(), name='eligibility'),
]
