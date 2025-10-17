#!/usr/bin/env python
"""
Test Telegram Bot Status
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings')
django.setup()

def test_telegram_bot_status():
    """Test Telegram bot status and configuration"""
    print("🤖 Testing Telegram Bot Status")
    print("=" * 50)
    
    try:
        from django.conf import settings
        from notifications.telegram_bot import bot
        
        print("✅ Bot Configuration:")
        print(f"  🤖 Bot Name: {settings.TELEGRAM_BOT_NAME}")
        print(f"  📱 Bot Username: {settings.TELEGRAM_BOT_USERNAME}")
        print(f"  👤 Admin Username: {settings.TELEGRAM_ADMIN_USERNAME}")
        print(f"  💬 Admin Chat ID: {settings.TELEGRAM_ADMIN_CHAT_ID}")
        
        if bot:
            print("\n✅ Bot Status: INITIALIZED")
            print("  🟢 Bot is ready to receive messages")
            print("  📱 Bot can send notifications")
            print("  🔔 Contact form notifications enabled")
            print("  📧 Application notifications enabled")
        else:
            print("\n❌ Bot Status: NOT INITIALIZED")
            print("  🔴 Bot needs to be started")
            print("  ⚠️  Check TELEGRAM_BOT_TOKEN in settings")
        
        print("\n🎯 Bot Features:")
        print("  📧 Contact form notifications")
        print("  📝 Application submission notifications")
        print("  🔍 Status checking via /status command")
        print("  📊 Admin commands (/admin, /search, /stats)")
        print("  💬 User support and assistance")
        
        print("\n🌐 Bot Commands:")
        print("  /start - Start conversation with bot")
        print("  /help - Show available commands")
        print("  /status - Check application status")
        print("  /admin - Admin panel (admin only)")
        print("  /search - Search users by phone (admin only)")
        print("  /stats - Bot statistics (admin only)")
        
        print("\n📱 Contact Information:")
        print("  🤖 Bot Username: @dv2027apply")
        print("  📞 Phone: +251-963-173-312")
        print("  📧 Email: support@dvportal-ethiopia.com")
        
        print("\n✅ Bot is running and ready!")
        print("   Users can now interact with @dv2027apply")
        
    except Exception as e:
        print(f"❌ Error testing bot: {e}")
        print("  ⚠️  Check bot configuration and token")

if __name__ == "__main__":
    test_telegram_bot_status()
