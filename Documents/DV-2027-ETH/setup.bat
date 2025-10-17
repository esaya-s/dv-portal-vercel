@echo off
echo 🚀 Starting DV Portal Complete Setup...
echo ================================================

echo.
echo 📦 Installing Python dependencies...
pip install -r requirements.txt

echo.
echo 🔧 Running complete setup script...
python complete_setup.py

echo.
echo 🎉 Setup completed! 
echo.
echo 📋 Next steps:
echo 1. Copy .env.template to .env and update with your values
echo 2. Run: python manage.py runserver
echo 3. Visit: http://localhost:8000
echo.
echo 🚀 For deployment, consider:
echo • Railway: railway.app (Recommended)
echo • Render: render.com  
echo • Heroku: heroku.com
echo • PythonAnywhere: pythonanywhere.com
echo.
pause
