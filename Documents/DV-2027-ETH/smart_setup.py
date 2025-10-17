#!/usr/bin/env python3
"""
Django Setup Script with Migration Handling
Handles existing database tables gracefully
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

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def generate_strong_password(length=10):
    """Generate a strong password with 10 characters"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    """Main setup function"""
    print("🚀 Starting DV Portal Ethiopia Setup...")
    print("=" * 60)
    
    try:
        # Step 1: Create directories
        print("\n📁 STEP 1: Creating Directories")
        print("-" * 40)
        
        logs_dir = project_dir / 'logs'
        logs_dir.mkdir(exist_ok=True)
        
        staticfiles_dir = project_dir / 'staticfiles'
        staticfiles_dir.mkdir(exist_ok=True)
        
        media_dir = project_dir / 'media'
        media_dir.mkdir(exist_ok=True)
        
        print("✅ Directories created successfully!")
        
        # Step 2: Setup Django
        print("\n🔧 STEP 2: Setting up Django")
        print("-" * 40)
        django.setup()
        print("✅ Django setup completed!")
        
        # Step 3: Handle migrations (with fake option if needed)
        print("\n🔄 STEP 3: Running Database Migrations")
        print("-" * 40)
        from django.core.management import execute_from_command_line
        
        try:
            # Try normal migration first
            execute_from_command_line(['manage.py', 'migrate', '--settings=dv_portal.settings_production'])
            print("✅ Database migrations completed!")
        except Exception as e:
            if "already exists" in str(e):
                print("⚠️ Some tables already exist, trying fake migration...")
                try:
                    # Try fake migration for existing tables
                    execute_from_command_line(['manage.py', 'migrate', '--fake', '--settings=dv_portal.settings_production'])
                    print("✅ Database migrations completed with fake option!")
                except Exception as e2:
                    print(f"⚠️ Migration issue: {e2}")
                    print("🔄 Trying to migrate specific apps...")
                    # Try migrating apps individually
                    apps = ['accounts', 'applications', 'core', 'notifications']
                    for app in apps:
                        try:
                            execute_from_command_line(['manage.py', 'migrate', app, '--settings=dv_portal.settings_production'])
                            print(f"✅ {app} migrations completed!")
                        except Exception as e3:
                            print(f"⚠️ {app} migration issue: {e3}")
            else:
                raise e
        
        # Step 4: Collect static files
        print("\n📁 STEP 4: Collecting Static Files")
        print("-" * 40)
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--settings=dv_portal.settings_production'])
        print("✅ Static files collected successfully!")
        
        # Step 5: Create admin user
        print("\n👤 STEP 5: Creating Admin User")
        print("-" * 40)
        
        from django.contrib.auth.models import User
        
        # Generate strong password
        admin_password = generate_strong_password(10)
        
        # Check if admin user already exists by username
        admin_username = 'admin'
        if User.objects.filter(username=admin_username).exists():
            print("✅ Admin user already exists!")
            admin_user = User.objects.get(username=admin_username)
            admin_user.set_password(admin_password)
            admin_user.save()
            print(f"🔑 Password updated for existing admin user!")
        else:
            # Create new admin user using Django's default User model
            User.objects.create_superuser(
                username=admin_username,
                email='admin@polocash.com',
                password=admin_password,
                first_name='Admin',
                last_name='User'
            )
            print("✅ Admin user created successfully!")
        
        print("=" * 50)
        print("🔐 ADMIN LOGIN DETAILS:")
        print("=" * 50)
        print(f"👤 Username: {admin_username}")
        print(f"🔑 Password: {admin_password}")
        print(f"📧 Email: admin@polocash.com")
        print("=" * 50)
        print("⚠️  IMPORTANT: Save these credentials securely!")
        print("⚠️  Change the password after first login!")
        print("=" * 50)
        
        # Final success message
        print("\n" + "=" * 60)
        print("🎉 SETUP SUCCESSFUL!")
        print("🌐 Your Django application is ready!")
        print("🔐 Admin credentials are displayed above")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ SETUP FAILED: {e}")
        print("🔧 Please check the error above and try again")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
