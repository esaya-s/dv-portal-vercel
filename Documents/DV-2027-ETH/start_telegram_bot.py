#!/usr/bin/env python3
"""
Telegram Bot Deployment Script for cPanel
This script can be run as a cron job to ensure the bot stays running
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
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(project_dir / 'logs' / 'telegram_bot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    """Main function to start the Telegram bot"""
    try:
        logger.info("Starting Telegram bot deployment script...")
        
        # Check if bot token is configured
        from django.conf import settings
        if not settings.TELEGRAM_BOT_TOKEN:
            logger.error("TELEGRAM_BOT_TOKEN is not configured!")
            return False
            
        logger.info("Bot token found, starting bot...")
        start_bot()
        
        logger.info("Telegram bot started successfully!")
        return True
        
    except Exception as e:
        logger.error(f"Failed to start Telegram bot: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
