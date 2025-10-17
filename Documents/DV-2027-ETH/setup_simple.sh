#!/bin/bash
echo "🚀 Starting Simple DV Portal Setup..."
echo "================================================"

echo ""
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "🔧 Running Django setup commands..."

# Set Django settings to use simple version
export DJANGO_SETTINGS_MODULE=dv_portal.settings_simple

echo "   Running migrations..."
python manage.py migrate

echo "   Collecting static files..."
python manage.py collectstatic --noinput

echo "   Creating admin user..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@dvportal.com', 'admin123') if not User.objects.filter(username='admin').exists() else print('Admin user already exists')" | python manage.py shell

echo ""
echo "🎉 Simple Setup Complete!"
echo ""
echo "📋 Next steps:"
echo "1. Run: python manage.py runserver"
echo "2. Visit: http://localhost:8000"
echo "3. Admin: http://localhost:8000/admin/ (admin/admin123)"
echo ""
echo "🚀 For deployment, consider:"
echo "• Railway: railway.app (Recommended)"
echo "• Render: render.com"
echo "• Heroku: heroku.com"
echo "• PythonAnywhere: pythonanywhere.com"
echo ""
