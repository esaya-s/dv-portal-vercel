from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.NotificationListView.as_view(), name='list'),
    path('telegram/setup/', views.TelegramSetupView.as_view(), name='telegram_setup'),
    path('telegram/verify/', views.TelegramVerifyView.as_view(), name='telegram_verify'),
    path('settings/', views.NotificationSettingsView.as_view(), name='settings'),
    
    # Webhook for Telegram bot
    path('telegram/webhook/', views.TelegramWebhookView.as_view(), name='telegram_webhook'),
]
