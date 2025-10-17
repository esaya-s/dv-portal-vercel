#!/usr/bin/env python
"""
Create a test application for admin panel testing
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

def create_test_applications():
    """Create test applications for admin panel"""
    print("📝 Creating Test Applications")
    print("=" * 50)
    
    # Create test application 1
    app1 = DVApplication.objects.create(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        phone_number="+251911234567",
        country_of_citizenship="Ethiopia",
        date_of_birth=date(1990, 5, 15),
        gender="M",
        marital_status="single",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia",
        telegram_username="johndoe",
        status="pending",
        payment_verified=False,
        photo_validation_passed=False
    )
    print(f"✅ Created Application 1: {app1.dv_id}")
    
    # Create test application 2
    app2 = DVApplication.objects.create(
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@example.com",
        phone_number="+251922345678",
        country_of_citizenship="Ethiopia",
        date_of_birth=date(1988, 8, 22),
        gender="F",
        marital_status="married",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia",
        telegram_username="janesmith",
        status="under_review",
        payment_verified=True,
        photo_validation_passed=True
    )
    print(f"✅ Created Application 2: {app2.dv_id}")
    
    # Create test application 3
    app3 = DVApplication.objects.create(
        first_name="Michael",
        last_name="Johnson",
        email="michael.johnson@example.com",
        phone_number="+251933456789",
        country_of_citizenship="Ethiopia",
        date_of_birth=date(1992, 12, 3),
        gender="M",
        marital_status="single",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia",
        telegram_username="michaelj",
        status="approved",
        payment_verified=True,
        photo_validation_passed=True
    )
    print(f"✅ Created Application 3: {app3.dv_id}")
    
    # Add spouse to application 2
    spouse = DVSpouse.objects.create(
        application=app2,
        first_name="Robert",
        last_name="Smith",
        date_of_birth=date(1985, 3, 10),
        gender="M",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia",
        country_of_citizenship="Ethiopia"
    )
    print(f"✅ Added spouse to Application 2: {spouse.first_name} {spouse.last_name}")
    
    # Add child to application 2
    child = DVChild.objects.create(
        application=app2,
        first_name="Emma",
        last_name="Smith",
        date_of_birth=date(2015, 7, 18),
        gender="F",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia"
    )
    print(f"✅ Added child to Application 2: {child.first_name} {child.last_name}")
    
    print("\n" + "=" * 50)
    print("✅ Test applications created successfully!")
    print(f"\n📊 Total Applications: {DVApplication.objects.count()}")
    print("\n🌐 You can now view these applications in the Django admin panel:")
    print("   http://localhost:8000/admin/applications/dvapplication/")

if __name__ == "__main__":
    create_test_applications()
