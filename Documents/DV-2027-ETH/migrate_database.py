#!/usr/bin/env python3
"""
Database Migration Script for cPanel
Run this script to set up your database tables
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
    """Run database migrations"""
    try:
        print("🔄 Running database migrations...")
        execute_from_command_line(['manage.py', 'migrate', '--settings=dv_portal.settings_production'])
        print("✅ Database migrations completed successfully!")
        return True
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
