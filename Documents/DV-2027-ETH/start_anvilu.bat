@echo off
echo 🚀 Starting DV Portal on anvilu.com...
echo ================================================

echo.
echo 🌐 Domain: anvilu.com
echo 👤 Admin: usadv27
echo 📧 Email: esayasdesta00@gmail.com
echo.

echo 🔧 Starting Django server...

REM Option 1: Django development server on port 8080
echo Starting on port 8080 (accessible at http://anvilu.com:8080)
set DJANGO_SETTINGS_MODULE=dv_portal.settings_production
python manage.py runserver 0.0.0.0:8080

REM Option 2: Gunicorn on port 8080 (uncomment to use)
REM echo Starting with Gunicorn on port 8080
REM gunicorn --bind 0.0.0.0:8080 dv_portal.wsgi:application

REM Option 3: Gunicorn on port 80 with sudo (uncomment to use)
REM echo Starting with Gunicorn on port 80 (requires sudo)
REM sudo gunicorn --bind 0.0.0.0:80 dv_portal.wsgi:application

pause
