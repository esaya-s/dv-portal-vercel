#!/usr/bin/env python3
"""
Fix database migrations - create missing tables
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def fix_migrations():
    print("🔧 Fixing database migrations...")
    print("=" * 50)
    
    try:
        import django
        from django.core.management import execute_from_command_line
        
        # Setup Django
        django.setup()
        print("✅ Django setup completed!")
        
        # Check current migration status
        print("\n📋 Checking migration status...")
        execute_from_command_line(['manage.py', 'showmigrations'])
        
        # Run migrations for all apps
        print("\n🔄 Running migrations for all apps...")
        execute_from_command_line(['manage.py', 'migrate', '--run-syncdb'])
        
        # Specifically run migrations for applications app
        print("\n🔄 Running applications app migrations...")
        execute_from_command_line(['manage.py', 'migrate', 'applications'])
        
        # Run any remaining migrations
        print("\n🔄 Running any remaining migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        print("\n✅ Migrations completed successfully!")
        
        # Test database tables
        print("\n🧪 Testing database tables...")
        from django.db import connection
        cursor = connection.cursor()
        
        # Check if applications table exists
        cursor.execute("SHOW TABLES LIKE 'applications_%'")
        tables = cursor.fetchall()
        print(f"✅ Applications tables found: {len(tables)}")
        
        for table in tables:
            print(f"   - {table[0]}")
        
        # Test applications model
        try:
            from applications.models import DVApplication
            app_count = DVApplication.objects.count()
            print(f"✅ DVApplication model working: {app_count} applications")
        except Exception as e:
            print(f"❌ DVApplication model error: {e}")
        
        print("\n🎉 Database fix completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during migration fix: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fix_migrations()
