#!/usr/bin/env python3
"""
Test Django application setup
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

try:
    import django
    django.setup()
    
    print("✅ Django setup successful!")
    print("✅ Settings module loaded correctly!")
    
    # Test database connection
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    print(f"✅ Database connection successful: {result}")
    
    # Test admin user
    from django.contrib.auth.models import User
    admin_count = User.objects.filter(username='admin').count()
    print(f"✅ Admin user exists: {admin_count > 0}")
    
    # Test applications
    from applications.models import DVApplication
    app_count = DVApplication.objects.count()
    print(f"✅ Applications table accessible: {app_count} applications")
    
    print("\n🎉 All tests passed! Your Django application is ready!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
