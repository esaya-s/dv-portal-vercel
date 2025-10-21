@echo off
echo ============================================================
echo Opening Deployment Guides
echo ============================================================
echo.

REM Open most important file first
start FINAL_FIX_SUMMARY.txt
timeout /t 2 /nobreak >nul

start START_HERE.txt
timeout /t 2 /nobreak >nul

start DEPLOYMENT_SUCCESS.md
timeout /t 2 /nobreak >nul

start VERCEL_NEXT_STEPS.md
timeout /t 2 /nobreak >nul

start DOMAIN_SETUP_GUIDE.md

echo.
echo ============================================================
echo All guides opened!
echo ============================================================
echo.
echo Also opening Vercel Dashboard in browser...
echo.

REM Open Vercel dashboard
start https://vercel.com/dashboard

echo.
echo ✅ Done! Check the opened files and browser tabs.
echo.
echo 📌 Start with FINAL_FIX_SUMMARY.txt for the complete overview!
echo.
pause

