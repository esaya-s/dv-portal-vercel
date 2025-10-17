#!/usr/bin/env python3
"""
Fix website deployment issues
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def fix_website():
    print("🔧 Fixing Website Deployment Issues")
    print("=" * 50)
    
    try:
        import django
        from django.core.management import execute_from_command_line
        
        # Setup Django
        django.setup()
        print("✅ Django setup completed!")
        
        # Step 1: Check file permissions
        print("\n📁 Step 1: Checking file permissions...")
        critical_files = [
            'passenger_wsgi.py',
            '.htaccess',
            'dv_portal/settings_production.py'
        ]
        
        for file_path in critical_files:
            if os.path.exists(file_path):
                stat = os.stat(file_path)
                print(f"✅ {file_path} exists (mode: {oct(stat.st_mode)})")
            else:
                print(f"❌ {file_path} missing")
        
        # Step 2: Test Django configuration
        print("\n⚙️ Step 2: Testing Django configuration...")
        try:
            from django.conf import settings
            print(f"✅ DEBUG: {settings.DEBUG}")
            print(f"✅ ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
            print(f"✅ ROOT_URLCONF: {settings.ROOT_URLCONF}")
        except Exception as e:
            print(f"❌ Django config error: {e}")
        
        # Step 3: Test database
        print("\n🗄️ Step 3: Testing database...")
        try:
            from django.db import connection
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print(f"✅ Database connection: {result}")
            
            # Check essential tables
            cursor.execute("SHOW TABLES LIKE 'applications_%'")
            app_tables = cursor.fetchall()
            print(f"✅ Applications tables: {len(app_tables)} found")
            
        except Exception as e:
            print(f"❌ Database error: {e}")
        
        # Step 4: Test URL patterns
        print("\n🔗 Step 4: Testing URL patterns...")
        try:
            from django.urls import get_resolver
            resolver = get_resolver()
            url_patterns = resolver.url_patterns
            print(f"✅ URL patterns loaded: {len(url_patterns)} found")
        except Exception as e:
            print(f"❌ URL patterns error: {e}")
        
        # Step 5: Test WSGI application
        print("\n🌐 Step 5: Testing WSGI application...")
        try:
            from django.core.wsgi import get_wsgi_application
            wsgi_app = get_wsgi_application()
            print("✅ WSGI application created successfully")
        except Exception as e:
            print(f"❌ WSGI error: {e}")
        
        # Step 6: Collect static files
        print("\n📁 Step 6: Collecting static files...")
        try:
            execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
            print("✅ Static files collected successfully")
        except Exception as e:
            print(f"❌ Static files error: {e}")
        
        # Step 7: Create simple test page
        print("\n📄 Step 7: Creating test page...")
        test_html = """
<!DOCTYPE html>
<html>
<head>
    <title>DV Portal Test</title>
</head>
<body>
    <h1>DV Portal Ethiopia - Test Page</h1>
    <p>If you can see this page, Django is working!</p>
    <p>Time: """ + str(django.utils.timezone.now()) + """</p>
    <p><a href="/admin/">Admin Panel</a></p>
    <p><a href="/apply/">Apply Now</a></p>
</body>
</html>
        """
        
        with open('test.html', 'w') as f:
            f.write(test_html)
        print("✅ Test page created: test.html")
        
        print("\n" + "=" * 50)
        print("🎯 WEBSITE FIX COMPLETED!")
        print("=" * 50)
        print("📋 Next Steps:")
        print("1. Check Python App settings in cPanel:")
        print("   - Application Root: public_html/dv")
        print("   - Application Startup File: passenger_wsgi.py")
        print("   - Application Entry Point: application")
        print("2. Restart Python App in cPanel")
        print("3. Check file permissions (should be 644 for files, 755 for directories)")
        print("4. Test: https://polocash.com/test.html")
        print("5. Test: https://polocash.com/")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Website fix error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fix_website()
