#!/usr/bin/env python3
"""
Create only essential tables for the website to work
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def create_essential_tables():
    print("🔧 Creating Essential Tables Only")
    print("=" * 40)
    
    try:
        import django
        from django.db import connection
        
        # Setup Django
        django.setup()
        print("✅ Django setup completed!")
        
        # Get fresh connection
        connection.close()
        cursor = connection.cursor()
        
        # Create only the most essential table - applications_dvapplication
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
            user_id bigint NOT NULL
        );
        """
        
        cursor.execute(create_applications_table)
        print("✅ Created applications_dvapplication table")
        
        # Create applications_spouse table
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
            updated_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
        );
        """
        
        cursor.execute(create_spouse_table)
        print("✅ Created applications_spouse table")
        
        # Create applications_child table
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
            updated_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
        );
        """
        
        cursor.execute(create_child_table)
        print("✅ Created applications_child table")
        
        # Test the essential table
        print("\n🧪 Testing essential table...")
        cursor.execute("SELECT COUNT(*) FROM applications_dvapplication")
        app_count = cursor.fetchone()[0]
        print(f"✅ applications_dvapplication: {app_count} records")
        
        # Test Django model
        print("\n🎯 Testing Django model...")
        try:
            from applications.models import DVApplication
            app_count = DVApplication.objects.count()
            print(f"✅ DVApplication model working: {app_count} applications")
        except Exception as e:
            print(f"❌ DVApplication model error: {e}")
        
        print("\n" + "=" * 40)
        print("🎉 ESSENTIAL TABLES CREATED!")
        print("🌐 Your application form should now work!")
        print("🔗 Test: https://polocash.com/apply/")
        print("=" * 40)
        
    except Exception as e:
        print(f"❌ Error creating essential tables: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    create_essential_tables()
