#!/usr/bin/env python
"""
Test the optional spouse and children functionality
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

def test_optional_family():
    """Test creating applications with and without family members"""
    print("🧪 Testing Optional Family Members")
    print("=" * 50)
    
    # Test 1: Single applicant only (no family)
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
        status="pending"
    )
    print(f"✅ Created single applicant: {app1.dv_id}")
    print(f"   - No spouse: {not DVSpouse.objects.filter(application=app1).exists()}")
    print(f"   - No children: {not DVChild.objects.filter(application=app1).exists()}")
    
    # Test 2: Married applicant with spouse only
    app2 = DVApplication.objects.create(
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@example.com",
        phone_number="+251922345678",
        country_of_citizenship="Ethiopia",
        date_of_birth=date(1988, 12, 3),
        gender="F",
        marital_status="married",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia",
        telegram_username="janesmith",
        status="pending"
    )
    
    # Add spouse
    spouse = DVSpouse.objects.create(
        application=app2,
        first_name="Bob",
        last_name="Smith",
        date_of_birth=date(1985, 8, 22),
        gender="M",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia",
        country_of_citizenship="Ethiopia"
    )
    print(f"✅ Created married applicant with spouse: {app2.dv_id}")
    print(f"   - Has spouse: {DVSpouse.objects.filter(application=app2).exists()}")
    print(f"   - No children: {not DVChild.objects.filter(application=app2).exists()}")
    
    # Test 3: Married applicant with spouse and children
    app3 = DVApplication.objects.create(
        first_name="Alice",
        last_name="Johnson",
        email="alice.johnson@example.com",
        phone_number="+251933456789",
        country_of_citizenship="Ethiopia",
        date_of_birth=date(1992, 3, 10),
        gender="F",
        marital_status="married",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia",
        telegram_username="alicejohnson",
        status="pending"
    )
    
    # Add spouse
    spouse2 = DVSpouse.objects.create(
        application=app3,
        first_name="David",
        last_name="Johnson",
        date_of_birth=date(1990, 7, 15),
        gender="M",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia",
        country_of_citizenship="Ethiopia"
    )
    
    # Add children
    child1 = DVChild.objects.create(
        application=app3,
        first_name="Emma",
        last_name="Johnson",
        date_of_birth=date(2015, 7, 18),
        gender="F",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia"
    )
    
    child2 = DVChild.objects.create(
        application=app3,
        first_name="Michael",
        last_name="Johnson",
        date_of_birth=date(2018, 3, 10),
        gender="M",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia"
    )
    
    print(f"✅ Created married applicant with spouse and children: {app3.dv_id}")
    print(f"   - Has spouse: {DVSpouse.objects.filter(application=app3).exists()}")
    print(f"   - Has children: {DVChild.objects.filter(application=app3).exists()}")
    print(f"   - Children count: {DVChild.objects.filter(application=app3).count()}")
    
    print("\n" + "=" * 50)
    print("✅ Optional family members test completed!")
    print(f"\n📊 Final Statistics:")
    print(f"  📝 Total Applications: {DVApplication.objects.count()}")
    print(f"  💑 Applications with Spouse: {DVApplication.objects.filter(spouse__isnull=False).distinct().count()}")
    print(f"  👶 Applications with Children: {DVApplication.objects.filter(children__isnull=False).distinct().count()}")
    print(f"  👤 Single Applications: {DVApplication.objects.filter(spouse__isnull=True, children__isnull=True).count()}")
    
    print(f"\n🌐 Test the form at: http://localhost:8000/applications/apply/")
    print(f"📋 View in admin: http://localhost:8000/admin/applications/dvapplication/")

if __name__ == "__main__":
    test_optional_family()
