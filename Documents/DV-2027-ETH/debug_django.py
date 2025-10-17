#!/usr/bin/env python
"""
Debug script to check Django configuration
"""

import os
import sys

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

try:
    import django
    django.setup()
    print("✅ Django setup successful")
    
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    print("✅ WSGI application created")
    
    # Test database connection
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT 1")
    print("✅ Database connection successful")
    
    # Test static files
    from django.conf import settings
    print(f"✅ Static files directory: {settings.STATIC_ROOT}")
    print(f"✅ Static URL: {settings.STATIC_URL}")
    
    # Test templates
    print(f"✅ Templates directory: {settings.TEMPLATES[0]['DIRS']}")
    
    print("🎉 All checks passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
