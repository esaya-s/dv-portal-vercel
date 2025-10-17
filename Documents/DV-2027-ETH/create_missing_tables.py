#!/usr/bin/env python3
"""
Create missing database tables directly with connection handling
"""

import os
import sys
import time

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def create_missing_tables():
    print("🔧 Creating Missing Database Tables")
    print("=" * 50)
    
    try:
        import django
        from django.db import connection, connections
        from django.core.management import execute_from_command_line
        
        # Setup Django
        django.setup()
        print("✅ Django setup completed!")
        
        # Close any existing connections
        connection.close()
        
        # Create new connection
        print("🔄 Establishing fresh database connection...")
        cursor = connection.cursor()
        
        # Test connection
        cursor.execute("SELECT 1")
        print("✅ Database connection established!")
        
        # Create missing tables one by one
        print("\n📋 Creating missing tables...")
        
        # 1. Create accounts_userprofile table
        print("🔄 Creating accounts_userprofile table...")
        create_userprofile_table = """
        CREATE TABLE IF NOT EXISTS accounts_userprofile (
            id bigint AUTO_INCREMENT NOT NULL PRIMARY KEY,
            user_id bigint NOT NULL,
            phone_number varchar(20) NOT NULL,
            date_of_birth date NOT NULL,
            gender varchar(10) NOT NULL,
            country_of_birth varchar(100) NOT NULL,
            country_of_citizenship varchar(100) NOT NULL,
            current_address text NOT NULL,
            city varchar(100) NOT NULL,
            state_province varchar(100),
            postal_code varchar(20),
            education_level varchar(50) NOT NULL,
            occupation varchar(100) NOT NULL,
            work_experience_years integer NOT NULL,
            emergency_contact_name varchar(100) NOT NULL,
            emergency_contact_phone varchar(20) NOT NULL,
            emergency_contact_relationship varchar(50) NOT NULL,
            marital_status varchar(20) NOT NULL,
            middle_name varchar(100),
            phone_verified boolean NOT NULL DEFAULT FALSE,
            email_verified boolean NOT NULL DEFAULT FALSE,
            profile_completed boolean NOT NULL DEFAULT FALSE,
            telegram_username varchar(100),
            created_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
            updated_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
            CONSTRAINT accounts_userprofile_user_id_fk_auth_user_id 
                FOREIGN KEY (user_id) REFERENCES auth_user (id)
        );
        """
        
        cursor.execute(create_userprofile_table)
        print("✅ Created accounts_userprofile table")
        
        # 2. Create applications_dvapplication table
        print("🔄 Creating applications_dvapplication table...")
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
            CONSTRAINT applications_dvapplicat_user_id_fk_auth_user_id 
                FOREIGN KEY (user_id) REFERENCES auth_user (id)
        );
        """
        
        cursor.execute(create_applications_table)
        print("✅ Created applications_dvapplication table")
        
        # 3. Create applications_spouse table
        print("🔄 Creating applications_spouse table...")
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
            CONSTRAINT applications_spouse_application_id_fk_applications_dvapplication_id 
                FOREIGN KEY (application_id) REFERENCES applications_dvapplication (id)
        );
        """
        
        cursor.execute(create_spouse_table)
        print("✅ Created applications_spouse table")
        
        # 4. Create applications_child table
        print("🔄 Creating applications_child table...")
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
            CONSTRAINT applications_child_application_id_fk_applications_dvapplication_id 
                FOREIGN KEY (application_id) REFERENCES applications_dvapplication (id)
        );
        """
        
        cursor.execute(create_child_table)
        print("✅ Created applications_child table")
        
        # 5. Create core_contactmessage table
        print("🔄 Creating core_contactmessage table...")
        create_contact_table = """
        CREATE TABLE IF NOT EXISTS core_contactmessage (
            id bigint AUTO_INCREMENT NOT NULL PRIMARY KEY,
            name varchar(100) NOT NULL,
            email varchar(254) NOT NULL,
            subject varchar(200) NOT NULL,
            message text NOT NULL,
            created_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
            updated_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
            is_read boolean NOT NULL DEFAULT FALSE
        );
        """
        
        cursor.execute(create_contact_table)
        print("✅ Created core_contactmessage table")
        
        # 6. Create notifications_telegramuser table
        print("🔄 Creating notifications_telegramuser table...")
        create_telegram_user_table = """
        CREATE TABLE IF NOT EXISTS notifications_telegramuser (
            id bigint AUTO_INCREMENT NOT NULL PRIMARY KEY,
            chat_id varchar(100) NOT NULL UNIQUE,
            username varchar(100),
            first_name varchar(100),
            last_name varchar(100),
            is_admin boolean NOT NULL DEFAULT FALSE,
            created_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
            updated_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
        );
        """
        
        cursor.execute(create_telegram_user_table)
        print("✅ Created notifications_telegramuser table")
        
        # 7. Create notifications_telegramnotification table
        print("🔄 Creating notifications_telegramnotification table...")
        create_telegram_notification_table = """
        CREATE TABLE IF NOT EXISTS notifications_telegramnotification (
            id bigint AUTO_INCREMENT NOT NULL PRIMARY KEY,
            chat_id varchar(100) NOT NULL,
            message text NOT NULL,
            message_type varchar(50) NOT NULL,
            sent_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
            is_successful boolean NOT NULL DEFAULT TRUE
        );
        """
        
        cursor.execute(create_telegram_notification_table)
        print("✅ Created notifications_telegramnotification table")
        
        # Test all tables
        print("\n🧪 Testing all created tables...")
        
        # Test accounts
        cursor.execute("SELECT COUNT(*) FROM accounts_userprofile")
        userprofile_count = cursor.fetchone()[0]
        print(f"✅ accounts_userprofile: {userprofile_count} records")
        
        # Test applications
        cursor.execute("SELECT COUNT(*) FROM applications_dvapplication")
        app_count = cursor.fetchone()[0]
        print(f"✅ applications_dvapplication: {app_count} records")
        
        cursor.execute("SELECT COUNT(*) FROM applications_spouse")
        spouse_count = cursor.fetchone()[0]
        print(f"✅ applications_spouse: {spouse_count} records")
        
        cursor.execute("SELECT COUNT(*) FROM applications_child")
        child_count = cursor.fetchone()[0]
        print(f"✅ applications_child: {child_count} records")
        
        # Test core
        cursor.execute("SELECT COUNT(*) FROM core_contactmessage")
        contact_count = cursor.fetchone()[0]
        print(f"✅ core_contactmessage: {contact_count} records")
        
        # Test notifications
        cursor.execute("SELECT COUNT(*) FROM notifications_telegramuser")
        tg_user_count = cursor.fetchone()[0]
        print(f"✅ notifications_telegramuser: {tg_user_count} records")
        
        cursor.execute("SELECT COUNT(*) FROM notifications_telegramnotification")
        tg_notif_count = cursor.fetchone()[0]
        print(f"✅ notifications_telegramnotification: {tg_notif_count} records")
        
        # Test Django models
        print("\n🎯 Testing Django models...")
        try:
            from applications.models import DVApplication
            app_count = DVApplication.objects.count()
            print(f"✅ DVApplication model working: {app_count} applications")
        except Exception as e:
            print(f"❌ DVApplication model error: {e}")
        
        try:
            from accounts.models import UserProfile
            profile_count = UserProfile.objects.count()
            print(f"✅ UserProfile model working: {profile_count} profiles")
        except Exception as e:
            print(f"❌ UserProfile model error: {e}")
        
        print("\n" + "=" * 50)
        print("🎉 ALL TABLES CREATED SUCCESSFULLY!")
        print("🌐 Your website should now work properly!")
        print("🔗 Visit: https://polocash.com")
        print("👤 Admin: https://polocash.com/admin/")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    create_missing_tables()
