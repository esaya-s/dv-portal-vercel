#!/usr/bin/env python3
"""
Fix 403 Forbidden errors and file permissions
"""

import os
import sys
import stat

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def fix_403_errors():
    print("🔧 Fixing 403 Forbidden Errors")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        print("✅ Django setup completed!")
        
        # Step 1: Check current file permissions
        print("\n📁 Step 1: Checking file permissions...")
        
        critical_files = [
            'passenger_wsgi.py',
            '.htaccess',
            'index.html',
            'dv_portal/settings_production.py'
        ]
        
        for file_path in critical_files:
            if os.path.exists(file_path):
                current_perms = oct(os.stat(file_path).st_mode)[-3:]
                print(f"✅ {file_path}: {current_perms}")
                
                # Check if permissions are correct
                if file_path == '.htaccess' and current_perms != '644':
                    print(f"⚠️ {file_path} should be 644, currently {current_perms}")
                elif file_path == 'passenger_wsgi.py' and current_perms not in ['644', '755']:
                    print(f"⚠️ {file_path} should be 644 or 755, currently {current_perms}")
            else:
                print(f"❌ {file_path} missing")
        
        # Step 2: Create a minimal .htaccess file
        print("\n📝 Step 2: Creating minimal .htaccess...")
        minimal_htaccess = '''RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ passenger_wsgi.py [QSA,L]
'''
        
        with open('.htaccess_minimal', 'w') as f:
            f.write(minimal_htaccess)
        print("✅ Created .htaccess_minimal")
        
        # Step 3: Create an even simpler .htaccess (no security restrictions)
        print("\n📝 Step 3: Creating ultra-simple .htaccess...")
        ultra_simple_htaccess = '''RewriteEngine On
RewriteRule ^(.*)$ passenger_wsgi.py [QSA,L]
'''
        
        with open('.htaccess_ultra_simple', 'w') as f:
            f.write(ultra_simple_htaccess)
        print("✅ Created .htaccess_ultra_simple")
        
        # Step 4: Create a test passenger_wsgi.py without telegram bot
        print("\n📝 Step 4: Creating simple passenger_wsgi.py...")
        simple_wsgi = '''#!/usr/bin/env python3
"""
Simple Passenger WSGI file for cPanel deployment
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

# Import Django's WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
'''
        
        with open('passenger_wsgi_simple.py', 'w') as f:
            f.write(simple_wsgi)
        print("✅ Created passenger_wsgi_simple.py")
        
        # Step 5: Create troubleshooting instructions
        print("\n📋 Step 5: Creating troubleshooting instructions...")
        instructions = '''# Fix 403 Forbidden Errors

## Problem: 403 Forbidden Error
This means the server is denying access to your files.

## Solution Steps:

### 1. Try Different .htaccess Files (in order):
1. **First try:** .htaccess_minimal
2. **If still 403:** .htaccess_ultra_simple
3. **If still 403:** Delete .htaccess completely

### 2. Try Different passenger_wsgi.py:
1. **First try:** passenger_wsgi_simple.py (no telegram bot)
2. **If still 403:** Check Python App settings in cPanel

### 3. Check File Permissions:
- passenger_wsgi.py should be 644 or 755
- .htaccess should be 644
- All directories should be 755

### 4. Check Python App Settings in cPanel:
- Go to cPanel → Software → Python App
- Application Root: public_html/dv
- Application Startup File: passenger_wsgi_simple.py
- Application Entry Point: application
- Restart Python App

### 5. Test URLs:
- https://polocash.com/ (should work)
- https://polocash.com/admin/ (should work)
- https://polocash.com/applications/apply/ (should work)

## Common Causes of 403 Errors:
1. **Too restrictive .htaccess** - Use minimal version
2. **Wrong file permissions** - Check 644/755
3. **Python App not started** - Restart in cPanel
4. **Wrong Application Startup File** - Check cPanel settings
5. **Server security restrictions** - Contact hosting provider

## Admin Credentials:
- Username: admin
- Password: v7Ix&Kwfkf

## If Nothing Works:
Contact your hosting provider - they may have server-level restrictions.
'''
        
        with open('FIX_403_ERRORS.txt', 'w') as f:
            f.write(instructions)
        print("✅ Created FIX_403_ERRORS.txt")
        
        print("\n" + "=" * 50)
        print("🎯 403 ERROR FIX COMPLETED!")
        print("=" * 50)
        print("📋 Try these solutions in order:")
        print("1. Replace .htaccess with .htaccess_minimal")
        print("2. If still 403, try .htaccess_ultra_simple")
        print("3. If still 403, try passenger_wsgi_simple.py")
        print("4. Check Python App settings in cPanel")
        print("5. Restart Python App")
        print("")
        print("🔍 Test: https://polocash.com/")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ 403 fix error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fix_403_errors()
