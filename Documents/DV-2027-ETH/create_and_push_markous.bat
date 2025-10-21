@echo off
echo 🚀 Create Repository and Push to markous2 GitHub
echo ================================================

echo.
echo 📋 Step 1: Create Repository on GitHub
echo ================================================
echo 1. Go to https://github.com/new
echo 2. Repository name: dv-portal-vercel
echo 3. Owner: markous2
echo 4. Description: Django DV Portal for Vercel Deployment
echo 5. Make it Public (recommended for Vercel)
echo 6. DON'T initialize with README, .gitignore, or license
echo 7. Click "Create repository"
echo.

echo 📋 Step 2: Push Your Code
echo ================================================
echo After creating the repository, run:
echo.
echo git push -u origin main
echo.

echo 🔧 If you get authentication errors:
echo ================================================
echo Option 1: Use Personal Access Token
echo 1. Go to https://github.com/settings/tokens
echo 2. Generate new token with 'repo' scope
echo 3. Use: git push https://markous2:YOUR_TOKEN@github.com/markous2/dv-portal-vercel.git main
echo.
echo Option 2: Use GitHub CLI
echo 1. Install: https://cli.github.com/
echo 2. Run: gh auth login
echo 3. Then: git push -u origin main
echo.

echo 📁 Repository URL:
echo https://github.com/markous2/dv-portal-vercel
echo.

echo 🌐 After pushing, deploy to Vercel:
echo ================================================
echo 1. Go to vercel.com
echo 2. Click "New Project"
echo 3. Import: https://github.com/markous2/dv-portal-vercel
echo 4. Choose "Django" framework
echo 5. Configure environment variables
echo 6. Deploy!
echo.

pause

