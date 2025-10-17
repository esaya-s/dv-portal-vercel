#!/bin/bash
echo "📦 Creating Django Deployment Package"
echo "================================================"

echo ""
echo "🔧 Creating deployment package..."

# Create deployment directory
mkdir -p django_deployment

# Copy essential files
cp -r dv_portal django_deployment/
cp -r core django_deployment/
cp -r applications django_deployment/
cp -r notifications django_deployment/
cp -r templates django_deployment/
cp -r static django_deployment/
cp manage.py django_deployment/
cp requirements_basic.txt django_deployment/
cp passenger_wsgi.py django_deployment/
cp *.py django_deployment/

# Create .htaccess for cPanel
cat > django_deployment/.htaccess << 'EOF'
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ passenger_wsgi.py [QSA,L]

# Static files
RewriteRule ^static/(.*)$ static/$1 [L]
RewriteRule ^media/(.*)$ media/$1 [L]
EOF

# Create deployment instructions
cat > django_deployment/DEPLOYMENT_INSTRUCTIONS.txt << 'EOF'
🚀 Django Deployment Instructions for cPanel
===============================================

1. Upload this entire folder to your cPanel public_html directory

2. In cPanel Terminal, run:
   cd public_html/django_deployment
   pip install -r requirements_basic.txt
   python manage.py migrate
   python manage.py collectstatic --noinput
   python manage.py createsuperuser

3. Start the server:
   python manage.py runserver 0.0.0.0:8000

4. Access your site:
   http://anvilu.com:8000
   Admin: http://anvilu.com:8000/admin/

5. To hide port 8000, use Cloudflare Tunnel or cPanel port forwarding

Admin Credentials:
- Username: admin
- Password: admin123
EOF

# Create ZIP file
zip -r django_deployment.zip django_deployment/

echo ""
echo "✅ Deployment package created: django_deployment.zip"
echo ""
echo "📋 Next steps:"
echo "1. Upload django_deployment.zip to your cPanel"
echo "2. Extract it in public_html/"
echo "3. Run the deployment commands in cPanel terminal"
echo ""
echo "🌐 Your site will be available at: http://anvilu.com:8000"
