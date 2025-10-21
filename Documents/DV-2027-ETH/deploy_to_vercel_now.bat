@echo off
echo 🚀 Deploy Django to Vercel - Quick Start
echo ================================================

echo.
echo 📋 Step 1: Go to Vercel
echo ================================================
echo 1. Open: https://vercel.com
echo 2. Sign up/Login with GitHub
echo 3. Click "New Project"
echo 4. Import: markous2/dv-portal-vercel
echo.

echo 📋 Step 2: Configure Project
echo ================================================
echo - Framework: Django
echo - Root Directory: ./
echo - Build Command: pip install -r requirements_vercel.txt
echo - Output Directory: ./
echo.

echo 📋 Step 3: Add Environment Variables
echo ================================================
echo Required:
echo SECRET_KEY=django-secret-key-change-in-production-2024
echo DEBUG=False
echo DJANGO_SETTINGS_MODULE=dv_portal.settings_vercel
echo.
echo Database (add your Vercel Postgres details):
echo POSTGRES_DATABASE=your-db-name
echo POSTGRES_USER=your-db-user
echo POSTGRES_PASSWORD=your-db-password
echo POSTGRES_HOST=your-db-host
echo POSTGRES_PORT=5432
echo.

echo 📋 Step 4: Deploy
echo ================================================
echo 1. Click "Deploy"
echo 2. Wait for completion
echo 3. Check build logs
echo.

echo 📋 Step 5: Set up Database
echo ================================================
echo After deployment:
echo 1. Go to Functions tab
echo 2. Run: python manage.py migrate
echo 3. Run: python manage.py collectstatic --noinput
echo 4. Run: python manage.py createsuperuser
echo.

echo 📋 Step 6: Add Custom Domain
echo ================================================
echo 1. Go to Domains tab
echo 2. Add: anvilu.com
echo 3. Add: www.anvilu.com
echo 4. Configure DNS
echo.

echo 🌐 Your Repository:
echo https://github.com/markous2/dv-portal-vercel
echo.

echo 🎉 After deployment:
echo - Main Site: https://anvilu.com
echo - Admin: https://anvilu.com/admin/
echo - Default Admin: admin / admin123
echo.

pause
