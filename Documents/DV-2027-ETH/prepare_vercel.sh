#!/bin/bash
echo "🚀 Preparing Django for Vercel Deployment"
echo "================================================"

echo ""
echo "📦 Creating Vercel deployment package..."

# Create vercel deployment directory
mkdir -p vercel_deployment

# Copy essential files
echo "📁 Copying Django files..."
cp -r dv_portal vercel_deployment/
cp -r core vercel_deployment/
cp -r applications vercel_deployment/
cp -r notifications vercel_deployment/
cp -r templates vercel_deployment/
cp -r static vercel_deployment/
cp manage.py vercel_deployment/
cp requirements_vercel.txt vercel_deployment/requirements.txt
cp vercel.json vercel_deployment/
cp -r api vercel_deployment/

# Create .vercelignore
echo "📝 Creating .vercelignore..."
cat > vercel_deployment/.vercelignore << 'EOF'
# Django
db.sqlite3
*.log
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
pip-log.txt
pip-delete-this-directory.txt
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git
.mypy_cache
.pytest_cache
.hypothesis

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Environment
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
EOF

# Create deployment instructions
echo "📖 Creating deployment instructions..."
cat > vercel_deployment/DEPLOYMENT_INSTRUCTIONS.txt << 'EOF'
🚀 Django Deployment Instructions for Vercel
===============================================

📋 Prerequisites:
- Vercel account (vercel.com)
- GitHub account
- PostgreSQL database (Vercel Postgres or external)

🔧 Deployment Steps:

1. Push to GitHub:
   - Create a new GitHub repository
   - Upload the vercel_deployment folder contents
   - Push to GitHub

2. Connect to Vercel:
   - Go to vercel.com
   - Click "New Project"
   - Import your GitHub repository
   - Choose "Django" as framework

3. Configure Environment Variables:
   - SECRET_KEY: Generate a new secret key
   - DEBUG: False
   - POSTGRES_DATABASE: Your database name
   - POSTGRES_USER: Your database user
   - POSTGRES_PASSWORD: Your database password
   - POSTGRES_HOST: Your database host
   - POSTGRES_PORT: 5432
   - TELEGRAM_BOT_TOKEN: Your bot token
   - TELEGRAM_ADMIN_CHAT_ID: Your admin chat ID

4. Deploy:
   - Click "Deploy"
   - Wait for deployment to complete

5. Set up Database:
   - Go to Vercel dashboard
   - Open your project
   - Go to "Functions" tab
   - Run: python manage.py migrate
   - Run: python manage.py collectstatic --noinput
   - Run: python manage.py createsuperuser

6. Custom Domain:
   - Go to "Domains" tab
   - Add anvilu.com
   - Configure DNS

🌐 Access Your Site:
- Main Site: https://anvilu.com
- Admin Panel: https://anvilu.com/admin/

👤 Admin Credentials:
- Username: admin
- Password: admin123

🔧 Troubleshooting:
- Check Vercel logs for errors
- Ensure all environment variables are set
- Verify database connection
- Test with: python manage.py check
EOF

# Create ZIP file
echo "📦 Creating ZIP file..."
zip -r vercel_deployment.zip vercel_deployment/

echo ""
echo "✅ Vercel deployment package created!"
echo ""
echo "📁 Files created:"
echo "   - vercel_deployment/ (folder)"
echo "   - vercel_deployment.zip (for upload)"
echo ""
echo "📋 Next steps:"
echo "1. Create GitHub repository"
echo "2. Upload vercel_deployment contents to GitHub"
echo "3. Connect to Vercel"
echo "4. Configure environment variables"
echo "5. Deploy!"
echo ""
echo "🌐 Your site will be available at: https://anvilu.com"
