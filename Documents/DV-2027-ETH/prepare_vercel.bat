@echo off
echo 🚀 Preparing Django for Vercel Deployment
echo ================================================

echo.
echo 📦 Creating Vercel deployment package...

REM Create vercel deployment directory
if not exist vercel_deployment mkdir vercel_deployment

REM Copy essential files
echo 📁 Copying Django files...
xcopy /E /I dv_portal vercel_deployment\dv_portal
xcopy /E /I core vercel_deployment\core
xcopy /E /I applications vercel_deployment\applications
xcopy /E /I notifications vercel_deployment\notifications
xcopy /E /I templates vercel_deployment\templates
xcopy /E /I static vercel_deployment\static
copy manage.py vercel_deployment\
copy requirements_vercel.txt vercel_deployment\requirements.txt
copy vercel.json vercel_deployment\
xcopy /E /I api vercel_deployment\api

REM Create .vercelignore
echo 📝 Creating .vercelignore...
(
echo # Django
echo db.sqlite3
echo *.log
echo __pycache__/
echo *.pyc
echo *.pyo
echo *.pyd
echo .Python
echo env/
echo venv/
echo .venv/
echo pip-log.txt
echo pip-delete-this-directory.txt
echo .tox/
echo .coverage
echo .coverage.*
echo .cache
echo nosetests.xml
echo coverage.xml
echo *.cover
echo *.log
echo .git
echo .mypy_cache
echo .pytest_cache
echo .hypothesis
echo.
echo # OS
echo .DS_Store
echo .DS_Store?
echo ._*
echo .Spotlight-V100
echo .Trashes
echo ehthumbs.db
echo Thumbs.db
echo.
echo # IDE
echo .vscode/
echo .idea/
echo *.swp
echo *.swo
echo *~
echo.
echo # Environment
echo .env
echo .env.local
echo .env.development.local
echo .env.test.local
echo .env.production.local
) > vercel_deployment\.vercelignore

REM Create deployment instructions
echo 📖 Creating deployment instructions...
(
echo 🚀 Django Deployment Instructions for Vercel
echo ===============================================
echo.
echo 📋 Prerequisites:
echo - Vercel account ^(vercel.com^)
echo - GitHub account
echo - PostgreSQL database ^(Vercel Postgres or external^)
echo.
echo 🔧 Deployment Steps:
echo.
echo 1. Push to GitHub:
echo    - Create a new GitHub repository
echo    - Upload the vercel_deployment folder contents
echo    - Push to GitHub
echo.
echo 2. Connect to Vercel:
echo    - Go to vercel.com
echo    - Click "New Project"
echo    - Import your GitHub repository
echo    - Choose "Django" as framework
echo.
echo 3. Configure Environment Variables:
echo    - SECRET_KEY: Generate a new secret key
echo    - DEBUG: False
echo    - POSTGRES_DATABASE: Your database name
echo    - POSTGRES_USER: Your database user
echo    - POSTGRES_PASSWORD: Your database password
echo    - POSTGRES_HOST: Your database host
echo    - POSTGRES_PORT: 5432
echo    - TELEGRAM_BOT_TOKEN: Your bot token
echo    - TELEGRAM_ADMIN_CHAT_ID: Your admin chat ID
echo.
echo 4. Deploy:
echo    - Click "Deploy"
echo    - Wait for deployment to complete
echo.
echo 5. Set up Database:
echo    - Go to Vercel dashboard
echo    - Open your project
echo    - Go to "Functions" tab
echo    - Run: python manage.py migrate
echo    - Run: python manage.py collectstatic --noinput
echo    - Run: python manage.py createsuperuser
echo.
echo 6. Custom Domain:
echo    - Go to "Domains" tab
echo    - Add anvilu.com
echo    - Configure DNS
echo.
echo 🌐 Access Your Site:
echo - Main Site: https://anvilu.com
echo - Admin Panel: https://anvilu.com/admin/
echo.
echo 👤 Admin Credentials:
echo - Username: admin
echo - Password: admin123
echo.
echo 🔧 Troubleshooting:
echo - Check Vercel logs for errors
echo - Ensure all environment variables are set
echo - Verify database connection
echo - Test with: python manage.py check
) > vercel_deployment\DEPLOYMENT_INSTRUCTIONS.txt

echo.
echo ✅ Vercel deployment package created!
echo.
echo 📁 Files created:
echo    - vercel_deployment\ ^(folder^)
echo.
echo 📋 Next steps:
echo 1. Create GitHub repository
echo 2. Upload vercel_deployment contents to GitHub
echo 3. Connect to Vercel
echo 4. Configure environment variables
echo 5. Deploy!
echo.
echo 🌐 Your site will be available at: https://anvilu.com
echo.
pause
