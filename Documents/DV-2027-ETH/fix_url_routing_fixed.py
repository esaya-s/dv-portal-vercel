#!/usr/bin/env python3
"""
Fix URL routing issues for cPanel deployment - CORRECTED VERSION
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def fix_url_routing():
    print("🔧 Fixing URL Routing Issues")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        print("✅ Django setup completed!")
        
        # Step 1: Create an improved .htaccess file
        print("\n📝 Step 1: Creating improved .htaccess...")
        htaccess_content = '''# Enable URL rewriting
RewriteEngine On

# Handle Django URLs - redirect everything to passenger_wsgi.py
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} !^/static/
RewriteCond %{REQUEST_URI} !^/media/
RewriteCond %{REQUEST_URI} !^/favicon.ico
RewriteCond %{REQUEST_URI} !^/robots.txt
RewriteRule ^(.*)$ passenger_wsgi.py [QSA,L]

# Serve static files directly
RewriteRule ^static/(.*)$ staticfiles/$1 [L]

# Security headers
Header always set X-Content-Type-Options nosniff
Header always set X-Frame-Options DENY
Header always set X-XSS-Protection "1; mode=block"

# Cache static files
<FilesMatch "\\.(css|js|png|jpg|jpeg|gif|ico|svg)$">
    ExpiresActive On
    ExpiresDefault "access plus 1 month"
</FilesMatch>
'''
        
        with open('.htaccess_new', 'w') as f:
            f.write(htaccess_content)
        print("✅ Created .htaccess_new")
        
        # Step 2: Create a simple test .htaccess (minimal version)
        print("\n📝 Step 2: Creating minimal .htaccess...")
        minimal_htaccess = '''RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ passenger_wsgi.py [QSA,L]
'''
        
        with open('.htaccess_minimal', 'w') as f:
            f.write(minimal_htaccess)
        print("✅ Created .htaccess_minimal")
        
        # Step 3: Create deployment instructions
        print("\n📋 Step 3: Creating deployment instructions...")
        instructions = '''# URL Routing Fix Instructions

## Problem: index.html works but Django URLs don't

This is a common cPanel issue where static files work but Django URL routing doesn't.

## Solution Steps:

### 1. Update .htaccess file
Choose one of these options:

#### Option A: Use .htaccess_new (recommended)
- Replace your current .htaccess with .htaccess_new
- This includes security headers and static file handling

#### Option B: Use .htaccess_minimal (if Option A doesn't work)
- Replace your current .htaccess with .htaccess_minimal
- This is the simplest version that should work

### 2. Test Django URLs
Try these URLs to test Django routing:
- https://polocash.com/admin/ (should show Django admin)
- https://polocash.com/apply/ (should show application form)
- https://polocash.com/applications/status/ (should show status page)

### 3. If URLs still don't work, try these fixes:

#### Check Python App settings in cPanel:
- Go to cPanel → Software → Python App
- Make sure Application Startup File is: passenger_wsgi.py
- Make sure Application Entry Point is: application
- Restart the Python App

#### Check file permissions:
- passenger_wsgi.py should be 644
- .htaccess should be 644
- All directories should be 755

### 4. Test Results Expected:
- ✅ https://polocash.com/admin/ → Django admin login
- ✅ https://polocash.com/apply/ → Application form
- ✅ https://polocash.com/applications/status/ → Status page
- ✅ https://polocash.com/ → Django homepage

## Admin Credentials:
- Username: admin
- Password: v7Ix&Kwfkf

## If still not working:
The issue might be with cPanel's Passenger configuration. Contact your hosting provider or try a different hosting service that better supports Django applications.
'''
        
        with open('URL_ROUTING_INSTRUCTIONS.txt', 'w') as f:
            f.write(instructions)
        print("✅ Created URL_ROUTING_INSTRUCTIONS.txt")
        
        print("\n" + "=" * 50)
        print("🎯 URL ROUTING FIX COMPLETED!")
        print("=" * 50)
        print("📋 Next Steps:")
        print("1. Choose one of these .htaccess files:")
        print("   - .htaccess_new (recommended)")
        print("   - .htaccess_minimal (simple version)")
        print("2. Replace your current .htaccess with the chosen file")
        print("3. Test: https://polocash.com/admin/")
        print("4. Test: https://polocash.com/apply/")
        print("")
        print("🔑 Admin Login:")
        print("   Username: admin")
        print("   Password: v7Ix&Kwfkf")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ URL routing fix error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fix_url_routing()
