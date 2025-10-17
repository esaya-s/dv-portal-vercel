#!/bin/bash
echo "🚀 Starting DV Portal on anvilu.com..."
echo "================================================"

echo ""
echo "🌐 Domain: anvilu.com"
echo "👤 Admin: usadv27"
echo "📧 Email: esayasdesta00@gmail.com"
echo ""

echo "🔧 Starting Django server..."

# Option 1: Django development server on port 8080
echo "Starting on port 8080 (accessible at http://anvilu.com:8080)"
DJANGO_SETTINGS_MODULE=dv_portal.settings_production python manage.py runserver 0.0.0.0:8080

# Option 2: Gunicorn on port 8080 (uncomment to use)
# echo "Starting with Gunicorn on port 8080"
# gunicorn --bind 0.0.0.0:8080 dv_portal.wsgi:application

# Option 3: Gunicorn on port 80 with sudo (uncomment to use)
# echo "Starting with Gunicorn on port 80 (requires sudo)"
# sudo gunicorn --bind 0.0.0.0:80 dv_portal.wsgi:application
