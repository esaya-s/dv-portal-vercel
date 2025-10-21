@echo off
echo 🔐 GitHub Authentication Setup
echo ================================================

echo.
echo 📋 Step 1: Create Personal Access Token
echo ================================================
echo 1. Go to https://github.com/settings/tokens
echo 2. Click "Generate new token" ^> "Generate new token (classic)"
echo 3. Give it a name: "DV Portal Vercel Deployment"
echo 4. Select scopes:
echo    ✅ repo (Full control of private repositories)
echo    ✅ workflow (Update GitHub Action workflows)
echo 5. Click "Generate token"
echo 6. COPY the token (you won't see it again!)
echo.

echo 📋 Step 2: Configure Git Authentication
echo ================================================
echo Run these commands with your GitHub username and token:
echo.
echo git config --global credential.helper store
echo git remote set-url origin https://YOUR_USERNAME:YOUR_TOKEN@github.com/YOUR_USERNAME/dv-portal-vercel.git
echo.
echo Example:
echo git remote set-url origin https://esaya-s:ghp_xxxxxxxxxxxx@github.com/esaya-s/dv-portal-vercel.git
echo.

echo 📋 Step 3: Push to GitHub
echo ================================================
echo git push -u origin main
echo.

echo 🔧 Alternative: Use GitHub CLI
echo ================================================
echo 1. Install GitHub CLI: https://cli.github.com/
echo 2. Run: gh auth login
echo 3. Follow the prompts
echo 4. Then: git push -u origin main
echo.

pause

