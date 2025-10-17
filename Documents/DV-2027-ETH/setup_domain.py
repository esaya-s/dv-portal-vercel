#!/usr/bin/env python
"""
Setup script to configure Django for your main domain
"""

import os
import sys

def setup_domain():
    """Setup Django for main domain"""
    print("🌐 Setting up Django for your main domain...")
    print("=" * 50)
    
    # Get domain from user
    domain = input("Enter your main domain (e.g., yourdomain.com): ").strip()
    
    if not domain:
        print("❌ No domain provided. Exiting.")
        return
    
    print(f"✅ Configuring Django for domain: {domain}")
    
    # Update settings files
    update_settings_file('dv_portal/settings.py', domain)
    update_settings_file('dv_portal/settings_production.py', domain)
    
    print(f"✅ Django configured for domain: {domain}")
    print("\n📋 Next steps:")
    print("1. Update your DNS to point to your server")
    print("2. Set up a web server (Apache/Nginx)")
    print("3. Configure SSL certificate")
    print("4. Start Django with production settings")
    
    print(f"\n🚀 To start Django on your domain:")
    print(f"   DJANGO_SETTINGS_MODULE=dv_portal.settings_production python manage.py runserver 0.0.0.0:80")

def update_settings_file(filename, domain):
    """Update a settings file with the domain"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        # Replace placeholder domains
        content = content.replace('yourdomain.com', domain)
        content = content.replace('www.yourdomain.com', f'www.{domain}')
        
        with open(filename, 'w') as f:
            f.write(content)
        
        print(f"   ✅ Updated {filename}")
        
    except Exception as e:
        print(f"   ❌ Error updating {filename}: {e}")

if __name__ == "__main__":
    setup_domain()
