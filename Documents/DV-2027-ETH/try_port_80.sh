#!/bin/bash
echo "🌐 Attempting to run Django directly on anvilu.com (port 80)..."
echo "================================================"

echo ""
echo "🔧 Trying to start Django on port 80..."

# Try Django development server on port 80
echo "Attempt 1: Django development server on port 80"
DJANGO_SETTINGS_MODULE=dv_portal.settings_production python manage.py runserver 0.0.0.0:80

# If that fails, try Gunicorn
echo ""
echo "Attempt 2: Gunicorn on port 80"
gunicorn --bind 0.0.0.0:80 --workers 3 dv_portal.wsgi:application

echo ""
echo "✅ If successful, your site will be available at: http://anvilu.com"
echo "👤 Admin panel: http://anvilu.com/admin/"
echo "📧 Username: usadv27"
