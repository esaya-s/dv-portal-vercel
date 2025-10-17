#!/usr/bin/env python3
"""
GitHub Push Script for Django DV Portal
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        if result.stdout.strip():
            print(f"Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stderr.strip():
            print(f"Error: {e.stderr.strip()}")
        return False

def check_git_status():
    """Check if we're in a git repository"""
    try:
        result = subprocess.run("git status", shell=True, capture_output=True, text=True)
        return result.returncode == 0
    except:
        return False

def initialize_git_repo():
    """Initialize git repository if not exists"""
    if not check_git_status():
        print("📦 Initializing Git repository...")
        if not run_command("git init", "Initialize Git repository"):
            return False
    
    # Create .gitignore
    gitignore_content = """# Django
db.sqlite3
db_new.sqlite3
*.log
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
pip-log.txt
pip-delete-this-directory.txt
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git
.mypy_cache
.pytest_cache
.hypothesis

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Environment
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Deployment
vercel_deployment/
*.zip
*.tar.gz

# Logs
logs/
*.log

# Temporary files
temp/
tmp/
"""
    
    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)
    
    print("✅ Created .gitignore file")
    return True

def push_to_github():
    """Push the project to GitHub"""
    print("🚀 Pushing Django Project to GitHub")
    print("=" * 50)
    
    # Initialize git if needed
    if not initialize_git_repo():
        print("❌ Failed to initialize Git repository")
        return False
    
    # Add all files
    if not run_command("git add .", "Add all files to Git"):
        return False
    
    # Check if there are changes to commit
    try:
        result = subprocess.run("git diff --cached --quiet", shell=True, capture_output=True)
        if result.returncode == 0:
            print("ℹ️ No changes to commit")
            return True
    except:
        pass
    
    # Commit changes
    commit_message = "Initial Django DV Portal deployment for Vercel"
    if not run_command(f'git commit -m "{commit_message}"', "Commit changes"):
        return False
    
    print("\n📋 GitHub Repository Setup Instructions:")
    print("=" * 50)
    print("1. Go to https://github.com/new")
    print("2. Create a new repository named 'dv-portal-vercel'")
    print("3. Don't initialize with README (we have files already)")
    print("4. Copy the repository URL")
    print("5. Run the following commands:")
    print()
    print("   git remote add origin https://github.com/YOUR_USERNAME/dv-portal-vercel.git")
    print("   git branch -M main")
    print("   git push -u origin main")
    print()
    print("🌐 Repository URL format:")
    print("   https://github.com/YOUR_USERNAME/dv-portal-vercel.git")
    print()
    print("💡 After pushing to GitHub:")
    print("   1. Go to vercel.com")
    print("   2. Click 'New Project'")
    print("   3. Import your GitHub repository")
    print("   4. Choose 'Django' as framework")
    print("   5. Configure environment variables")
    print("   6. Deploy!")
    
    return True

if __name__ == "__main__":
    push_to_github()
