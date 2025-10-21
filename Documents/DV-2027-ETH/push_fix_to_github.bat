@echo off
echo ============================================================
echo Pushing Vercel Fix to GitHub
echo ============================================================

cd /d "%~dp0"

echo.
echo [1/3] Adding changes...
git add .

echo.
echo [2/3] Committing changes...
git commit -m "Fix: Remove pyproject.toml to resolve Vercel build error"

echo.
echo [3/3] Pushing to GitHub...
git push origin main

echo.
echo ============================================================
echo Successfully pushed fixes to GitHub!
echo ============================================================
echo.
echo Now Vercel will automatically redeploy your application.
echo Check your Vercel dashboard for deployment status.
echo.
pause

