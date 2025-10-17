#!/usr/bin/env python3
"""
Static Files Collection Script for cPanel
Run this script to collect all static files for production
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

from django.core.management import execute_from_command_line

def main():
    """Collect static files"""
    try:
        print("📁 Collecting static files...")
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--settings=dv_portal.settings_production'])
        print("✅ Static files collected successfully!")
        return True
    except Exception as e:
        print(f"❌ Static collection failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
