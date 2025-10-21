🚀 Django Deployment to Vercel - Complete Guide
===============================================

📋 Prerequisites:
✅ GitHub repository created: https://github.com/markous2/dv-portal-vercel
✅ Django project ready with Vercel configuration
✅ All files committed and pushed

🔧 Step 1: Connect to Vercel
===============================================
1. Go to https://vercel.com
2. Sign up/Login with your GitHub account
3. Click "New Project"
4. Import your repository: markous2/dv-portal-vercel
5. Choose "Django" as the framework preset

🔧 Step 2: Configure Project Settings
===============================================
- Framework Preset: Django
- Root Directory: ./
- Build Command: pip install -r requirements_vercel.txt
- Output Directory: ./
- Install Command: pip install -r requirements_vercel.txt

🔧 Step 3: Environment Variables
===============================================
Add these environment variables in Vercel dashboard:

Required Variables:
SECRET_KEY=django-secret-key-change-in-production-2024
DEBUG=False
DJANGO_SETTINGS_MODULE=dv_portal.settings_vercel

Database (Use Vercel Postgres):
POSTGRES_DATABASE=your-db-name
POSTGRES_USER=your-db-user
POSTGRES_PASSWORD=your-db-password
POSTGRES_HOST=your-db-host
POSTGRES_PORT=5432

Telegram Bot (Optional):
TELEGRAM_BOT_TOKEN=your-bot-token
TELEGRAM_ADMIN_CHAT_ID=your-chat-id
TELEGRAM_ADMIN_USERNAME=anvilutech
TELEGRAM_BOT_NAME=DV2027
TELEGRAM_BOT_USERNAME=dv20272etbot

Email (Optional):
EMAIL_HOST=your-smtp-host
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-password
DEFAULT_FROM_EMAIL=noreply@dvportal.com

🔧 Step 4: Deploy
===============================================
1. Click "Deploy"
2. Wait for deployment to complete
3. Check build logs for any errors

🔧 Step 5: Set up Database
===============================================
After successful deployment:
1. Go to Vercel dashboard
2. Open your project
3. Go to "Functions" tab
4. Run these commands:
   - python manage.py migrate
   - python manage.py collectstatic --noinput
   - python manage.py createsuperuser

🔧 Step 6: Custom Domain (anvilu.com)
===============================================
1. Go to "Domains" tab in Vercel
2. Add "anvilu.com"
3. Add "www.anvilu.com"
4. Configure DNS settings:
   - A record: @ → Vercel IP
   - CNAME record: www → cname.vercel-dns.com

🌐 Access Your Site:
===============================================
- Main Site: https://anvilu.com
- Admin Panel: https://anvilu.com/admin/
- Default Admin: admin / admin123

🔧 Troubleshooting:
===============================================
- Check Vercel build logs for errors
- Ensure all environment variables are set
- Verify database connection
- Test with: python manage.py check

📁 Your Repository:
https://github.com/markous2/dv-portal-vercel
