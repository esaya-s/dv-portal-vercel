#!/usr/bin/env python
"""
Minimal Django WSGI for debugging
"""

import os
import sys

# Add the project directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_simple')

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    print("✅ Django WSGI application loaded successfully")
except Exception as e:
    print(f"❌ Django WSGI error: {e}")
    import traceback
    traceback.print_exc()
    
    # Fallback to simple WSGI
    def application(environ, start_response):
        response_body = f"""
        <html>
        <head><title>Django Error</title></head>
        <body>
            <h1>Django Error</h1>
            <p>Error: {e}</p>
            <p>Check your Django configuration</p>
        </body>
        </html>
        """.encode()
        
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        return [response_body]
