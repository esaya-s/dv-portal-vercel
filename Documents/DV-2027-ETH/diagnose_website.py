#!/usr/bin/env python3
"""
Diagnose website issues and fix WSGI problems
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def diagnose_website():
    print("🔍 Diagnosing Website Issues")
    print("=" * 50)
    
    try:
        import django
        from django.core.management import execute_from_command_line
        from django.conf import settings
        
        # Setup Django
        django.setup()
        print("✅ Django setup completed!")
        
        # Test 1: Check Django configuration
        print("\n🔧 Test 1: Django Configuration")
        print(f"✅ DEBUG: {settings.DEBUG}")
        print(f"✅ ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
        print(f"✅ ROOT_URLCONF: {settings.ROOT_URLCONF}")
        print(f"✅ WSGI_APPLICATION: {settings.WSGI_APPLICATION}")
        
        # Test 2: Check URL configuration
        print("\n🔗 Test 2: URL Configuration")
        try:
            from django.urls import get_resolver
            resolver = get_resolver()
            print("✅ URL resolver loaded successfully")
            
            # Check if we can access URL patterns
            url_patterns = resolver.url_patterns
            print(f"✅ Found {len(url_patterns)} URL patterns")
            
            for pattern in url_patterns:
                print(f"   - {pattern}")
                
        except Exception as e:
            print(f"❌ URL configuration error: {e}")
        
        # Test 3: Check database connectivity
        print("\n🗄️ Test 3: Database Connectivity")
        try:
            from django.db import connection
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print(f"✅ Database connection: {result}")
            
            # Check if essential tables exist
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
            print(f"✅ Total tables: {len(tables)}")
            
            essential_tables = ['applications_dvapplication', 'applications_spouse', 'applications_child']
            for table in essential_tables:
                if table in tables:
                    print(f"✅ {table} exists")
                else:
                    print(f"❌ {table} missing")
                    
        except Exception as e:
            print(f"❌ Database error: {e}")
        
        # Test 4: Check Django models
        print("\n📋 Test 4: Django Models")
        try:
            from applications.models import DVApplication
            app_count = DVApplication.objects.count()
            print(f"✅ DVApplication model: {app_count} records")
        except Exception as e:
            print(f"❌ DVApplication model error: {e}")
        
        # Test 5: Check static files
        print("\n📁 Test 5: Static Files")
        try:
            static_root = settings.STATIC_ROOT
            print(f"✅ STATIC_ROOT: {static_root}")
            print(f"✅ STATIC_URL: {settings.STATIC_URL}")
            
            if os.path.exists(static_root):
                static_files = os.listdir(static_root)
                print(f"✅ Static files directory exists with {len(static_files)} items")
            else:
                print(f"❌ Static files directory missing: {static_root}")
                
        except Exception as e:
            print(f"❌ Static files error: {e}")
        
        # Test 6: Django system check
        print("\n🔍 Test 6: Django System Check")
        try:
            execute_from_command_line(['manage.py', 'check'])
            print("✅ Django system check passed!")
        except Exception as e:
            print(f"❌ System check failed: {e}")
        
        print("\n" + "=" * 50)
        print("🎯 DIAGNOSIS COMPLETE!")
        print("If all tests passed, the issue is likely with:")
        print("1. Python App configuration in cPanel")
        print("2. passenger_wsgi.py file")
        print("3. .htaccess file")
        print("4. File permissions")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Diagnosis error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    diagnose_website()
