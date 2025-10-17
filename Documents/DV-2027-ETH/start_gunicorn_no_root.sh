#!/bin/bash
echo "🚀 Starting Django with Gunicorn (no root access)..."
echo "================================================"

echo ""
echo "🔧 Starting Gunicorn on port 8080..."

# Start Gunicorn on port 8080
gunicorn --bind 0.0.0.0:8080 --workers 3 --timeout 120 dv_portal.wsgi:application

echo ""
echo "✅ Gunicorn is now running on port 8080"
echo "🌐 Access your site at: http://anvilu.com:8080"
echo "👤 Admin panel: http://anvilu.com:8080/admin/"
echo "📧 Username: usadv27"
echo ""
echo "💡 To run in background:"
echo "nohup gunicorn --bind 0.0.0.0:8080 --workers 3 --timeout 120 dv_portal.wsgi:application &"
