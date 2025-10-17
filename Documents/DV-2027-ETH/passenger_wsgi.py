#!/usr/bin/env python
"""
WSGI configuration for DV Portal on cPanel
This file is required for cPanel Python App deployment
"""

import os
import sys

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Set Django settings module for production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

# Get WSGI application
application = get_wsgi_application()

# Optional: Start Telegram bot in production
try:
    from notifications.telegram_bot import start_bot
    # Uncomment the next line to start Telegram bot in production
    # start_bot()
except ImportError:
    pass
except Exception as e:
    print(f"Warning: Could not start Telegram bot: {e}")