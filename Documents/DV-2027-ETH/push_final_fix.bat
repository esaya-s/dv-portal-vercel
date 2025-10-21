@echo off
echo ============================================================
echo Pushing Final Fix - Remove Extra Requirements Files
echo ============================================================

cd /d "%~dp0"

echo.
echo [1/3] Adding changes...
git add .
git add -u

echo.
echo [2/3] Committing...
git commit -m "Fix: Remove all extra requirements files, use only requirements.txt"

echo.
echo [3/3] Pushing to GitHub...
git push origin main

echo.
echo ============================================================
echo SUCCESS! Final fix pushed to GitHub
echo ============================================================
echo.
echo What was fixed:
echo   ✅ Removed requirements_basic.txt (had mysqlclient)
echo   ✅ Removed requirements_essentials.txt
echo   ✅ Removed requirements_fixed.txt
echo   ✅ Removed requirements_full.txt
echo   ✅ Removed requirements_minimal.txt
echo   ✅ Removed requirements_production.txt
echo   ✅ Updated .vercelignore to exclude extra requirements
echo.
echo Now using ONLY:
echo   👉 requirements.txt (clean, Vercel-compatible)
echo   👉 runtime.txt (Python 3.12)
echo.
echo Vercel will now use psycopg2-binary (PostgreSQL)
echo instead of mysqlclient (which failed to compile)
echo.
echo ============================================================
echo Next: Monitor Vercel dashboard for successful deployment!
echo ============================================================
pause

