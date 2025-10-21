@echo off
echo ============================================================
echo Pushing Clean Vercel Build Configuration
echo ============================================================

cd /d "%~dp0"

echo.
echo [1/4] Adding all changes...
git add .
git add -u

echo.
echo [2/4] Committing changes...
git commit -m "Fix: Clean Vercel config - remove pyproject, use single requirements.txt"

echo.
echo [3/4] Pushing to GitHub...
git push origin main

echo.
echo [4/4] Triggering Vercel redeploy...
echo Changes pushed! Vercel will automatically redeploy.

echo.
echo ============================================================
echo Successfully pushed clean build configuration!
echo ============================================================
echo.
echo Changes made:
echo   - Removed builds section from vercel.json
echo   - Added runtime.txt (Python 3.12)
echo   - Added .vercelignore
echo   - Consolidated to single requirements.txt
echo   - No more pyproject.toml conflicts!
echo.
echo Next: Check Vercel dashboard for new deployment
echo.
pause

