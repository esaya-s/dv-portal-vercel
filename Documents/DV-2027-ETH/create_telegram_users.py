#!/usr/bin/env python
"""
Create test Telegram users for admin panel demonstration
"""
import os
import sys
import django
from datetime import datetime, timedelta

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings')
django.setup()

from notifications.models import TelegramUser, TelegramNotification
from applications.models import DVApplication

def create_test_telegram_users():
    """Create test Telegram users for admin panel"""
    print("🤖 Creating Test Telegram Users")
    print("=" * 50)
    
    # Create test Telegram users
    users_data = [
        {
            'chat_id': '123456789',
            'username': 'johndoe',
            'first_name': 'John',
            'last_name': 'Doe',
            'is_admin': False,
            'is_blocked': False
        },
        {
            'chat_id': '987654321',
            'username': 'janesmith',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'is_admin': False,
            'is_blocked': False
        },
        {
            'chat_id': '555666777',
            'username': 'anvilutech',
            'first_name': 'Anvil',
            'last_name': 'Tech',
            'is_admin': True,
            'is_blocked': False
        },
        {
            'chat_id': '111222333',
            'username': 'michaelj',
            'first_name': 'Michael',
            'last_name': 'Johnson',
            'is_admin': False,
            'is_blocked': False
        },
        {
            'chat_id': '444555666',
            'username': 'blockeduser',
            'first_name': 'Blocked',
            'last_name': 'User',
            'is_admin': False,
            'is_blocked': True
        },
        {
            'chat_id': '777888999',
            'username': 'testuser1',
            'first_name': 'Test',
            'last_name': 'User1',
            'is_admin': False,
            'is_blocked': False
        },
        {
            'chat_id': '000111222',
            'username': 'testuser2',
            'first_name': 'Test',
            'last_name': 'User2',
            'is_admin': False,
            'is_blocked': False
        }
    ]
    
    created_users = []
    for user_data in users_data:
        user, created = TelegramUser.objects.get_or_create(
            chat_id=user_data['chat_id'],
            defaults=user_data
        )
        if created:
            print(f"✅ Created Telegram User: @{user_data['username']} ({user_data['first_name']} {user_data['last_name']})")
            created_users.append(user)
        else:
            print(f"ℹ️ Telegram User already exists: @{user_data['username']}")
    
    # Create some test notifications
    print("\n📨 Creating Test Notifications")
    print("-" * 30)
    
    # Get some applications to link notifications to
    applications = DVApplication.objects.all()[:3]
    
    notification_data = [
        {
            'telegram_user': created_users[0] if len(created_users) > 0 else None,
            'application': applications[0] if len(applications) > 0 else None,
            'message': 'Your DV-2027 application has been received and is being processed.',
            'sent': True,
            'sent_at': datetime.now() - timedelta(hours=2)
        },
        {
            'telegram_user': created_users[1] if len(created_users) > 1 else None,
            'application': applications[1] if len(applications) > 1 else None,
            'message': 'Your application status has been updated to Under Review.',
            'sent': True,
            'sent_at': datetime.now() - timedelta(hours=1)
        },
        {
            'telegram_user': created_users[2] if len(created_users) > 2 else None,
            'application': applications[2] if len(applications) > 2 else None,
            'message': 'Congratulations! Your application has been approved.',
            'sent': True,
            'sent_at': datetime.now() - timedelta(minutes=30)
        },
        {
            'telegram_user': created_users[3] if len(created_users) > 3 else None,
            'application': None,
            'message': 'Failed to send notification - user not found.',
            'sent': False,
            'sent_at': None
        }
    ]
    
    for notif_data in notification_data:
        if notif_data['telegram_user']:  # Only create if we have a user
            notification = TelegramNotification.objects.create(**notif_data)
            print(f"✅ Created notification for @{notif_data['telegram_user'].username}")
    
    print("\n" + "=" * 50)
    print("✅ Test Telegram users and notifications created!")
    print(f"\n📊 Statistics:")
    print(f"  👥 Total Telegram Users: {TelegramUser.objects.count()}")
    print(f"  👑 Admin Users: {TelegramUser.objects.filter(is_admin=True).count()}")
    print(f"  🚫 Blocked Users: {TelegramUser.objects.filter(is_blocked=True).count()}")
    print(f"  📨 Total Notifications: {TelegramNotification.objects.count()}")
    
    print(f"\n🌐 View in Admin Panel:")
    print(f"  📋 Telegram Users: http://localhost:8000/admin/notifications/telegramuser/")
    print(f"  📨 Notifications: http://localhost:8000/admin/notifications/telegramnotification/")
    print(f"  🤖 Bot Analytics: http://localhost:8000/admin/bot-analytics/")

if __name__ == "__main__":
    create_test_telegram_users()
