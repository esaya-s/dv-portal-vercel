#!/bin/bash
echo "📦 Creating cPanel Django Deployment Package"
echo "================================================"

echo ""
echo "🔧 Creating deployment package for cPanel..."

# Create deployment directory
mkdir -p cpanel_deployment

# Copy essential Django files
echo "📁 Copying Django files..."
cp -r dv_portal cpanel_deployment/
cp -r core cpanel_deployment/
cp -r applications cpanel_deployment/
cp -r notifications cpanel_deployment/
cp -r templates cpanel_deployment/
cp -r static cpanel_deployment/
cp manage.py cpanel_deployment/
cp requirements_basic.txt cpanel_deployment/
cp passenger_wsgi.py cpanel_deployment/

# Create .htaccess for cPanel
echo "📝 Creating .htaccess file..."
cat > cpanel_deployment/.htaccess << 'EOF'
RewriteEngine On

# Handle Django URLs
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ passenger_wsgi.py [QSA,L]

# Static files
RewriteRule ^static/(.*)$ static/$1 [L]
RewriteRule ^media/(.*)$ media/$1 [L]

# Security headers
Header always set X-Content-Type-Options nosniff
Header always set X-Frame-Options DENY
Header always set X-XSS-Protection "1; mode=block"

# Cache static files
<FilesMatch "\.(css|js|png|jpg|jpeg|gif|ico|svg)$">
    ExpiresActive On
    ExpiresDefault "access plus 1 month"
</FilesMatch>
EOF

# Create requirements.txt for cPanel
echo "📋 Creating requirements.txt..."
cat > cpanel_deployment/requirements.txt << 'EOF'
Django>=4.2.0,<5.0.0
django-crispy-forms>=2.0
crispy-bootstrap5>=0.7
django-countries>=7.5.1
django-phonenumber-field>=7.1.0
phonenumbers>=8.13.0
python-telegram-bot>=20.0
Pillow>=10.0.0
whitenoise>=6.5.0
gunicorn>=21.2.0
python-dotenv>=1.0.0
python-decouple>=3.8
EOF

# Create deployment instructions
echo "📖 Creating deployment instructions..."
cat > cpanel_deployment/DEPLOYMENT_INSTRUCTIONS.txt << 'EOF'
🚀 Django Deployment Instructions for cPanel
===============================================

📋 Prerequisites:
- cPanel with Python App support
- Python 3.8+ enabled

🔧 Deployment Steps:

1. Upload Files:
   - Upload this entire folder to your cPanel public_html directory
   - Or upload the ZIP file and extract it in public_html/

2. Create Python App in cPanel:
   - Go to "Python App" in cPanel
   - Create a new Python application
   - Set the app directory to: public_html/cpanel_deployment
   - Set the app URL to: anvilu.com (or your domain)
   - Choose Python version 3.8 or higher

3. Install Dependencies:
   - In the Python App interface, go to "Packages"
   - Install the packages from requirements.txt
   - Or run: pip install -r requirements.txt

4. Run Django Commands:
   - In Python App terminal, run:
     python manage.py migrate
     python manage.py collectstatic --noinput
     python manage.py createsuperuser

5. Start the Application:
   - The Python App should automatically start
   - Or manually start it from the Python App interface

🌐 Access Your Site:
- Main Site: http://anvilu.com
- Admin Panel: http://anvilu.com/admin/

👤 Admin Credentials:
- Username: admin
- Password: admin123

🔧 Troubleshooting:
- Check Python App logs for errors
- Ensure all dependencies are installed
- Verify .htaccess file is in place
- Check file permissions (755 for directories, 644 for files)

📞 Support:
- Check cPanel Python App documentation
- Verify Django settings are correct
- Test with: python manage.py check
EOF

# Create a simple setup script
echo "🔧 Creating setup script..."
cat > cpanel_deployment/setup.py << 'EOF'
#!/usr/bin/env python
"""
Quick setup script for cPanel Django deployment
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

# Setup Django
django.setup()

def main():
    print("🚀 Setting up Django for cPanel...")
    
    try:
        # Run migrations
        print("🗄️ Running migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        # Collect static files
        print("📦 Collecting static files...")
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
        
        # Create admin user
        print("👤 Creating admin user...")
        from django.contrib.auth.models import User
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@anvilu.com', 'admin123')
            print("✅ Admin user created: admin/admin123")
        else:
            print("✅ Admin user already exists")
        
        print("🎉 Setup complete!")
        print("🌐 Your site should be available at: http://anvilu.com")
        
    except Exception as e:
        print(f"❌ Setup failed: {e}")

if __name__ == "__main__":
    main()
EOF

# Create ZIP file
echo "📦 Creating ZIP file..."
zip -r cpanel_deployment.zip cpanel_deployment/

echo ""
echo "✅ cPanel deployment package created!"
echo ""
echo "📁 Files created:"
echo "   - cpanel_deployment/ (folder)"
echo "   - cpanel_deployment.zip (for upload)"
echo ""
echo "📋 Next steps:"
echo "1. Upload cpanel_deployment.zip to your cPanel"
echo "2. Extract it in public_html/"
echo "3. Create Python App in cPanel"
echo "4. Run: python setup.py"
echo ""
echo "🌐 Your site will be available at: http://anvilu.com"
