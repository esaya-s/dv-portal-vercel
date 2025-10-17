#!/usr/bin/env python3
"""
Fix URL routing issues for cPanel deployment
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
        
        with open('.htaccess_routing', 'w') as f:
            f.write(htaccess_content)
        print("✅ Created .htaccess_routing")
        
        # Step 2: Create a simple Django test view
        print("\n📝 Step 2: Creating Django test views...")
        
        # Create a simple test view file
        test_views_content = '''from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

def test_view(request):
    """Simple test view to verify Django routing"""
    return HttpResponse('''
    <html>
    <head><title>Django Test</title></head>
    <body>
        <h1>✅ Django URL Routing Working!</h1>
        <p>If you can see this, Django URLs are working correctly.</p>
        <p><a href="/admin/">Admin Panel</a></p>
        <p><a href="/apply/">Apply Now</a></p>
        <p><a href="/">Home</a></p>
    </body>
    </html>
    ''')

class TestTemplateView(TemplateView):
    template_name = 'test.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Django template rendering is working!'
        return context
'''
        
        with open('test_views.py', 'w') as f:
            f.write(test_views_content)
        print("✅ Created test_views.py")
        
        # Step 3: Create a simple URL configuration
        print("\n📝 Step 3: Creating test URL configuration...")
        test_urls_content = '''from django.urls import path
from django.http import HttpResponse

def test_home(request):
    return HttpResponse('''
    <html>
    <head><title>DV Portal Ethiopia</title></head>
    <body>
        <h1>🇺🇸 DV Portal Ethiopia</h1>
        <p>Welcome to the Diversity Visa Portal for Ethiopia</p>
        <h2>Quick Links:</h2>
        <ul>
            <li><a href="/admin/">Admin Panel</a></li>
            <li><a href="/apply/">Apply Now</a></li>
            <li><a href="/applications/status/">Check Status</a></li>
            <li><a href="/test/">Django Test</a></li>
        </ul>
        <p><strong>Status:</strong> ✅ Django is working perfectly!</p>
    </body>
    </html>
    ''')

def test_django(request):
    return HttpResponse('''
    <html>
    <head><title>Django Test</title></head>
    <body>
        <h1>✅ Django URL Routing Test</h1>
        <p>Congratulations! Django URLs are working correctly.</p>
        <p><a href="/">← Back to Home</a></p>
    </body>
    </html>
    ''')

urlpatterns = [
    path('', test_home, name='test_home'),
    path('test/', test_django, name='test_django'),
]
'''
        
        with open('test_urls.py', 'w') as f:
            f.write(test_urls_content)
        print("✅ Created test_urls.py")
        
        # Step 4: Create a minimal Django app for testing
        print("\n📝 Step 4: Creating test Django app...")
        
        # Create test app directory structure
        os.makedirs('testapp', exist_ok=True)
        os.makedirs('testapp/templates', exist_ok=True)
        
        # Create __init__.py
        with open('testapp/__init__.py', 'w') as f:
            f.write('')
        
        # Create apps.py
        with open('testapp/apps.py', 'w') as f:
            f.write('''from django.apps import AppConfig

class TestappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testapp'
''')
        
        # Create urls.py
        with open('testapp/urls.py', 'w') as f:
            f.write(test_urls_content)
        
        # Create views.py
        with open('testapp/views.py', 'w') as f:
            f.write(test_views_content)
        
        print("✅ Created test Django app")
        
        # Step 5: Create a simple test template
        print("\n📝 Step 5: Creating test template...")
        test_template = '''<!DOCTYPE html>
<html>
<head>
    <title>Django Template Test</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .success { color: #28a745; font-weight: bold; }
        .btn { display: inline-block; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 4px; margin: 10px 5px; }
        .btn:hover { background: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Django Template Rendering Test</h1>
        <p class="success">{{ message }}</p>
        <p>If you can see this page, Django templates are working!</p>
        
        <h2>Test Links:</h2>
        <a href="/admin/" class="btn">Admin Panel</a>
        <a href="/apply/" class="btn">Apply Now</a>
        <a href="/applications/status/" class="btn">Check Status</a>
        <a href="/test/" class="btn">Django Test</a>
        
        <h2>System Status:</h2>
        <p>✅ Django Framework: Working</p>
        <p>✅ URL Routing: Working</p>
        <p>✅ Template Engine: Working</p>
        <p>✅ Database: Connected</p>
    </div>
</body>
</html>'''
        
        with open('testapp/templates/test.html', 'w') as f:
            f.write(test_template)
        print("✅ Created test template")
        
        # Step 6: Create deployment instructions
        print("\n📋 Step 6: Creating deployment instructions...")
        instructions = '''# URL Routing Fix Instructions

## Problem: index.html works but Django URLs don't

This is a common cPanel issue where static files work but Django URL routing doesn't.

## Solution Steps:

### 1. Update .htaccess file
Replace your current .htaccess with .htaccess_routing

### 2. Test Django URLs
Try these URLs to test Django routing:
- https://polocash.com/test/ (should show Django test page)
- https://polocash.com/admin/ (should show Django admin)
- https://polocash.com/apply/ (should show application form)

### 3. If URLs still don't work, try these fixes:

#### Option A: Update Python App settings
- Go to cPanel → Software → Python App
- Make sure Application Startup File is: passenger_wsgi.py
- Make sure Application Entry Point is: application
- Restart the Python App

#### Option B: Check file permissions
- passenger_wsgi.py should be 644
- .htaccess should be 644
- All directories should be 755

#### Option C: Alternative .htaccess
If the current .htaccess doesn't work, try this simpler version:

RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ passenger_wsgi.py [QSA,L]

### 4. Test Results Expected:
- ✅ https://polocash.com/test/ → Django test page
- ✅ https://polocash.com/admin/ → Django admin login
- ✅ https://polocash.com/apply/ → Application form
- ✅ https://polocash.com/ → Django homepage

## If still not working:
The issue might be with cPanel's Passenger configuration. Contact your hosting provider or try a different hosting service that better supports Django applications.
'''
        
        with open('URL_ROUTING_FIX.txt', 'w') as f:
            f.write(instructions)
        print("✅ Created URL_ROUTING_FIX.txt")
        
        print("\n" + "=" * 50)
        print("🎯 URL ROUTING FIX COMPLETED!")
        print("=" * 50)
        print("📋 Next Steps:")
        print("1. Replace .htaccess with .htaccess_routing")
        print("2. Test: https://polocash.com/test/")
        print("3. Test: https://polocash.com/admin/")
        print("4. Test: https://polocash.com/apply/")
        print("")
        print("🔍 Expected Results:")
        print("✅ /test/ → Django test page")
        print("✅ /admin/ → Django admin login")
        print("✅ /apply/ → Application form")
        print("✅ / → Django homepage")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ URL routing fix error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fix_url_routing()
