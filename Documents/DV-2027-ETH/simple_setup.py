#!/usr/bin/env python
"""
Simple DV Portal Setup Script
This script handles basic setup without external dependencies
"""

import os
import sys
import secrets
import string

def generate_strong_password(length=12):
    """Generate a strong password"""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def create_directories():
    """Create necessary directories"""
    print("📁 Creating necessary directories...")
    
    directories = [
        'staticfiles',
        'media',
        'logs',
        'static/core',
        'static/applications',
        'static/notifications'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"   Created: {directory}")
    
    print("✅ Directories created")

def run_django_commands():
    """Run Django management commands"""
    print("🔧 Running Django setup commands...")
    
    commands = [
        ['python', 'manage.py', 'migrate'],
        ['python', 'manage.py', 'collectstatic', '--noinput'],
        ['python', 'manage.py', 'createsuperuser', '--username', 'admin', '--email', 'admin@dvportal.com', '--noinput']
    ]
    
    for cmd in commands:
        try:
            print(f"   Running: {' '.join(cmd)}")
            result = os.system(' '.join(cmd))
            if result == 0:
                print(f"   ✅ Command successful")
            else:
                print(f"   ⚠️ Command failed with code {result}")
        except Exception as e:
            print(f"   ⚠️ Command failed: {e}")

def create_requirements_file():
    """Create requirements.txt file"""
    print("📋 Creating requirements.txt...")
    
    requirements = """Django>=4.2.0
crispy-forms>=2.0
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
"""
    
    try:
        with open('requirements.txt', 'w') as f:
            f.write(requirements)
        print("✅ requirements.txt created")
    except Exception as e:
        print(f"⚠️ requirements.txt creation failed: {e}")

def create_env_file():
    """Create .env file template"""
    print("🔐 Creating .env template...")
    
    env_content = """# Django Settings
SECRET_KEY=your-secret-key-here-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database Settings (SQLite - no additional config needed)
# DATABASE_URL=sqlite:///db_new.sqlite3

# Telegram Bot Settings
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
TELEGRAM_BOT_USERNAME=your-bot-username
TELEGRAM_ADMIN_CHAT_ID=your-admin-chat-id
TELEGRAM_ADMIN_USERNAME=your-admin-username

# Email Settings
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_PORT=587
EMAIL_USE_TLS=True

# Payment Settings
PAYMENT_AMOUNT=800
PAYMENT_CURRENCY=ETB

# Gemini API (optional)
GEMINI_API_KEY=your-gemini-api-key
"""
    
    try:
        with open('.env.template', 'w') as f:
            f.write(env_content)
        print("✅ .env.template created")
        print("   📝 Copy .env.template to .env and update with your values")
    except Exception as e:
        print(f"⚠️ .env.template creation failed: {e}")

def create_deployment_files():
    """Create deployment configuration files"""
    print("🚀 Creating deployment files...")
    
    # Procfile for Railway/Heroku
    procfile_content = """web: gunicorn dv_portal.wsgi:application --bind 0.0.0.0:$PORT
"""
    
    try:
        with open('Procfile', 'w') as f:
            f.write(procfile_content)
        print("✅ Procfile created")
    except Exception as e:
        print(f"⚠️ Procfile creation failed: {e}")
    
    # Railway configuration
    railway_config = """{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "gunicorn dv_portal.wsgi:application --bind 0.0.0.0:$PORT",
    "healthcheckPath": "/",
    "healthcheckTimeout": 100,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
"""
    
    try:
        with open('railway.json', 'w') as f:
            f.write(railway_config)
        print("✅ railway.json created")
    except Exception as e:
        print(f"⚠️ railway.json creation failed: {e}")

def create_simple_settings():
    """Create a simple settings file without decouple"""
    print("⚙️ Creating simple settings file...")
    
    simple_settings = """"""
    
    try:
        with open('dv_portal/settings_simple.py', 'w') as f:
            f.write(simple_settings)
        print("✅ Simple settings created")
    except Exception as e:
        print(f"⚠️ Simple settings creation failed: {e}")

def main():
    """Main setup function"""
    print("🚀 Starting Simple DV Portal Setup...")
    print("=" * 50)
    
    try:
        # Step 1: Create directories
        create_directories()
        
        # Step 2: Run Django commands
        run_django_commands()
        
        # Step 3: Create requirements.txt
        create_requirements_file()
        
        # Step 4: Create .env template
        create_env_file()
        
        # Step 5: Create deployment files
        create_deployment_files()
        
        print("=" * 50)
        print("🎉 Simple Setup Complete!")
        print("=" * 50)
        
        print(f"👤 Admin Login Credentials:")
        print(f"   Username: admin")
        print(f"   Password: (set during createsuperuser)")
        print(f"   URL: http://localhost:8000/admin/")
        
        print("\n📋 Next Steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Copy .env.template to .env and update with your values")
        print("3. Run: python manage.py runserver")
        print("4. Visit: http://localhost:8000")
        print("5. For deployment, use Railway, Render, or Heroku")
        
        print("\n🚀 Deployment Options:")
        print("• Railway: railway.app (Recommended)")
        print("• Render: render.com")
        print("• Heroku: heroku.com")
        print("• PythonAnywhere: pythonanywhere.com")
        
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()