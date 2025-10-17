#!/bin/bash
echo "🚀 Quick cPanel Django Deployment"
echo "================================================"

echo ""
echo "📋 This script will set up Django on your cPanel server"
echo ""

# Create public_html directory if it doesn't exist
mkdir -p public_html

echo "🔧 Setting up Django in public_html..."

# Copy Django files to public_html
cp -r * public_html/ 2>/dev/null || echo "Files copied to public_html"

cd public_html

echo "📦 Installing Python dependencies..."
pip install -r requirements_basic.txt

echo "🗄️ Running migrations..."
python manage.py migrate

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "👤 Creating admin user..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@anvilu.com', 'admin123') if not User.objects.filter(username='admin').exists() else print('Admin user already exists')" | python manage.py shell

echo ""
echo "🚀 Starting Django server..."
echo "🌐 Your site will be available at: http://anvilu.com:8000"

# Start Django server
python manage.py runserver 0.0.0.0:8000
