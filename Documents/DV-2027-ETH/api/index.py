from django.core.wsgi import get_wsgi_application
import os

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_vercel')

# Get WSGI application
application = get_wsgi_application()

# Vercel handler
def handler(request):
    return application(request.environ, request.start_response)
