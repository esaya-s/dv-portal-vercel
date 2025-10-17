from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import FAQ, Announcement, ContactMessage
from .forms import ContactForm


class HomeView(TemplateView):
    """Homepage view"""
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcements'] = Announcement.objects.filter(is_active=True).order_by('-created_at')[:3]
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    """Admin dashboard view"""
    template_name = 'core/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get applications data if the applications app is installed
        try:
            from applications.models import DVApplication
            context['applications'] = DVApplication.objects.all().order_by('-created_at')[:10]
            context['total_applications'] = DVApplication.objects.count()
            context['pending_applications'] = DVApplication.objects.filter(status='pending').count()
            context['approved_applications'] = DVApplication.objects.filter(status='approved').count()
            context['rejected_applications'] = DVApplication.objects.filter(status='rejected').count()
        except ImportError:
            context['applications'] = []
            context['total_applications'] = 0
            context['pending_applications'] = 0
            context['approved_applications'] = 0
            context['rejected_applications'] = 0
        
        return context


class AboutView(TemplateView):
    """About page view"""
    template_name = 'core/about.html'


class ContactView(FormView):
    """Contact page with form"""
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:contact_success')
    
    def form_valid(self, form):
        # Create contact message
        contact_message = ContactMessage.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data.get('phone', ''),
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message']
        )
        
        # Send notification to admin panel
        try:
            from notifications.models import AdminNotification
            AdminNotification.objects.create(
                title=f"New Contact Message: {contact_message.subject}",
                message=f"From: {contact_message.name} ({contact_message.email})\nPhone: {contact_message.phone}\n\nMessage: {contact_message.message}",
                application=None
            )
        except Exception as e:
            # Log error but don't fail the form submission
            print(f"Failed to create admin notification: {e}")
        
        # Send Telegram notification to admin
        try:
            from notifications.telegram_bot import send_contact_notification_to_admin
            send_contact_notification_to_admin(contact_message)
        except Exception as e:
            # Log error but don't fail the form submission
            print(f"Failed to send Telegram notification: {e}")
        
        messages.success(self.request, 'Your message has been sent successfully. We will get back to you soon.')
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    """Contact success page"""
    template_name = 'core/contact_success.html'


class FAQView(ListView):
    """FAQ page view"""
    template_name = 'core/faq.html'
    model = FAQ
    context_object_name = 'faqs'
    
    def get_queryset(self):
        return FAQ.objects.filter(is_active=True).order_by('order')


class InstructionsView(TemplateView):
    """Instructions page view"""
    template_name = 'core/instructions.html'


class EligibilityView(TemplateView):
    """Eligibility page view"""
    template_name = 'core/eligibility.html'