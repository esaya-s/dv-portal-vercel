#!/bin/bash
echo "🌐 Setting up Django for anvilu.com (without root access)..."
echo "================================================"

echo ""
echo "📋 Since you don't have root access, we'll use port 8080"
echo "🌐 Your site will be available at: http://anvilu.com:8080"
echo ""

echo "🔧 Starting Django with production settings..."

# Start Django on port 8080
DJANGO_SETTINGS_MODULE=dv_portal.settings_production python manage.py runserver 0.0.0.0:8080

echo ""
echo "✅ Django is now running on port 8080"
echo "🌐 Access your site at: http://anvilu.com:8080"
echo "👤 Admin panel: http://anvilu.com:8080/admin/"
echo "📧 Username: usadv27"
echo ""
echo "💡 To hide the port number, you can:"
echo "1. Use a reverse proxy service (like Cloudflare)"
echo "2. Set up port forwarding in your hosting control panel"
echo "3. Use a subdomain like app.anvilu.com"
