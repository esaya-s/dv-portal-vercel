#!/usr/bin/env python3
"""
Create Superuser Script for cPanel
Run this script to create an admin user
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

from django.contrib.auth import get_user_model

def main():
    """Create superuser if it doesn't exist"""
    try:
        User = get_user_model()
        
        # Check if admin user already exists
        if User.objects.filter(username='admin').exists():
            print("✅ Admin user already exists!")
            return True
            
        # Create admin user
        print("👤 Creating admin user...")
        User.objects.create_superuser(
            username='admin',
            email='admin@polocash.com',
            password='admin123'
        )
        print("✅ Admin user created successfully!")
        print("📧 Username: admin")
        print("🔑 Password: admin123")
        print("⚠️  Please change the password after first login!")
        return True
        
    except Exception as e:
        print(f"❌ Superuser creation failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)