# cPanel Deployment Guide for DV Portal Ethiopia

This guide walks you through deploying the DV Portal Django application on cPanel hosting with Python support.

## Prerequisites

1. **cPanel hosting with Python support** (Python 3.8+ required)
2. **SSH access** (recommended) or File Manager access
3. **MySQL database** (or use SQLite for small deployments)
4. **Domain/subdomain** configured

## Step 1: Prepare cPanel Environment

### 1.1 Create Python App (if available)
1. Log into cPanel
2. Go to "Setup Python App" (if available)
3. Create new Python app with Python 3.8+
4. Note the app directory path

### 1.2 Alternative Setup
If Python App is not available, use the public_html directory:
```
/home/yourusername/public_html/dv_portal/
```

## Step 2: Upload Files

### Method 1: Via SSH (Recommended)
```bash
# Connect via SSH
ssh yourusername@yourserver.com

# Navigate to your domain directory
cd public_html

# Clone or upload the project files
# (Upload the entire project directory)
```

### Method 2: Via File Manager
1. Compress the entire project into a ZIP file
2. Upload via cPanel File Manager
3. Extract in your domain directory

## Step 3: Install Dependencies

### 3.1 Via SSH
```bash
# Navigate to project directory
cd /home/yourusername/public_html/dv_portal

# Install dependencies locally
pip3 install --user -r requirements.txt

# Or use pip without user flag if you have permissions
pip3 install -r requirements.txt
```

### 3.2 Via cPanel Terminal (if available)
Use the cPanel terminal to run the same commands.

## Step 4: Configure Environment

### 4.1 Create .env file
Create a `.env` file in your project root:

```bash
# Copy from template
cp env_template.txt .env

# Edit with your settings
nano .env
```

### 4.2 Configure .env file
```env
# Django Settings
SECRET_KEY=your-very-long-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database (SQLite for simple setup)
# For MySQL, use: DATABASE_URL=mysql://username:password@localhost/dbname

# Email Configuration
EMAIL_HOST=mail.yourdomain.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=noreply@yourdomain.com
EMAIL_HOST_PASSWORD=your-email-password
DEFAULT_FROM_EMAIL=noreply@yourdomain.com

# Telegram Bot
TELEGRAM_BOT_TOKEN=your-bot-token
TELEGRAM_ADMIN_CHAT_ID=your-admin-chat-id

# Gemini AI
GEMINI_API_KEY=your-gemini-api-key
```

## Step 5: Database Setup

### 5.1 SQLite (Simplest)
No additional setup required - Django will create the database file.

### 5.2 MySQL Setup
1. Create MySQL database in cPanel
2. Create database user and assign privileges
3. Update DATABASE_URL in .env file

## Step 6: Initialize Django

```bash
# Navigate to project directory
cd /home/yourusername/public_html/dv_portal

# Run migrations
python3 manage.py migrate

# Create superuser
python3 manage.py createsuperuser

# Collect static files
python3 manage.py collectstatic --noinput
```

## Step 7: Configure Web Server

### 7.1 Update passenger_wsgi.py
Edit the file and update paths:
```python
# Update this line with your actual username
site.addsitedir('/home/YOURUSERNAME/.local/lib/python3.9/site-packages')
site.addsitedir('/home/YOURUSERNAME/public_html/dv_portal')
```

### 7.2 Update .htaccess
Edit the file and update paths:
```apache
PassengerPythonPath "/home/YOURUSERNAME/.local/bin:/usr/bin"
PassengerAppRoot "/home/YOURUSERNAME/public_html/dv_portal"
```

## Step 8: Set File Permissions

```bash
# Set proper permissions
chmod 644 passenger_wsgi.py
chmod 644 .htaccess
chmod -R 755 static/
chmod -R 755 media/
chmod 600 .env
```

## Step 9: Test Deployment

1. Visit your domain: `https://yourdomain.com`
2. Check if the homepage loads
3. Test registration and login
4. Access admin panel: `https://yourdomain.com/admin`

## Step 10: Configure Services

### 10.1 Set up Telegram Bot
1. Create bot via @BotFather on Telegram
2. Get bot token and add to .env
3. Set webhook (optional): `https://yourdomain.com/notifications/telegram/webhook/`

### 10.2 Configure Gemini AI
1. Get API key from Google AI Studio
2. Add to .env file

## Troubleshooting

### Common Issues

#### 1. 500 Internal Server Error
- Check error logs in cPanel
- Verify Python path in passenger_wsgi.py
- Ensure all dependencies are installed

#### 2. Static Files Not Loading
- Run `python3 manage.py collectstatic`
- Check .htaccess static file rules
- Verify STATIC_ROOT in settings.py

#### 3. Database Connection Error
- Verify DATABASE_URL in .env
- Check database credentials
- Ensure database exists

#### 4. Permission Denied Errors
- Set correct file permissions
- Check directory ownership
- Verify Python executable path

### Log Locations
- **cPanel Error Logs:** Usually in `/home/username/logs/`
- **Django Logs:** Check `dv_portal.log` in project directory
- **Apache Logs:** Available in cPanel Error Logs section

### Performance Optimization

1. **Enable caching** in Django settings
2. **Optimize database** queries
3. **Use CDN** for static files
4. **Enable compression** in .htaccess
5. **Set up proper caching headers**

## Security Checklist

- [ ] Set DEBUG=False in production
- [ ] Use strong SECRET_KEY
- [ ] Configure ALLOWED_HOSTS properly
- [ ] Set up SSL certificate
- [ ] Secure .env file permissions
- [ ] Regular security updates
- [ ] Monitor error logs

## Maintenance Tasks

### Regular Updates
```bash
# Update dependencies
pip3 install --upgrade -r requirements.txt

# Apply new migrations
python3 manage.py migrate

# Collect new static files
python3 manage.py collectstatic --noinput

# Restart application (touch passenger_wsgi.py)
touch passenger_wsgi.py
```

### Backup Strategy
1. **Database backup:** Regular MySQL dumps or SQLite file copies
2. **Media files backup:** User uploaded files
3. **Code backup:** Keep version control updated

## Support

If you encounter issues:
1. Check cPanel error logs
2. Review Django debug information
3. Contact hosting provider for server-specific issues
4. Refer to Django deployment documentation

## Additional Resources

- [Django Deployment Documentation](https://docs.djangoproject.com/en/stable/howto/deployment/)
- [Passenger Documentation](https://www.phusionpassenger.com/library/)
- [cPanel Python App Guide](https://docs.cpanel.net/cpanel/software/python-selector/)

---

**Important:** Always test in a staging environment before deploying to production!
