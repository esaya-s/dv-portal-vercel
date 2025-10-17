#!/bin/bash
echo "🌐 Setting up Django for anvilu.com (no port)..."
echo "================================================"

echo ""
echo "📋 Choose your web server:"
echo "1. Apache with mod_wsgi"
echo "2. Nginx with Gunicorn"
echo "3. Simple Gunicorn with systemd"
echo ""

read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo "🔧 Setting up Apache with mod_wsgi..."
        
        # Install Apache and mod_wsgi
        sudo apt update
        sudo apt install apache2 libapache2-mod-wsgi-py3
        
        # Copy Apache configuration
        sudo cp apache_anvilu.conf /etc/apache2/sites-available/anvilu.com.conf
        
        # Enable site
        sudo a2ensite anvilu.com.conf
        sudo a2dissite 000-default
        
        # Enable mod_wsgi
        sudo a2enmod wsgi
        
        # Restart Apache
        sudo systemctl restart apache2
        
        echo "✅ Apache configured for anvilu.com"
        echo "🌐 Your site is now available at: http://anvilu.com"
        ;;
        
    2)
        echo "🔧 Setting up Nginx with Gunicorn..."
        
        # Install Nginx
        sudo apt update
        sudo apt install nginx
        
        # Copy Nginx configuration
        sudo cp nginx_anvilu.conf /etc/nginx/sites-available/anvilu.com
        
        # Enable site
        sudo ln -s /etc/nginx/sites-available/anvilu.com /etc/nginx/sites-enabled/
        sudo rm -f /etc/nginx/sites-enabled/default
        
        # Test configuration
        sudo nginx -t
        
        # Start Gunicorn
        echo "🚀 Starting Gunicorn..."
        gunicorn --bind 127.0.0.1:8000 --daemon dv_portal.wsgi:application
        
        # Restart Nginx
        sudo systemctl restart nginx
        
        echo "✅ Nginx configured for anvilu.com"
        echo "🌐 Your site is now available at: http://anvilu.com"
        ;;
        
    3)
        echo "🔧 Setting up simple Gunicorn with systemd..."
        
        # Create systemd service
        sudo tee /etc/systemd/system/anvilu-django.service > /dev/null <<EOF
[Unit]
Description=Django application for anvilu.com
After=network.target

[Service]
Type=notify
User=anviluco
Group=anviluco
WorkingDirectory=/home/anviluco/DV
Environment="DJANGO_SETTINGS_MODULE=dv_portal.settings_production"
ExecStart=/home/anviluco/virtualenv/DV/3.10/bin/gunicorn --bind 0.0.0.0:80 --workers 3 dv_portal.wsgi:application
ExecReload=/bin/kill -s HUP \$MAINPID
Restart=always

[Install]
WantedBy=multi-user.target
EOF
        
        # Reload systemd and start service
        sudo systemctl daemon-reload
        sudo systemctl enable anvilu-django
        sudo systemctl start anvilu-django
        
        echo "✅ Gunicorn service configured for anvilu.com"
        echo "🌐 Your site is now available at: http://anvilu.com"
        ;;
        
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "🎉 Setup complete!"
echo "📋 Next steps:"
echo "1. Configure your DNS to point anvilu.com to this server"
echo "2. Test your site: http://anvilu.com"
echo "3. Admin panel: http://anvilu.com/admin/"
echo "4. Username: usadv27"
echo "5. Email: esayasdesta00@gmail.com"
echo ""
echo "🔧 To check status:"
echo "  - Apache: sudo systemctl status apache2"
echo "  - Nginx: sudo systemctl status nginx"
echo "  - Gunicorn: sudo systemctl status anvilu-django"
