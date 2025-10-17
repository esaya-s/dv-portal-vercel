#!/usr/bin/env python3
"""
Complete Deployment Script for DV Portal Ethiopia
This single script handles all deployment tasks
"""

import os
import sys
import django
import secrets
import string
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(project_dir))

# Set Django settings (will be called after directories are created)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

from django.core.management import execute_from_command_line
from django.contrib.auth import get_user_model
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def generate_strong_password(length=10):
    """Generate a strong password with 10 characters"""
    # Use a mix of letters, digits, and symbols
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def install_dependencies():
    """Install Python dependencies"""
    try:
        print("📦 Installing Python dependencies...")
        import subprocess
        
        # Try different pip commands
        pip_commands = [
            ['pip', 'install', '-r', 'requirements.txt'],
            ['pip3', 'install', '-r', 'requirements.txt'],
            ['python', '-m', 'pip', 'install', '-r', 'requirements.txt'],
            ['python3', '-m', 'pip', 'install', '-r', 'requirements.txt']
        ]
        
        for cmd in pip_commands:
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
                if result.returncode == 0:
                    print("✅ Dependencies installed successfully!")
                    return True
                else:
                    print(f"⚠️ Command failed: {' '.join(cmd)}")
                    print(f"Error: {result.stderr}")
            except Exception as e:
                print(f"⚠️ Command error: {' '.join(cmd)} - {e}")
                continue
        
        print("❌ All pip commands failed. Please install manually.")
        return False
        
    except Exception as e:
        print(f"❌ Dependency installation failed: {e}")
        return False

def run_migrations():
    """Run database migrations"""
    try:
        print("🔄 Running database migrations...")
        execute_from_command_line(['manage.py', 'migrate', '--settings=dv_portal.settings_production'])
        print("✅ Database migrations completed successfully!")
        return True
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False

def collect_static_files():
    """Collect static files"""
    try:
        print("📁 Collecting static files...")
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--settings=dv_portal.settings_production'])
        print("✅ Static files collected successfully!")
        return True
    except Exception as e:
        print(f"❌ Static collection failed: {e}")
        return False

def create_superuser():
    """Create superuser with strong password"""
    try:
        print("👤 Creating admin user...")
        
        User = get_user_model()
        
        # Generate strong password
        admin_password = generate_strong_password(10)
        
        # Check if admin user already exists
        if User.objects.filter(username='admin').exists():
            print("✅ Admin user already exists!")
            # Update password for existing user
            admin_user = User.objects.get(username='admin')
            admin_user.set_password(admin_password)
            admin_user.save()
            print(f"🔑 Password updated for existing admin user!")
        else:
            # Create new admin user
            User.objects.create_superuser(
                username='admin',
                email='admin@polocash.com',
                password=admin_password
            )
            print("✅ Admin user created successfully!")
        
        print("=" * 50)
        print("🔐 ADMIN LOGIN DETAILS:")
        print("=" * 50)
        print(f"👤 Username: admin")
        print(f"🔑 Password: {admin_password}")
        print(f"📧 Email: admin@polocash.com")
        print("=" * 50)
        print("⚠️  IMPORTANT: Save these credentials securely!")
        print("⚠️  Change the password after first login!")
        print("=" * 50)
        
        return True
        
    except Exception as e:
        print(f"❌ Superuser creation failed: {e}")
        return False

def start_telegram_bot():
    """Start the Telegram bot"""
    try:
        print("🤖 Starting Telegram bot...")
        
        # Check if bot token is configured
        from django.conf import settings
        if not settings.TELEGRAM_BOT_TOKEN:
            print("⚠️ TELEGRAM_BOT_TOKEN is not configured!")
            print("📝 Please set TELEGRAM_BOT_TOKEN in environment variables")
            return False
            
        print("✅ Bot token found, starting bot...")
        from notifications.telegram_bot import start_bot
        start_bot()
        
        print("✅ Telegram bot started successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Failed to start Telegram bot: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    try:
        print("📁 Creating necessary directories...")
        
        # Create logs directory
        logs_dir = project_dir / 'logs'
        logs_dir.mkdir(exist_ok=True)
        
        # Create staticfiles directory
        staticfiles_dir = project_dir / 'staticfiles'
        staticfiles_dir.mkdir(exist_ok=True)
        
        # Create media directory
        media_dir = project_dir / 'media'
        media_dir.mkdir(exist_ok=True)
        
        print("✅ Directories created successfully!")
        
        # Now setup Django after directories exist
        print("🔧 Setting up Django...")
        django.setup()
        print("✅ Django setup completed!")
        
        return True
        
    except Exception as e:
        print(f"❌ Directory creation failed: {e}")
        return False

def main():
    """Main deployment function"""
    print("🚀 Starting DV Portal Ethiopia Deployment...")
    print("=" * 60)
    
    success_count = 0
    total_steps = 6
    
    # Step 0: Create directories
    print("\n📁 STEP 0: Creating Directories")
    print("-" * 40)
    if create_directories():
        success_count += 1
    
    # Step 1: Install dependencies
    print("\n📦 STEP 1: Installing Dependencies")
    print("-" * 40)
    if install_dependencies():
        success_count += 1
    
    # Step 2: Run migrations
    print("\n🔄 STEP 2: Database Migrations")
    print("-" * 40)
    if run_migrations():
        success_count += 1
    
    # Step 3: Collect static files
    print("\n📁 STEP 3: Collecting Static Files")
    print("-" * 40)
    if collect_static_files():
        success_count += 1
    
    # Step 4: Create superuser
    print("\n👤 STEP 4: Creating Admin User")
    print("-" * 40)
    if create_superuser():
        success_count += 1
    
    # Step 5: Start Telegram bot
    print("\n🤖 STEP 5: Starting Telegram Bot")
    print("-" * 40)
    if start_telegram_bot():
        success_count += 1
    
    # Final results
    print("\n" + "=" * 60)
    print("🎯 DEPLOYMENT SUMMARY")
    print("=" * 60)
    print(f"✅ Completed: {success_count}/{total_steps} steps")
    
    if success_count == total_steps:
        print("🎉 DEPLOYMENT SUCCESSFUL!")
        print("🌐 Your Django application is now running!")
        print("🤖 Telegram bot is active!")
    elif success_count >= 3:
        print("⚠️ PARTIAL SUCCESS")
        print("🔧 Some steps failed, but core functionality should work")
    else:
        print("❌ DEPLOYMENT FAILED")
        print("🔧 Please check the errors above and try again")
    
    print("=" * 60)
    
    return success_count >= 3

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
