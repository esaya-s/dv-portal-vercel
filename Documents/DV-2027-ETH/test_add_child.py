#!/usr/bin/env python
"""
Test the add child functionality
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

from applications.models import DVApplication, DVChild

def test_add_child_functionality():
    """Test adding multiple children to an application"""
    print("🧪 Testing Add Child Functionality")
    print("=" * 50)
    
    # Create a test application
    app = DVApplication.objects.create(
        first_name="Test",
        last_name="Parent",
        email="test.parent@example.com",
        phone_number="+251911234567",
        country_of_citizenship="Ethiopia",
        date_of_birth=date(1990, 5, 15),
        gender="M",
        marital_status="married",
        city_of_birth="Addis Ababa",
        country_of_birth="Ethiopia",
        telegram_username="testparent",
        status="pending"
    )
    print(f"✅ Created test application: {app.dv_id}")
    
    # Add multiple children
    children_data = [
        {
            'first_name': 'Child1',
            'last_name': 'Parent',
            'date_of_birth': date(2015, 7, 18),
            'gender': 'F',
            'city_of_birth': 'Addis Ababa',
            'country_of_birth': 'Ethiopia'
        },
        {
            'first_name': 'Child2',
            'last_name': 'Parent',
            'date_of_birth': date(2018, 3, 10),
            'gender': 'M',
            'city_of_birth': 'Addis Ababa',
            'country_of_birth': 'Ethiopia'
        },
        {
            'first_name': 'Child3',
            'last_name': 'Parent',
            'date_of_birth': date(2020, 12, 5),
            'gender': 'F',
            'city_of_birth': 'Addis Ababa',
            'country_of_birth': 'Ethiopia'
        }
    ]
    
    for i, child_data in enumerate(children_data, 1):
        child = DVChild.objects.create(
            application=app,
            **child_data
        )
        print(f"✅ Added child {i}: {child.first_name} {child.last_name}")
    
    print(f"\n📊 Application Statistics:")
    print(f"  📝 Application ID: {app.dv_id}")
    print(f"  👶 Total Children: {DVChild.objects.filter(application=app).count()}")
    
    # List all children
    children = DVChild.objects.filter(application=app).order_by('first_name')
    for child in children:
        print(f"    - {child.first_name} {child.last_name} ({child.gender}, {child.date_of_birth})")
    
    print(f"\n🌐 Test the form at: http://localhost:8000/applications/apply/")
    print(f"📋 View in admin: http://localhost:8000/admin/applications/dvapplication/")
    print(f"\n💡 Instructions:")
    print(f"  1. Go to the application form")
    print(f"  2. Check 'Include Children Information'")
    print(f"  3. Click 'Add Another Child' button")
    print(f"  4. Verify new child form appears")
    print(f"  5. Test removing children with 'Remove Child' button")

if __name__ == "__main__":
    test_add_child_functionality()
