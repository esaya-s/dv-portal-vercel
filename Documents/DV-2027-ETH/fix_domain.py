#!/usr/bin/env python
"""
Quick script to fix domain access for Django
"""

import os
import sys

def fix_domain_access():
    """Fix domain access by updating ALLOWED_HOSTS"""
    print("🔧 Fixing Domain Access...")
    
    # Get current domain from user
    domain = input("Enter your domain (e.g., yourdomain.com): ").strip()
    
    if not domain:
        print("❌ No domain provided. Exiting.")
        return
    
    # Update settings.py
    settings_file = 'dv_portal/settings.py'
    
    try:
        with open(settings_file, 'r') as f:
            content = f.read()
        
        # Replace ALLOWED_HOSTS line
        old_line = "ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=lambda v: [s.strip() for s in v.split(',')])"
        new_line = f"ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1,{domain}', cast=lambda v: [s.strip() for s in v.split(',')])"
        
        if old_line in content:
            content = content.replace(old_line, new_line)
            
            with open(settings_file, 'w') as f:
                f.write(content)
            
            print(f"✅ Updated ALLOWED_HOSTS to include: {domain}")
        else:
            print("⚠️ Could not find ALLOWED_HOSTS line in settings.py")
            
    except Exception as e:
        print(f"❌ Error updating settings: {e}")

def start_server():
    """Start Django server on all interfaces"""
    print("\n🚀 Starting Django Server...")
    print("Server will be accessible at:")
    print(f"  - http://localhost:8000")
    print(f"  - http://127.0.0.1:8000")
    print(f"  - http://your-server-ip:8000")
    print(f"  - http://yourdomain.com:8000")
    print("\nPress Ctrl+C to stop the server")
    
    # Start server
    os.system('python manage.py runserver 0.0.0.0:8000')

if __name__ == "__main__":
    print("🌐 Django Domain Access Fixer")
    print("=" * 40)
    
    try:
        fix_domain_access()
        start_server()
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")
