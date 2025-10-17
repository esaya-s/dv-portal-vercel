# DV Portal Ethiopia - cPanel Deployment Guide

## 📋 Pre-Deployment Checklist

### 1. **Domain & Hosting Setup**
- [ ] Purchase domain name
- [ ] Set up cPanel hosting account
- [ ] Configure DNS to point to your hosting
- [ ] Enable SSL certificate (Let's Encrypt recommended)

### 2. **Database Setup**
- [ ] Create MySQL database in cPanel
- [ ] Create database user with full privileges
- [ ] Note down database credentials

### 3. **Environment Variables**
Set these in cPanel Environment Variables section:

```bash
SECRET_KEY=your-super-secret-key-here
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
TELEGRAM_ADMIN_USERNAME=anvilutech
TELEGRAM_BOT_NAME=DV2027
TELEGRAM_BOT_USERNAME=dv20272etbot
TELEGRAM_ADMIN_CHAT_ID=your-telegram-chat-id
SITE_URL=https://yourdomain.com
GEMINI_API_KEY=your-gemini-api-key
```

## 🚀 Step-by-Step Deployment

### Step 1: Upload Files to cPanel
1. **Compress your project folder** (excluding `__pycache__`, `.git`, `db.sqlite3`)
2. **Upload via cPanel File Manager** to `public_html/` directory
3. **Extract the files** in the root directory

### Step 2: Configure Python App
1. **Go to cPanel → Software → Python App**
2. **Create New Application:**
   - Python Version: 3.9+ (recommended 3.11)
   - Application Root: `public_html`
   - Application URL: `/` (or your domain)
   - Application Startup File: `passenger_wsgi.py`
   - Application Entry Point: `application`

### Step 3: Install Dependencies
1. **Open Terminal in cPanel**
2. **Navigate to your project directory:**
   ```bash
   cd public_html
   ```
3. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

### Step 4: Database Configuration
1. **Update `dv_portal/settings_production.py`** with your database credentials
2. **Run migrations:**
   ```bash
   python manage.py migrate --settings=dv_portal.settings_production
   ```
3. **Create superuser:**
   ```bash
   python manage.py createsuperuser --settings=dv_portal.settings_production
   ```

### Step 5: Static Files Setup
1. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput --settings=dv_portal.settings_production
   ```

### Step 6: Telegram Bot Setup
1. **Create bot on Telegram:**
   - Message @BotFather on Telegram
   - Send `/newbot`
   - Follow instructions to create bot
   - Save the bot token

2. **Get your Telegram Chat ID:**
   - Message @userinfobot on Telegram
   - It will reply with your chat ID

3. **Start the bot:**
   ```bash
   python start_telegram_bot.py
   ```

### Step 7: Set Up Cron Jobs (Optional)
1. **Go to cPanel → Advanced → Cron Jobs**
2. **Add cron job to restart bot every hour:**
   ```bash
   0 * * * * cd /home/yourusername/public_html && python start_telegram_bot.py
   ```

## 🔧 Configuration Files

### File Structure After Deployment:
```
public_html/
├── passenger_wsgi.py          # WSGI entry point
├── .htaccess                   # Apache configuration
├── dv_portal/
│   ├── settings_production.py # Production settings
│   └── ...
├── staticfiles/               # Collected static files
├── media/                     # User uploaded files
├── logs/                      # Application logs
└── start_telegram_bot.py      # Bot startup script
```

## 🧪 Testing Your Deployment

### 1. **Test Web Application**
- [ ] Visit your domain
- [ ] Check if homepage loads
- [ ] Test application form
- [ ] Test admin panel login
- [ ] Verify static files are loading

### 2. **Test Telegram Bot**
- [ ] Search for your bot on Telegram
- [ ] Send `/start` command
- [ ] Test `/help` command
- [ ] Submit a test application
- [ ] Check if admin receives notifications

### 3. **Test Database**
- [ ] Create test application
- [ ] Check admin panel for data
- [ ] Verify Telegram notifications

## 🛠️ Troubleshooting

### Common Issues:

#### 1. **"Module not found" errors**
- Check Python version compatibility
- Ensure all dependencies are installed
- Verify virtual environment is activated

#### 2. **Database connection errors**
- Verify database credentials
- Check if database exists
- Ensure user has proper permissions

#### 3. **Static files not loading**
- Run `collectstatic` command
- Check file permissions
- Verify `.htaccess` configuration

#### 4. **Telegram bot not responding**
- Verify bot token is correct
- Check if bot is running
- Look at logs for errors

#### 5. **Permission errors**
- Set proper file permissions (644 for files, 755 for directories)
- Ensure web server can read files

## 📊 Monitoring & Maintenance

### 1. **Log Files**
- Check `logs/django.log` for application errors
- Check `logs/telegram_bot.log` for bot issues

### 2. **Database Backup**
- Set up regular database backups in cPanel
- Export database weekly

### 3. **Security Updates**
- Keep Django and dependencies updated
- Monitor security advisories

## 🔐 Security Considerations

### 1. **Environment Variables**
- Never commit sensitive data to version control
- Use cPanel Environment Variables for secrets

### 2. **File Permissions**
- Set restrictive permissions on sensitive files
- Don't expose configuration files

### 3. **SSL Certificate**
- Always use HTTPS in production
- Set up automatic SSL renewal

## 📞 Support Contacts

- **Telegram Support:** @dv2027apply
- **Phone:** +251-963-173-312
- **Email:** support@dvportal-ethiopia.com

## 🎯 Post-Deployment Checklist

- [ ] Domain is accessible via HTTPS
- [ ] All pages load correctly
- [ ] Application form works
- [ ] Admin panel accessible
- [ ] Telegram bot responds
- [ ] Database operations work
- [ ] Static files load properly
- [ ] SSL certificate is active
- [ ] Error logging is working
- [ ] Backup system is set up

---

**Note:** This deployment guide assumes you have basic knowledge of cPanel and web hosting. If you encounter issues, contact your hosting provider or refer to the troubleshooting section.
