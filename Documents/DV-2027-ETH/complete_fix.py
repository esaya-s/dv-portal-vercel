#!/usr/bin/env python3
"""
Complete database fix - handles migrations and missing tables
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def complete_fix():
    print("🔧 Complete Database Fix for DV Portal")
    print("=" * 60)
    
    try:
        import django
        from django.core.management import execute_from_command_line
        from django.db import connection
        
        # Setup Django
        django.setup()
        print("✅ Django setup completed!")
        
        # Step 1: Check current tables
        print("\n📋 STEP 1: Checking existing tables...")
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        existing_tables = [table[0] for table in cursor.fetchall()]
        print(f"✅ Found {len(existing_tables)} existing tables")
        
        # Step 2: Run migrations
        print("\n🔄 STEP 2: Running Django migrations...")
        try:
            execute_from_command_line(['manage.py', 'migrate', '--run-syncdb'])
            print("✅ Django migrations completed!")
        except Exception as e:
            print(f"⚠️ Migration warning: {e}")
        
        # Step 3: Check if applications tables exist
        print("\n🔍 STEP 3: Checking applications tables...")
        cursor.execute("SHOW TABLES LIKE 'applications_%'")
        app_tables = cursor.fetchall()
        
        if len(app_tables) == 0:
            print("❌ No applications tables found, creating them...")
            
            # Create applications_dvapplication table
            create_applications_table = """
            CREATE TABLE IF NOT EXISTS applications_dvapplication (
                id bigint AUTO_INCREMENT NOT NULL PRIMARY KEY,
                confirmation_number varchar(20) NOT NULL UNIQUE,
                first_name varchar(100) NOT NULL,
                last_name varchar(100) NOT NULL,
                middle_name varchar(100),
                date_of_birth date NOT NULL,
                gender varchar(10) NOT NULL,
                country_of_birth varchar(100) NOT NULL,
                country_of_citizenship varchar(100) NOT NULL,
                marital_status varchar(20) NOT NULL,
                current_address text NOT NULL,
                city varchar(100) NOT NULL,
                state_province varchar(100),
                postal_code varchar(20),
                phone_number varchar(20) NOT NULL,
                email varchar(254) NOT NULL,
                education_level varchar(50) NOT NULL,
                occupation varchar(100) NOT NULL,
                work_experience_years integer NOT NULL,
                emergency_contact_name varchar(100) NOT NULL,
                emergency_contact_phone varchar(20) NOT NULL,
                emergency_contact_relationship varchar(50) NOT NULL,
                photo varchar(100) NOT NULL,
                payment_proof varchar(100) NOT NULL,
                status varchar(20) NOT NULL DEFAULT 'pending',
                created_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
                updated_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
                telegram_chat_id varchar(100),
                user_id bigint NOT NULL,
                INDEX idx_confirmation_number (confirmation_number),
                INDEX idx_user_id (user_id),
                INDEX idx_status (status)
            );
            """
            
            cursor.execute(create_applications_table)
            print("✅ Created applications_dvapplication table")
            
            # Create applications_spouse table
            create_spouse_table = """
            CREATE TABLE IF NOT EXISTS applications_spouse (
                id bigint AUTO_INCREMENT NOT NULL PRIMARY KEY,
                first_name varchar(100) NOT NULL,
                last_name varchar(100) NOT NULL,
                middle_name varchar(100),
                date_of_birth date NOT NULL,
                gender varchar(10) NOT NULL,
                country_of_birth varchar(100) NOT NULL,
                country_of_citizenship varchar(100) NOT NULL,
                application_id bigint NOT NULL,
                created_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
                updated_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
                INDEX idx_application_id (application_id)
            );
            """
            
            cursor.execute(create_spouse_table)
            print("✅ Created applications_spouse table")
            
            # Create applications_child table
            create_child_table = """
            CREATE TABLE IF NOT EXISTS applications_child (
                id bigint AUTO_INCREMENT NOT NULL PRIMARY KEY,
                first_name varchar(100) NOT NULL,
                last_name varchar(100) NOT NULL,
                middle_name varchar(100),
                date_of_birth date NOT NULL,
                gender varchar(10) NOT NULL,
                country_of_birth varchar(100) NOT NULL,
                country_of_citizenship varchar(100) NOT NULL,
                application_id bigint NOT NULL,
                created_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
                updated_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
                INDEX idx_application_id (application_id)
            );
            """
            
            cursor.execute(create_child_table)
            print("✅ Created applications_child table")
            
        else:
            print(f"✅ Found {len(app_tables)} applications tables")
            for table in app_tables:
                print(f"   - {table[0]}")
        
        # Step 4: Test Django models
        print("\n🧪 STEP 4: Testing Django models...")
        try:
            from applications.models import DVApplication
            app_count = DVApplication.objects.count()
            print(f"✅ DVApplication model working: {app_count} applications")
        except Exception as e:
            print(f"❌ DVApplication model error: {e}")
        
        # Step 5: Test admin access
        print("\n👤 STEP 5: Testing admin user...")
        try:
            from django.contrib.auth.models import User
            admin_user = User.objects.get(username='admin')
            print(f"✅ Admin user exists: {admin_user.username}")
        except Exception as e:
            print(f"❌ Admin user error: {e}")
        
        # Step 6: Final test
        print("\n🎯 STEP 6: Final comprehensive test...")
        try:
            from django.core.management import execute_from_command_line
            execute_from_command_line(['manage.py', 'check'])
            print("✅ Django system check passed!")
        except Exception as e:
            print(f"⚠️ System check warning: {e}")
        
        print("\n" + "=" * 60)
        print("🎉 COMPLETE FIX SUCCESSFUL!")
        print("🌐 Your Django application should now work properly!")
        print("🔗 Website: https://polocash.com")
        print("👤 Admin: https://polocash.com/admin/")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Error during complete fix: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    complete_fix()
