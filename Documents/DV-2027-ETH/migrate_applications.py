#!/usr/bin/env python3
"""
Create missing applications tables
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def create_missing_tables():
    print("🔧 Creating missing database tables...")
    print("=" * 50)
    
    try:
        import django
        from django.core.management import execute_from_command_line
        from django.db import connection
        
        # Setup Django
        django.setup()
        print("✅ Django setup completed!")
        
        # Create tables manually using SQL
        print("\n🔄 Creating missing tables...")
        cursor = connection.cursor()
        
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
            status varchar(20) NOT NULL,
            created_at datetime(6) NOT NULL,
            updated_at datetime(6) NOT NULL,
            telegram_chat_id varchar(100),
            user_id bigint NOT NULL,
            CONSTRAINT applications_dvapplicat_user_id_fk_auth_user_id 
                FOREIGN KEY (user_id) REFERENCES auth_user (id)
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
            CONSTRAINT applications_spouse_application_id_fk_applications_dvapplication_id 
                FOREIGN KEY (application_id) REFERENCES applications_dvapplication (id)
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
            CONSTRAINT applications_child_application_id_fk_applications_dvapplication_id 
                FOREIGN KEY (application_id) REFERENCES applications_dvapplication (id)
        );
        """
        
        cursor.execute(create_child_table)
        print("✅ Created applications_child table")
        
        # Test the tables
        print("\n🧪 Testing created tables...")
        cursor.execute("SELECT COUNT(*) FROM applications_dvapplication")
        app_count = cursor.fetchone()[0]
        print(f"✅ DVApplication table working: {app_count} records")
        
        cursor.execute("SELECT COUNT(*) FROM applications_spouse")
        spouse_count = cursor.fetchone()[0]
        print(f"✅ Spouse table working: {spouse_count} records")
        
        cursor.execute("SELECT COUNT(*) FROM applications_child")
        child_count = cursor.fetchone()[0]
        print(f"✅ Child table working: {child_count} records")
        
        print("\n🎉 All tables created successfully!")
        
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    create_missing_tables()
