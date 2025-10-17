from django.core.management.base import BaseCommand
from django.shortcuts import render
from django.db.models import Count
from notifications.models import TelegramUser, TelegramNotification
from applications.models import DVApplication

class Command(BaseCommand):
    help = 'Display Telegram bot analytics in the terminal'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🤖 Telegram Bot Analytics'))
        self.stdout.write('=' * 50)
        
        # Get statistics
        total_users = TelegramUser.objects.count()
        active_users = TelegramUser.objects.filter(is_blocked=False).count()
        admin_users = TelegramUser.objects.filter(is_admin=True).count()
        blocked_users = TelegramUser.objects.filter(is_blocked=True).count()
        
        # Get users with applications
        users_with_apps = TelegramUser.objects.filter(
            chat_id__in=DVApplication.objects.exclude(telegram_chat_id__isnull=True).values_list('telegram_chat_id', flat=True)
        ).count()
        
        # Application status distribution
        app_status_stats = DVApplication.objects.values('status').annotate(count=Count('status'))
        
        # Display statistics
        self.stdout.write(f'👥 Total Telegram Users: {total_users}')
        self.stdout.write(f'✅ Active Users: {active_users}')
        self.stdout.write(f'👑 Admin Users: {admin_users}')
        self.stdout.write(f'🚫 Blocked Users: {blocked_users}')
        self.stdout.write(f'📝 Users with Applications: {users_with_apps}')
        
        self.stdout.write('\n📊 Application Status Distribution:')
        for stat in app_status_stats:
            self.stdout.write(f'  • {stat["status"].title()}: {stat["count"]}')
        
        # Recent users
        self.stdout.write('\n👥 Recent Telegram Users:')
        recent_users = TelegramUser.objects.order_by('-created_at')[:5]
        for user in recent_users:
            status = 'Admin' if user.is_admin else 'Blocked' if user.is_blocked else 'Active'
            username = f'@{user.username}' if user.username else 'No username'
            self.stdout.write(f'  • {username} ({user.first_name} {user.last_name}) - {status}')
        
        # Recent notifications
        self.stdout.write('\n📨 Recent Notifications:')
        recent_notifications = TelegramNotification.objects.order_by('-created_at')[:5]
        for notif in recent_notifications:
            status = '✓ Sent' if notif.sent else '✗ Failed'
            user_info = f'@{notif.telegram_user.username}' if notif.telegram_user and notif.telegram_user.username else 'Unknown'
            self.stdout.write(f'  • {user_info}: {status}')
        
        self.stdout.write('\n🌐 Admin Panel URLs:')
        self.stdout.write('  📋 Telegram Users: http://localhost:8000/admin/notifications/telegramuser/')
        self.stdout.write('  📨 Notifications: http://localhost:8000/admin/notifications/telegramnotification/')
        self.stdout.write('  🤖 Bot Analytics: http://localhost:8000/admin/bot-analytics/')
