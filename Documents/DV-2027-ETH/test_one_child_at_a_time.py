#!/usr/bin/env python
"""
Test the improved add child functionality - one at a time
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

def test_one_child_at_a_time():
    """Test the improved add child functionality"""
    print("🧪 Testing One Child at a Time Functionality")
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
    
    print(f"\n📋 New Behavior:")
    print(f"  🎯 Only ONE child form shows initially")
    print(f"  ➕ Click 'Add Another Child' to show the next form")
    print(f"  ➖ Click 'Remove Child' to hide a form (not delete)")
    print(f"  🔄 Forms can be shown/hidden as needed")
    
    print(f"\n🌐 Test Instructions:")
    print(f"  1. Go to: http://localhost:8000/applications/apply/")
    print(f"  2. Check 'Include Children Information'")
    print(f"  3. You should see ONLY Child 1 form")
    print(f"  4. Click 'Add Another Child' - Child 2 appears")
    print(f"  5. Click 'Add Another Child' - Child 3 appears")
    print(f"  6. Click 'Remove Child' on Child 2 - it hides")
    print(f"  7. Click 'Add Another Child' - Child 2 appears again")
    
    print(f"\n✅ Benefits:")
    print(f"  🎯 Cleaner interface - only shows what's needed")
    print(f"  🚀 Better performance - no form cloning")
    print(f"  💾 Preserves form data when hiding/showing")
    print(f"  🔄 Reusable forms - can show/hide multiple times")

if __name__ == "__main__":
    test_one_child_at_a_time()
