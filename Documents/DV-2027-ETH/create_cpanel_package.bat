@echo off
echo 📦 Creating cPanel Django Deployment Package
echo ================================================

echo.
echo 🔧 Creating deployment package for cPanel...

REM Create deployment directory
mkdir cpanel_deployment 2>nul

echo 📁 Copying Django files...
xcopy dv_portal cpanel_deployment\dv_portal /E /I
xcopy core cpanel_deployment\core /E /I
xcopy applications cpanel_deployment\applications /E /I
xcopy notifications cpanel_deployment\notifications /E /I
xcopy templates cpanel_deployment\templates /E /I
xcopy static cpanel_deployment\static /E /I
copy manage.py cpanel_deployment\
copy requirements_basic.txt cpanel_deployment\
copy passenger_wsgi.py cpanel_deployment\
copy .htaccess cpanel_deployment\

echo 📝 Creating requirements.txt...
echo Django>=4.2.0,<5.0.0 > cpanel_deployment\requirements.txt
echo django-crispy-forms>=2.0 >> cpanel_deployment\requirements.txt
echo crispy-bootstrap5>=0.7 >> cpanel_deployment\requirements.txt
echo django-countries>=7.5.1 >> cpanel_deployment\requirements.txt
echo django-phonenumber-field>=7.1.0 >> cpanel_deployment\requirements.txt
echo phonenumbers>=8.13.0 >> cpanel_deployment\requirements.txt
echo python-telegram-bot>=20.0 >> cpanel_deployment\requirements.txt
echo Pillow>=10.0.0 >> cpanel_deployment\requirements.txt
echo whitenoise>=6.5.0 >> cpanel_deployment\requirements.txt
echo gunicorn>=21.2.0 >> cpanel_deployment\requirements.txt
echo python-dotenv>=1.0.0 >> cpanel_deployment\requirements.txt
echo python-decouple>=3.8 >> cpanel_deployment\requirements.txt

echo 📖 Creating deployment instructions...
echo 🚀 Django Deployment Instructions for cPanel > cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo ================================================ >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo. >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo 📋 Prerequisites: >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo - cPanel with Python App support >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo - Python 3.8+ enabled >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo. >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo 🔧 Deployment Steps: >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo. >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo 1. Upload Files: >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo    - Upload this entire folder to your cPanel public_html directory >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo. >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo 2. Create Python App in cPanel: >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo    - Go to "Python App" in cPanel >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo    - Create a new Python application >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo    - Set the app directory to: public_html/cpanel_deployment >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo    - Set the app URL to: anvilu.com >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo    - Choose Python version 3.8 or higher >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo. >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo 3. Install Dependencies: >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo    - In the Python App interface, go to "Packages" >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo    - Install the packages from requirements.txt >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo. >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo 4. Run Django Commands: >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo    - In Python App terminal, run: >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo      python manage.py migrate >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo      python manage.py collectstatic --noinput >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo      python manage.py createsuperuser >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo. >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo 5. Start the Application: >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo    - The Python App should automatically start >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo. >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo 🌐 Access Your Site: >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo - Main Site: http://anvilu.com >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo - Admin Panel: http://anvilu.com/admin/ >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo. >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo 👤 Admin Credentials: >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo - Username: admin >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt
echo - Password: admin123 >> cpanel_deployment\DEPLOYMENT_INSTRUCTIONS.txt

echo.
echo ✅ cPanel deployment package created!
echo.
echo 📁 Files created:
echo    - cpanel_deployment\ (folder)
echo.
echo 📋 Next steps:
echo 1. Upload cpanel_deployment folder to your cPanel
echo 2. Extract it in public_html/
echo 3. Create Python App in cPanel
echo 4. Run Django commands
echo.
echo 🌐 Your site will be available at: http://anvilu.com
echo.
pause
