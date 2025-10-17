#!/usr/bin/env python3
"""
Telegram Bot Startup Script for cPanel
Run this script to start the Telegram bot
"""

import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(project_dir))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')
django.setup()

import logging
from notifications.telegram_bot import start_bot

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def main():
    """Start the Telegram bot"""
    try:
        print("🤖 Starting Telegram bot...")
        
        # Check if bot token is configured
        from django.conf import settings
        if not settings.TELEGRAM_BOT_TOKEN:
            print("❌ TELEGRAM_BOT_TOKEN is not configured!")
            return False
            
        print("✅ Bot token found, starting bot...")
        start_bot()
        
        print("✅ Telegram bot started successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Failed to start Telegram bot: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
