#!/usr/bin/env python
"""
Test the application form with spouse and children functionality
"""
import os
import sys
import django
from datetime import date

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings')
django.setup()

from applications.models import DVApplication, DVSpouse, DVChild

def test_application_with_family():
    """Test creating an application with spouse and children"""
    print("🧪 Testing Application Form with Family")
    print("=" * 50)
    
    # Create a married applicant
    app = DVApplication.objects.create(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        phone_number="+251911234567",
        country_of_citizenship="Ethiopia",
        date_of_birth=date(1990, 5, 15),
        gender="M",
        marital_status="married",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia",
        telegram_username="johndoe",
        status="pending"
    )
    print(f"✅ Created married applicant: {app.dv_id}")
    
    # Add spouse
    spouse = DVSpouse.objects.create(
        application=app,
        first_name="Jane",
        last_name="Doe",
        date_of_birth=date(1992, 8, 22),
        gender="F",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia",
        country_of_citizenship="Ethiopia"
    )
    print(f"✅ Added spouse: {spouse.first_name} {spouse.last_name}")
    
    # Add children
    child1 = DVChild.objects.create(
        application=app,
        first_name="Emma",
        last_name="Doe",
        date_of_birth=date(2015, 7, 18),
        gender="F",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia"
    )
    print(f"✅ Added child 1: {child1.first_name} {child1.last_name}")
    
    child2 = DVChild.objects.create(
        application=app,
        first_name="Michael",
        last_name="Doe",
        date_of_birth=date(2018, 3, 10),
        gender="M",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia"
    )
    print(f"✅ Added child 2: {child2.first_name} {child2.last_name}")
    
    # Test single parent application
    app2 = DVApplication.objects.create(
        first_name="Sarah",
        last_name="Smith",
        email="sarah.smith@example.com",
        phone_number="+251922345678",
        country_of_citizenship="Ethiopia",
        date_of_birth=date(1988, 12, 3),
        gender="F",
        marital_status="single",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia",
        telegram_username="sarahsmith",
        status="pending"
    )
    print(f"✅ Created single parent applicant: {app2.dv_id}")
    
    # Add child to single parent
    child3 = DVChild.objects.create(
        application=app2,
        first_name="Alex",
        last_name="Smith",
        date_of_birth=date(2016, 5, 25),
        gender="M",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia"
    )
    print(f"✅ Added child to single parent: {child3.first_name} {child3.last_name}")
    
    print("\n" + "=" * 50)
    print("✅ Family application test completed!")
    print(f"\n📊 Statistics:")
    print(f"  📝 Total Applications: {DVApplication.objects.count()}")
    print(f"  💑 Total Spouses: {DVSpouse.objects.count()}")
    print(f"  👶 Total Children: {DVChild.objects.count()}")
    
    print(f"\n🌐 Test the form at: http://localhost:8000/applications/apply/")
    print(f"📋 View in admin: http://localhost:8000/admin/applications/dvapplication/")

if __name__ == "__main__":
    test_application_with_family()
