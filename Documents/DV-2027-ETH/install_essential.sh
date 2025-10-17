#!/bin/bash
echo "🚀 Installing Essential Django Packages..."
echo "================================================"

echo ""
echo "📦 Installing core Django packages..."

# Install the most essential packages first
pip install Django>=4.2.0
pip install django-crispy-forms>=2.0
pip install crispy-bootstrap5>=0.7
pip install django-countries>=7.5.1
pip install django-phonenumber-field>=7.1.0
pip install phonenumbers>=8.13.0
pip install python-telegram-bot>=20.0
pip install Pillow>=10.0.0
pip install whitenoise>=6.5.0
pip install gunicorn>=21.2.0
pip install python-dotenv>=1.0.0
pip install python-decouple>=3.8

echo ""
echo "📦 Installing database drivers..."
pip install psycopg2-binary>=2.9.0
pip install mysqlclient>=2.2.0

echo ""
echo "📦 Installing additional packages..."
pip install django-cors-headers>=4.0.0
pip install django-storages>=1.14.0
pip install django-anymail>=10.0
pip install redis>=4.5.0
pip install django-redis>=5.2.0
pip install sentry-sdk>=1.32.0
pip install pytest>=7.4.0
pip install pytest-django>=4.5.0
pip install black>=23.0.0
pip install flake8>=6.0.0
pip install djangorestframework>=3.14.0
pip install django-filter>=23.0.0
pip install celery>=5.3.0
pip install django-celery-beat>=2.5.0
pip install requests>=2.31.0
pip install python-dateutil>=2.8.0
pip install pytz>=2023.3
pip install cryptography>=41.0.0
pip install ujson>=5.8.0
pip install httpx>=0.24.0
pip install django-environ>=0.10.0
pip install django-health-check>=3.17.0
pip install django-admin-interface>=0.20.0
pip install python-magic>=0.4.27
pip install qrcode>=7.4.0
pip install reportlab>=4.0.0
pip install xlrd>=2.0.0
pip install xlsxwriter>=3.1.0
pip install django-compressor>=4.4.0
pip install django-allauth>=0.54.0
pip install channels>=4.0.0
pip install channels-redis>=4.1.0
pip install django-rq>=2.8.0
pip install django-ckeditor>=6.7.0
pip install django-dbbackup>=3.3.0
pip install django-maintenance-mode>=0.16.0
pip install django-silk>=5.0.0
pip install django-tenants>=3.5.0
pip install django-waffle>=3.0.0
pip install django-audit-log>=2.0.0
pip install django-model-utils>=4.3.0
pip install django-uuidfield>=0.5.0
pip install django-timezone-field>=6.0.0
pip install django-autoslug>=1.9.0
pip install django-templated-email>=3.0.0
pip install django-formtools>=2.4.0
pip install django-pure-pagination>=0.3.0
pip install django-bootstrap-breadcrumbs>=0.9.0
pip install django-modal-forms>=1.5.0
pip install django-ajax-selects>=1.9.0
pip install django-filebrowser>=3.14.0
pip install django-imagekit>=4.1.0
pip install sorl-thumbnail>=12.9.0
pip install django-taggit>=4.0.0
pip install django-mptt>=0.14.0
pip install django-treebeard>=4.7.0
pip install django-bulk-update>=2.2.0
pip install django-import-export>=3.2.0
pip install django-excel>=0.0.7
pip install django-jsonfield>=2.0.0

echo ""
echo "🎉 All packages installed successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Run: python manage.py migrate"
echo "2. Run: python manage.py collectstatic --noinput"
echo "3. Run: python manage.py createsuperuser"
echo "4. Run: python manage.py runserver"
echo ""
echo "🚀 Your Django app is ready!"
