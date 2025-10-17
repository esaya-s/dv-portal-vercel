#!/usr/bin/env python
"""
Check Django admin registration and applications
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings')
django.setup()

from django.contrib import admin
from applications.models import DVApplication, DVSpouse, DVChild, ApplicationStatus

def check_admin_registration():
    """Check if models are registered in admin"""
    print("🔍 Checking Django Admin Registration")
    print("=" * 50)
    
    # Check if models are registered
    registered_models = []
    for model, admin_class in admin.site._registry.items():
        registered_models.append(model.__name__)
    
    print("📋 Registered Models in Admin:")
    for model_name in registered_models:
        print(f"  ✅ {model_name}")
    
    print(f"\n📊 Total registered models: {len(registered_models)}")
    
    # Check specific models
    models_to_check = [
        ('DVApplication', DVApplication),
        ('DVSpouse', DVSpouse), 
        ('DVChild', DVChild),
        ('ApplicationStatus', ApplicationStatus)
    ]
    
    print("\n🔍 Checking Specific Models:")
    for model_name, model_class in models_to_check:
        if model_class in admin.site._registry:
            print(f"  ✅ {model_name} is registered")
        else:
            print(f"  ❌ {model_name} is NOT registered")
    
    # Check if there are any applications in database
    print("\n📊 Database Statistics:")
    try:
        app_count = DVApplication.objects.count()
        print(f"  📝 Total Applications: {app_count}")
        
        if app_count > 0:
            print("\n📋 Recent Applications:")
            recent_apps = DVApplication.objects.all()[:5]
            for app in recent_apps:
                print(f"    • {app.dv_id} - {app.first_name} {app.last_name} ({app.status})")
    except Exception as e:
        print(f"  ❌ Error accessing database: {e}")

if __name__ == "__main__":
    check_admin_registration()
