#!/usr/bin/env python3
"""
Simple test for Django URL routing
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def test_urls():
    print("🧪 Testing Django URLs")
    print("=" * 40)
    
    try:
        import django
        django.setup()
        print("✅ Django setup completed!")
        
        # Test URL patterns
        print("\n🔗 Testing URL patterns...")
        from django.urls import get_resolver
        
        resolver = get_resolver()
        url_patterns = resolver.url_patterns
        
        print(f"✅ Found {len(url_patterns)} URL patterns:")
        for i, pattern in enumerate(url_patterns, 1):
            print(f"   {i}. {pattern}")
        
        # Test specific URL resolution
        print("\n🎯 Testing URL resolution...")
        from django.urls import resolve
        
        test_paths = [
            ('/', 'Home page'),
            ('/admin/', 'Admin panel'),
            ('/apply/', 'Application form'),
            ('/applications/status/', 'Status page'),
        ]
        
        for path, description in test_paths:
            try:
                resolved = resolve(path)
                print(f"✅ {description}: {path} → {resolved.view_name}")
            except Exception as e:
                print(f"❌ {description}: {path} → Error: {e}")
        
        print("\n" + "=" * 40)
        print("🎯 URL TEST COMPLETED!")
        print("=" * 40)
        print("If all tests passed, Django URLs are working.")
        print("The issue is with .htaccess routing.")
        print("=" * 40)
        
    except Exception as e:
        print(f"❌ URL test error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_urls()
