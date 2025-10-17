#!/usr/bin/env python3
"""
Test Django URL routing
"""

import os
import sys

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dv_portal.settings_production')

def test_django_urls():
    print("🧪 Testing Django URL Routing")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        print("✅ Django setup completed!")
        
        # Test URL resolution
        print("\n🔗 Testing URL Resolution...")
        from django.urls import reverse, resolve
        from django.test import Client
        
        # Test URLs
        test_urls = [
            ('/', 'Home page'),
            ('/admin/', 'Admin panel'),
            ('/apply/', 'Application form'),
            ('/applications/status/', 'Status check'),
            ('/privacy-policy/', 'Privacy policy'),
            ('/terms-of-service/', 'Terms of service'),
        ]
        
        client = Client()
        
        for url, description in test_urls:
            try:
                response = client.get(url)
                if response.status_code == 200:
                    print(f"✅ {description}: {url} → {response.status_code}")
                elif response.status_code == 302:
                    print(f"🔄 {description}: {url} → {response.status_code} (redirect)")
                else:
                    print(f"⚠️ {description}: {url} → {response.status_code}")
            except Exception as e:
                print(f"❌ {description}: {url} → Error: {e}")
        
        # Test URL patterns
        print("\n📋 Testing URL Patterns...")
        try:
            from django.urls import get_resolver
            resolver = get_resolver()
            url_patterns = resolver.url_patterns
            
            print(f"✅ Found {len(url_patterns)} URL patterns:")
            for pattern in url_patterns:
                print(f"   - {pattern}")
                
        except Exception as e:
            print(f"❌ URL patterns error: {e}")
        
        # Test specific URL resolution
        print("\n🎯 Testing Specific URL Resolution...")
        try:
            from django.urls import resolve
            
            test_paths = ['/', '/admin/', '/apply/', '/applications/status/']
            for path in test_paths:
                try:
                    resolved = resolve(path)
                    print(f"✅ {path} → {resolved.view_name} ({resolved.func})")
                except Exception as e:
                    print(f"❌ {path} → Error: {e}")
                    
        except Exception as e:
            print(f"❌ URL resolution error: {e}")
        
        print("\n" + "=" * 50)
        print("🎯 URL ROUTING TEST COMPLETED!")
        print("=" * 50)
        print("If all tests passed, the issue is with:")
        print("1. .htaccess file not routing to Django")
        print("2. cPanel Passenger configuration")
        print("3. File permissions")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ URL test error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_django_urls()
