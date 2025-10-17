#!/usr/bin/env python3
"""
Quick Vercel Deployment Script for Django DV Portal
"""

import os
import subprocess
import sys
import zipfile
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def create_vercel_package():
    """Create Vercel deployment package"""
    print("🚀 Creating Vercel Deployment Package")
    print("=" * 50)
    
    # Create deployment directory
    deploy_dir = Path("vercel_deployment")
    if deploy_dir.exists():
        import shutil
        shutil.rmtree(deploy_dir)
    deploy_dir.mkdir()
    
    # Copy essential files and directories
    essential_items = [
        "dv_portal",
        "core", 
        "applications",
        "notifications",
        "templates",
        "static",
        "manage.py",
        "vercel.json",
        "api"
    ]
    
    for item in essential_items:
        if Path(item).exists():
            if Path(item).is_dir():
                run_command(f"xcopy /E /I {item} vercel_deployment\\{item}", f"Copying {item}")
            else:
                run_command(f"copy {item} vercel_deployment\\", f"Copying {item}")
    
    # Copy requirements
    run_command("copy requirements_vercel.txt vercel_deployment\\requirements.txt", "Copying requirements")
    
    # Create .vercelignore
    vercelignore_content = """# Django
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
"""
    
    with open("vercel_deployment/.vercelignore", "w", encoding="utf-8") as f:
        f.write(vercelignore_content)
    
    # Create deployment instructions
    instructions = """🚀 Django Deployment Instructions for Vercel
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
"""
    
    with open("vercel_deployment/DEPLOYMENT_INSTRUCTIONS.txt", "w", encoding="utf-8") as f:
        f.write(instructions)
    
    print("\n✅ Vercel deployment package created!")
    print("\n📁 Files created:")
    print("   - vercel_deployment/ (folder)")
    print("\n📋 Next steps:")
    print("1. Create GitHub repository")
    print("2. Upload vercel_deployment contents to GitHub")
    print("3. Connect to Vercel")
    print("4. Configure environment variables")
    print("5. Deploy!")
    print("\n🌐 Your site will be available at: https://anvilu.com")

if __name__ == "__main__":
    create_vercel_package()
