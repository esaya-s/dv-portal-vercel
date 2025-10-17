from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from .models import TelegramNotification


class NotificationListView(LoginRequiredMixin, ListView):
    """List user's notifications"""
    model = TelegramNotification
    template_name = 'notifications/list.html'
    context_object_name = 'notifications'
    
    def get_queryset(self):
        return TelegramNotification.objects.filter(
            user=self.request.user
        ).order_by('-created_at')


class TelegramSetupView(LoginRequiredMixin, TemplateView):
    """Telegram bot setup instructions"""
    template_name = 'notifications/telegram_setup.html'


class TelegramVerifyView(LoginRequiredMixin, TemplateView):
    """Telegram account verification"""
    template_name = 'notifications/telegram_verify.html'


class NotificationSettingsView(LoginRequiredMixin, TemplateView):
    """Notification settings"""
    template_name = 'notifications/settings.html'


@method_decorator(csrf_exempt, name='dispatch')
class TelegramWebhookView(TemplateView):
    """Telegram bot webhook endpoint"""
    
    def post(self, request, *args, **kwargs):
        # TODO: Implement webhook processing
        # This would handle incoming Telegram messages
        return HttpResponse("OK")
    
    def get(self, request, *args, **kwargs):
        return HttpResponse("Telegram Webhook Endpoint")
