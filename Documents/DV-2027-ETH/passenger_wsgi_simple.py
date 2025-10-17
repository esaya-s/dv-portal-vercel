#!/usr/bin/env python3
"""
Simple Passenger WSGI file for cPanel deployment
This version excludes the telegram bot to isolate issues
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module to production settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

# Import Django's WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

print("WSGI application loaded successfully!")
