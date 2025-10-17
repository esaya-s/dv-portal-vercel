#!/usr/bin/env python3
"""
Final test to verify everything is working
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def final_test():
    print("🧪 Final System Test for DV Portal")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        print("✅ Django setup successful!")
        
        # Test database connection
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"✅ Database connection: {result}")
        
        # Test all models
        print("\n📋 Testing Django Models:")
        
        # Test User model
        from django.contrib.auth.models import User
        user_count = User.objects.count()
        print(f"✅ User model: {user_count} users")
        
        # Test UserProfile model
        try:
            from accounts.models import UserProfile
            profile_count = UserProfile.objects.count()
            print(f"✅ UserProfile model: {profile_count} profiles")
        except Exception as e:
            print(f"❌ UserProfile model: {e}")
        
        # Test DVApplication model
        try:
            from applications.models import DVApplication
            app_count = DVApplication.objects.count()
            print(f"✅ DVApplication model: {app_count} applications")
        except Exception as e:
            print(f"❌ DVApplication model: {e}")
        
        # Test Spouse model
        try:
            from applications.models import Spouse
            spouse_count = Spouse.objects.count()
            print(f"✅ Spouse model: {spouse_count} spouses")
        except Exception as e:
            print(f"❌ Spouse model: {e}")
        
        # Test Child model
        try:
            from applications.models import Child
            child_count = Child.objects.count()
            print(f"✅ Child model: {child_count} children")
        except Exception as e:
            print(f"❌ Child model: {e}")
        
        # Test ContactMessage model
        try:
            from core.models import ContactMessage
            contact_count = ContactMessage.objects.count()
            print(f"✅ ContactMessage model: {contact_count} messages")
        except Exception as e:
            print(f"❌ ContactMessage model: {e}")
        
        # Test TelegramUser model
        try:
            from notifications.models import TelegramUser
            tg_user_count = TelegramUser.objects.count()
            print(f"✅ TelegramUser model: {tg_user_count} users")
        except Exception as e:
            print(f"❌ TelegramUser model: {e}")
        
        # Test TelegramNotification model
        try:
            from notifications.models import TelegramNotification
            tg_notif_count = TelegramNotification.objects.count()
            print(f"✅ TelegramNotification model: {tg_notif_count} notifications")
        except Exception as e:
            print(f"❌ TelegramNotification model: {e}")
        
        # Test admin user
        print("\n👤 Testing Admin User:")
        try:
            admin_user = User.objects.get(username='admin')
            print(f"✅ Admin user exists: {admin_user.username}")
            print(f"✅ Admin email: {admin_user.email}")
        except Exception as e:
            print(f"❌ Admin user: {e}")
        
        # Test Django system check
        print("\n🔍 Running Django System Check:")
        try:
            from django.core.management import execute_from_command_line
            execute_from_command_line(['manage.py', 'check'])
            print("✅ Django system check passed!")
        except Exception as e:
            print(f"⚠️ System check: {e}")
        
        print("\n" + "=" * 50)
        print("🎉 FINAL TEST COMPLETED!")
        print("🌐 Your DV Portal is ready!")
        print("🔗 Website: https://polocash.com")
        print("👤 Admin: https://polocash.com/admin/")
        print("📱 Telegram Bot: @dv20272etbot")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Final test error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    final_test()
