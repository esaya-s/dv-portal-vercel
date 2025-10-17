#!/usr/bin/env python3
"""
Debug Passenger WSGI file - with detailed error logging
"""

import os
import sys
import traceback

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

print("🔧 Starting Passenger WSGI Debug...")
print(f"📁 Project directory: {project_dir}")
print(f"🐍 Python path: {sys.path}")
print(f"⚙️ Settings module: {os.environ.get('DJANGO_SETTINGS_MODULE')}")

try:
    # Import Django's WSGI application
    from django.core.wsgi import get_wsgi_application
    print("✅ Django WSGI imported successfully")
    
    # Get the WSGI application
    application = get_wsgi_application()
    print("✅ WSGI application created successfully")
    
    print("🎉 WSGI application is ready!")
    
except Exception as e:
    print(f"❌ WSGI Error: {e}")
    print("📋 Full traceback:")
    traceback.print_exc()
    
    # Create a simple error application
    def application(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        
        error_html = f"""
        <html>
        <head><title>WSGI Error</title></head>
        <body>
        <h1>WSGI Configuration Error</h1>
        <p>Error: {str(e)}</p>
        <pre>{traceback.format_exc()}</pre>
        </body>
        </html>
        """
        
        return [error_html.encode('utf-8')]

print("🔧 Passenger WSGI Debug completed")
