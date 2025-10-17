#!/usr/bin/env python
"""
Test the application form submission with Telegram integration
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings')
django.setup()

from applications.models import DVApplication
from notifications.telegram_bot import send_application_notification_to_admin, send_confirmation_to_applicant

def test_telegram_integration():
    """Test Telegram integration with a sample application"""
    
    print("🧪 Testing Telegram Integration")
    print("=" * 50)
    
    # Create a test application
    from datetime import date
    test_app = DVApplication.objects.create(
        first_name="Test",
        last_name="User",
        email="test@example.com",
        phone_number="+251911234567",
        country_of_citizenship="Ethiopia",
        date_of_birth=date(1990, 1, 1),
        gender="M",
        marital_status="single",
        telegram_username="testuser",  # This would be provided by user
        status="pending"
    )
    
    print(f"✅ Created test application: {test_app.dv_id}")
    
    # Test admin notification
    print("\n📤 Testing admin notification...")
    admin_result = send_application_notification_to_admin(test_app)
    if admin_result:
        print("✅ Admin notification sent successfully")
    else:
        print("⚠️ Admin notification failed (this is expected if admin chat not configured)")
    
    # Test user confirmation
    print("\n📤 Testing user confirmation...")
    user_result = send_confirmation_to_applicant(test_app)
    if user_result:
        if isinstance(user_result, str) and user_result.startswith("https://t.me/"):
            print(f"✅ Deep link generated: {user_result}")
        else:
            print("✅ User confirmation sent successfully")
    else:
        print("⚠️ User confirmation failed")
    
    # Clean up test application
    test_app.delete()
    print(f"\n🧹 Cleaned up test application")
    
    print("\n" + "=" * 50)
    print("✅ Telegram integration test completed!")
    print("\nTo test with real data:")
    print("1. Start the bot: python manage.py start_telegram_bot")
    print("2. Submit an application through the web form")
    print("3. Check Telegram for notifications")

if __name__ == "__main__":
    test_telegram_integration()
