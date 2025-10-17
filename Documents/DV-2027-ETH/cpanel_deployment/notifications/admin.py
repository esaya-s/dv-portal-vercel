from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import render
from django.db.models import Count, Q
from .models import BotCommand, TelegramUser, TelegramNotification, AdminNotification
from applications.models import DVApplication


@admin.register(BotCommand)
class BotCommandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'chat_id', 'first_name', 'last_name', 'is_admin', 'is_blocked', 'created_at')
    list_filter = ('is_admin', 'is_blocked', 'created_at')
    search_fields = ('username', 'chat_id', 'first_name', 'last_name')
    readonly_fields = ('chat_id', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Telegram Information', {
            'fields': ('chat_id', 'username', 'first_name', 'last_name')
        }),
        ('Status', {
            'fields': ('is_admin', 'is_blocked')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(TelegramNotification)
class TelegramNotificationAdmin(admin.ModelAdmin):
    list_display = ('telegram_user', 'application', 'sent', 'created_at', 'sent_at')
    list_filter = ('sent', 'created_at')
    raw_id_fields = ('telegram_user', 'application')
    search_fields = ('message', 'telegram_user__username', 'application__dv_id')
    readonly_fields = ('created_at', 'sent_at')
    ordering = ('-created_at',)


@admin.register(AdminNotification)
class AdminNotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'application', 'is_read', 'created_at', 'read_at')
    list_filter = ('is_read', 'created_at')
    raw_id_fields = ('user', 'application')
    search_fields = ('title', 'message')
    readonly_fields = ('created_at', 'read_at')
    ordering = ('-created_at',)


# Custom admin view for Telegram bot analytics
class TelegramBotAnalyticsAdmin(admin.AdminSite):
    site_header = "Telegram Bot Analytics"
    site_title = "Bot Analytics"
    index_title = "Telegram Bot User Management"

    def index(self, request, extra_context=None):
        # Get statistics
        total_users = TelegramUser.objects.count()
        active_users = TelegramUser.objects.filter(is_blocked=False).count()
        admin_users = TelegramUser.objects.filter(is_admin=True).count()
        blocked_users = TelegramUser.objects.filter(is_blocked=True).count()
        
        # Get users with applications
        users_with_apps = TelegramUser.objects.filter(
            chat_id__in=DVApplication.objects.exclude(telegram_chat_id__isnull=True).values_list('telegram_chat_id', flat=True)
        ).count()
        
        # Recent activity
        recent_users = TelegramUser.objects.order_by('-created_at')[:10]
        recent_notifications = TelegramNotification.objects.order_by('-created_at')[:10]
        
        # Application status distribution
        app_status_stats = DVApplication.objects.values('status').annotate(count=Count('status'))
        
        context = {
            'total_users': total_users,
            'active_users': active_users,
            'admin_users': admin_users,
            'blocked_users': blocked_users,
            'users_with_apps': users_with_apps,
            'recent_users': recent_users,
            'recent_notifications': recent_notifications,
            'app_status_stats': app_status_stats,
        }
        
        return render(request, 'admin/telegram_bot_analytics.html', context)


# Create a custom admin view for bot users
class BotUsersAdminView:
    def __init__(self):
        self.site = TelegramBotAnalyticsAdmin(name='bot_analytics')
    
    def get_urls(self):
        return [
            path('bot-analytics/', self.site.index, name='bot_analytics'),
        ]


# Add bot analytics to the main admin
admin.site.site_header = "DV-2027 Ethiopia Portal Administration"
admin.site.site_title = "DV-2027 Admin"
admin.site.index_title = "Welcome to DV-2027 Administration"