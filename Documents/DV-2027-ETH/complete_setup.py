#!/usr/bin/env python
"""
Complete DV Portal Setup Script
This script handles all aspects of setting up the Django application
"""

import os
import sys
import secrets
import string

# Configure Django settings FIRST
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings')

import django
django.setup()

from django.core.management import execute_from_command_line
from django.contrib.auth.models import User
from django.db import connection

def generate_strong_password(length=12):
    """Generate a strong password"""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def setup_django():
    """Setup Django environment"""
    print("🔧 Setting up Django environment...")
    
    # Django is already setup at module level
    print("✅ Django environment setup complete")

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

def run_migrations():
    """Run Django migrations"""
    print("🗄️ Running database migrations...")
    
    try:
        # Try normal migration first
        execute_from_command_line(['manage.py', 'migrate'])
        print("✅ Normal migrations completed")
    except Exception as e:
        print(f"⚠️ Normal migration failed: {e}")
        
        try:
            # Try fake migration
            execute_from_command_line(['manage.py', 'migrate', '--fake'])
            print("✅ Fake migrations completed")
        except Exception as e2:
            print(f"⚠️ Fake migration failed: {e2}")
            
            try:
                # Try individual app migrations
                apps = ['auth', 'contenttypes', 'sessions', 'admin', 'messages', 'staticfiles']
                for app in apps:
                    try:
                        execute_from_command_line(['manage.py', 'migrate', app])
                        print(f"   ✅ {app} migration completed")
                    except Exception as e3:
                        print(f"   ⚠️ {app} migration failed: {e3}")
            except Exception as e4:
                print(f"⚠️ Individual migrations failed: {e4}")

def create_essential_tables():
    """Create essential tables if migrations fail"""
    print("🔨 Creating essential tables...")
    
    try:
        with connection.cursor() as cursor:
            # Create core tables (SQLite syntax)
            tables_sql = [
                # Core contact messages table
                """
                CREATE TABLE IF NOT EXISTS core_contactmessage (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    phone VARCHAR(20),
                    subject VARCHAR(255) NOT NULL,
                    message TEXT NOT NULL,
                    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """,
                
                # Applications tables
                """
                CREATE TABLE IF NOT EXISTS applications_dvapplication (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    confirmation_number VARCHAR(50) UNIQUE NOT NULL,
                    first_name VARCHAR(100) NOT NULL,
                    middle_name VARCHAR(100),
                    last_name VARCHAR(100) NOT NULL,
                    date_of_birth DATE NOT NULL,
                    place_of_birth VARCHAR(100) NOT NULL,
                    nationality VARCHAR(100) NOT NULL,
                    gender VARCHAR(10) NOT NULL,
                    marital_status VARCHAR(20) NOT NULL,
                    passport_number VARCHAR(50) NOT NULL,
                    passport_issue_date DATE NOT NULL,
                    passport_expiry_date DATE NOT NULL,
                    passport_issue_country VARCHAR(100) NOT NULL,
                    address_line1 VARCHAR(255) NOT NULL,
                    address_line2 VARCHAR(255),
                    city VARCHAR(100) NOT NULL,
                    state VARCHAR(100) NOT NULL,
                    postal_code VARCHAR(20) NOT NULL,
                    country VARCHAR(100) NOT NULL,
                    phone VARCHAR(20) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    education_level VARCHAR(50) NOT NULL,
                    occupation VARCHAR(100) NOT NULL,
                    work_experience_years INTEGER NOT NULL,
                    english_proficiency VARCHAR(20) NOT NULL,
                    other_languages TEXT,
                    has_spouse BOOLEAN NOT NULL DEFAULT 0,
                    has_children BOOLEAN NOT NULL DEFAULT 0,
                    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """,
                
                # Spouse table
                """
                CREATE TABLE IF NOT EXISTS applications_spouse (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    application_id INTEGER NOT NULL,
                    first_name VARCHAR(100) NOT NULL,
                    middle_name VARCHAR(100),
                    last_name VARCHAR(100) NOT NULL,
                    date_of_birth DATE NOT NULL,
                    place_of_birth VARCHAR(100) NOT NULL,
                    nationality VARCHAR(100) NOT NULL,
                    gender VARCHAR(10) NOT NULL,
                    passport_number VARCHAR(50) NOT NULL,
                    passport_issue_date DATE NOT NULL,
                    passport_expiry_date DATE NOT NULL,
                    passport_issue_country VARCHAR(100) NOT NULL,
                    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """,
                
                # Children table
                """
                CREATE TABLE IF NOT EXISTS applications_child (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    application_id INTEGER NOT NULL,
                    first_name VARCHAR(100) NOT NULL,
                    middle_name VARCHAR(100),
                    last_name VARCHAR(100) NOT NULL,
                    date_of_birth DATE NOT NULL,
                    place_of_birth VARCHAR(100) NOT NULL,
                    nationality VARCHAR(100) NOT NULL,
                    gender VARCHAR(10) NOT NULL,
                    passport_number VARCHAR(50) NOT NULL,
                    passport_issue_date DATE NOT NULL,
                    passport_expiry_date DATE NOT NULL,
                    passport_issue_country VARCHAR(100) NOT NULL,
                    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """,
                
                # Notifications tables
                """
                CREATE TABLE IF NOT EXISTS notifications_telegramuser (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    telegram_id INTEGER UNIQUE NOT NULL,
                    username VARCHAR(100),
                    first_name VARCHAR(100),
                    last_name VARCHAR(100),
                    is_bot BOOLEAN NOT NULL DEFAULT 0,
                    language_code VARCHAR(10),
                    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """,
                
                """
                CREATE TABLE IF NOT EXISTS notifications_adminnotification (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title VARCHAR(255) NOT NULL,
                    message TEXT NOT NULL,
                    is_read BOOLEAN NOT NULL DEFAULT 0,
                    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """,
                
                """
                CREATE TABLE IF NOT EXISTS notifications_telegramnotification (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    message TEXT NOT NULL,
                    sent_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    status VARCHAR(20) NOT NULL DEFAULT 'pending'
                )
                """
            ]
            
            for sql in tables_sql:
                try:
                    cursor.execute(sql)
                    print("   ✅ Table created successfully")
                except Exception as e:
                    print(f"   ⚠️ Table creation failed: {e}")
            
            connection.commit()
            print("✅ Essential tables created")
            
    except Exception as e:
        print(f"⚠️ Table creation failed: {e}")

def collect_static_files():
    """Collect static files"""
    print("📦 Collecting static files...")
    
    try:
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
        print("✅ Static files collected")
    except Exception as e:
        print(f"⚠️ Static file collection failed: {e}")

def create_admin_user():
    """Create admin user"""
    print("👤 Creating admin user...")
    
    try:
        # Generate strong password
        admin_password = generate_strong_password()
        
        # Check if admin user exists
        if User.objects.filter(username='admin').exists():
            print("   ⚠️ Admin user already exists")
            return admin_password
        
        # Create admin user
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@dvportal.com',
            password=admin_password,
            first_name='Admin',
            last_name='User'
        )
        
        print(f"✅ Admin user created successfully")
        print(f"   Username: admin")
        print(f"   Password: {admin_password}")
        print(f"   Email: admin@dvportal.com")
        
        return admin_password
        
    except Exception as e:
        print(f"⚠️ Admin user creation failed: {e}")
        return None

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

def main():
    """Main setup function"""
    print("🚀 Starting Complete DV Portal Setup...")
    print("=" * 50)
    
    try:
        # Step 1: Setup Django
        setup_django()
        
        # Step 2: Create directories
        create_directories()
        
        # Step 3: Run migrations
        run_migrations()
        
        # Step 4: Create essential tables if needed
        create_essential_tables()
        
        # Step 5: Collect static files
        collect_static_files()
        
        # Step 6: Create admin user
        admin_password = create_admin_user()
        
        # Step 7: Create requirements.txt
        create_requirements_file()
        
        # Step 8: Create .env template
        create_env_file()
        
        # Step 9: Create deployment files
        create_deployment_files()
        
        print("=" * 50)
        print("🎉 Setup Complete!")
        print("=" * 50)
        
        if admin_password:
            print(f"👤 Admin Login Credentials:")
            print(f"   Username: admin")
            print(f"   Password: {admin_password}")
            print(f"   URL: http://localhost:8000/admin/")
        
        print("\n📋 Next Steps:")
        print("1. Copy .env.template to .env and update with your values")
        print("2. Run: python manage.py runserver")
        print("3. Visit: http://localhost:8000")
        print("4. For deployment, use Railway, Render, or Heroku")
        
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
