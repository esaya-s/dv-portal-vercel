#!/bin/bash
# Deployment script for cPanel
# This script helps deploy the Django application and Telegram bot

set -e  # Exit on any error

echo "🚀 Starting DV Portal Ethiopia Deployment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    print_error "manage.py not found. Please run this script from the project root directory."
    exit 1
fi

print_status "Setting up directories..."
mkdir -p logs
mkdir -p staticfiles
mkdir -p media

print_status "Installing Python dependencies..."
pip install -r requirements.txt

print_status "Collecting static files..."
python manage.py collectstatic --noinput --settings=dv_portal.settings_production

print_status "Running database migrations..."
python manage.py migrate --settings=dv_portal.settings_production

print_status "Creating superuser (if needed)..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell --settings=dv_portal.settings_production

print_status "Setting up Telegram bot..."
python start_telegram_bot.py &

print_status "Deployment completed successfully!"
print_warning "Don't forget to:"
print_warning "1. Update your domain name in settings_production.py"
print_warning "2. Set up environment variables in cPanel"
print_warning "3. Configure your database credentials"
print_warning "4. Set up SSL certificate"
print_warning "5. Test the Telegram bot functionality"

echo ""
print_status "Your Django application should now be running!"
print_status "Telegram bot is running in the background."
