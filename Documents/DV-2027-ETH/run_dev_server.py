#!/usr/bin/env python3
"""
Quick development server startup script for DV Portal Ethiopia
"""
import os
import sys
import subprocess
from pathlib import Path

def main():
    """Start the Django development server with proper setup"""
    
    print("🚀 Starting DV Portal Ethiopia Development Server")
    print("=" * 50)
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("⚠️  .env file not found!")
        print("Creating .env file from template...")
        
        # Copy the example file
        if os.path.exists('env_example.txt'):
            with open('env_example.txt', 'r') as src:
                content = src.read()
            with open('.env', 'w') as dst:
                dst.write(content)
            print("✅ .env file created successfully!")
            print("📝 Please edit .env file with your API keys if needed")
        else:
            print("❌ env_example.txt not found!")
            return
    
    # Check if database exists
    if not os.path.exists('db.sqlite3'):
        print("\n📊 Setting up database...")
        try:
            subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
            print("✅ Database migrations completed!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running migrations: {e}")
            return
    
    # Collect static files
    print("\n📁 Collecting static files...")
    try:
        subprocess.run([
            sys.executable, 'manage.py', 'collectstatic', '--noinput'
        ], check=True)
        print("✅ Static files collected!")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Warning: Static files collection failed: {e}")
    
    # Create superuser prompt
    print("\n👤 Admin user setup:")
    print("You can create an admin user to access the admin panel at /admin")
    create_admin = input("Create admin user now? (y/n): ").lower().strip()
    
    if create_admin == 'y':
        try:
            subprocess.run([sys.executable, 'manage.py', 'createsuperuser'])
        except subprocess.CalledProcessError:
            print("⚠️  Superuser creation skipped or failed")
    
    # Start the development server
    print("\n🌐 Starting development server...")
    print("📍 Application will be available at: http://localhost:8000")
    print("🔧 Admin panel available at: http://localhost:8000/admin")
    print("⌨️  Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        subprocess.run([
            sys.executable, 'manage.py', 'runserver', '0.0.0.0:8000'
        ])
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Thank you for using DV Portal Ethiopia!")

if __name__ == '__main__':
    main()
