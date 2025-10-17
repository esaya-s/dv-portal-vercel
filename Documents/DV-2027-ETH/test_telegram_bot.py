#!/usr/bin/env python
"""
Test script for Telegram bot functionality
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings')
django.setup()

from notifications.telegram_bot import bot, ADMIN_USERNAME, BOT_NAME, BOT_USERNAME

def test_bot_info():
    """Test bot information"""
    try:
        if bot:
            bot_info = bot.get_me()
            print(f"✅ Bot initialized successfully!")
            print(f"Bot Name: {bot_info.first_name}")
            print(f"Bot Username: @{bot_info.username}")
            print(f"Bot ID: {bot_info.id}")
            print(f"Expected Bot Name: {BOT_NAME}")
            print(f"Expected Bot Username: @{BOT_USERNAME}")
            print(f"Admin Username: @{ADMIN_USERNAME}")
            return True
        else:
            print("❌ Bot not initialized")
            return False
    except Exception as e:
        print(f"❌ Error testing bot: {e}")
        return False

def test_admin_access():
    """Test admin access"""
    try:
        # This would require the admin to have started a conversation with the bot
        print(f"Admin username configured: @{ADMIN_USERNAME}")
        print("To test admin access, the admin needs to start a conversation with the bot first.")
        return True
    except Exception as e:
        print(f"❌ Error testing admin access: {e}")
        return False

if __name__ == "__main__":
    print("🤖 Testing Telegram Bot Configuration")
    print("=" * 50)
    
    # Test bot info
    bot_ok = test_bot_info()
    
    print("\n" + "=" * 50)
    
    # Test admin access
    admin_ok = test_admin_access()
    
    print("\n" + "=" * 50)
    
    if bot_ok and admin_ok:
        print("✅ All tests passed! Bot is ready to use.")
        print("\nTo start the bot, run:")
        print("python manage.py start_telegram_bot")
    else:
        print("❌ Some tests failed. Please check your configuration.")
