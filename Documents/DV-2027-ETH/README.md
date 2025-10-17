# DV Portal Ethiopia 🇺🇸🇪🇹

Professional assistance platform for Ethiopian citizens applying to the US Diversity Visa Program. This Django-based system provides comprehensive application management, AI-powered validation, Telegram integration, and payment processing.

## 🌟 Features

### Core Functionality
- **User Registration & Authentication** - Secure user accounts with email/phone verification
- **DV Application Management** - Complete application forms similar to official US DV system
- **Payment Processing** - 800 ETB fee collection with proof upload and verification
- **AI-Powered Validation** - Gemini AI integration for photo and application data validation
- **Telegram Bot Integration** - Real-time notifications and status updates
- **Admin Dashboard** - Comprehensive management interface with search capabilities

### Technical Features
- **Random ID Generation** - DV2027-XXXXXXXXXXX format confirmation numbers
- **Photo Validation** - US DV photo requirements checking with white background detection
- **Family Member Support** - Spouse and children information management
- **Document Management** - Secure file upload and validation
- **Multi-language Support** - Designed for Ethiopian users with English interface
- **Mobile Responsive** - Bootstrap-based responsive design
- **cPanel Deployment Ready** - Configured for shared hosting deployment

### Security & Compliance
- **Data Encryption** - All sensitive data encrypted
- **Privacy Policy** - Comprehensive privacy protection similar to US government standards
- **Terms of Service** - Clear terms and conditions
- **Audit Trail** - Complete application status tracking
- **Secure File Storage** - Protected document and photo storage

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 4.2+
- SQLite/MySQL/PostgreSQL
- Telegram Bot Token
- Google Gemini AI API Key

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd dv-portal-ethiopia
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
# Copy environment template
cp env_template.txt .env

# Edit .env with your configuration
nano .env
```

5. **Set up database**
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **Collect static files**
```bash
python manage.py collectstatic
```

7. **Run development server**
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the application.

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following configurations:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database
DATABASE_URL=sqlite:///db.sqlite3
# For MySQL: DATABASE_URL=mysql://username:password@localhost/dbname

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@dvportal.com

# Telegram Bot
TELEGRAM_BOT_TOKEN=your-bot-token-from-botfather
TELEGRAM_ADMIN_CHAT_ID=your-admin-chat-id

# Gemini AI
GEMINI_API_KEY=your-gemini-api-key-from-google-ai-studio
```

### Telegram Bot Setup

1. **Create bot with BotFather**
```
/start
/newbot
DV Portal Ethiopia Bot
dvportal_ethiopia_bot
```

2. **Get bot token and add to .env file**

3. **Set up webhook (production only)**
```bash
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook" \
     -d "url=https://yourdomain.com/notifications/telegram/webhook/"
```

### Gemini AI Setup

1. **Get API key from Google AI Studio**
   - Visit: https://makersuite.google.com/app/apikey
   - Create new API key
   - Add to .env file

2. **Configure AI prompts**
   - Photo validation prompts are in `core/gemini_service.py`
   - Customize for specific requirements

## 📱 Telegram Bot Commands

### User Commands
- `/start` - Initialize bot and get welcome message
- `/help` - Show available commands
- `/status` - Check DV application status
- `/verify <phone>` - Link Telegram account with user account

### Admin Commands (Admin Chat Only)
- `/search <phone>` - Search user by phone number
- Get notifications for new applications, payments, etc.

## 💳 Payment System

### Supported Payment Methods
- Bank Transfer
- Mobile Money (M-Birr, etc.)
- TeleBirr
- CBE Birr
- Cash Deposit

### Payment Flow
1. User creates application
2. System generates payment request (800 ETB)
3. User makes payment via preferred method
4. User uploads payment proof screenshot
5. Admin verifies payment
6. Application processing begins

## 🤖 AI Validation Features

### Photo Validation
- **White background detection**
- **Facial expression analysis**
- **Head position and size validation**
- **Image quality assessment**
- **Lighting and shadow detection**
- **US DV photo requirements compliance**

### Application Validation
- **Data completeness checking**
- **Consistency validation**
- **Eligibility requirements verification**
- **Name and address formatting**
- **Date logic validation**

## 🏗️ Architecture

### Project Structure
```
dv_portal/
├── accounts/           # User management
├── applications/       # DV applications
├── core/              # Main functionality
├── notifications/     # Telegram integration
├── payments/          # Payment processing
├── static/            # Static files
├── templates/         # HTML templates
├── media/             # User uploads
└── manage.py
```

### Key Models
- **User** - Custom user with Ethiopian-specific fields
- **DVApplication** - Main application data
- **Payment** - Payment tracking and verification
- **TelegramNotification** - Message history
- **AdminNotification** - Admin alerts

## 🚀 Deployment

### cPanel Deployment
See [CPANEL_DEPLOYMENT.md](CPANEL_DEPLOYMENT.md) for detailed cPanel deployment instructions.

### Production Checklist
- [ ] Set `DEBUG=False`
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Set up SSL certificate
- [ ] Configure email backend
- [ ] Set up database backups
- [ ] Configure logging
- [ ] Set up monitoring
- [ ] Test Telegram bot
- [ ] Verify AI services
- [ ] Test payment flow

## 📊 Admin Features

### Admin Dashboard
- **Application management** - View, approve, reject applications
- **Payment verification** - Approve/reject payment proofs
- **User search** - Search by phone, email, name
- **Statistics** - Application and payment analytics
- **Notification management** - Send announcements

### Search Functionality
- Search users by phone number
- Filter applications by status
- Payment verification queue
- Generate reports

## 🔧 API Integration

### External Services
- **Telegram Bot API** - User notifications
- **Google Gemini AI** - Validation services
- **Payment Gateways** - (Future integration)
- **Email Services** - User communications

### Webhook Endpoints
- `/notifications/telegram/webhook/` - Telegram bot webhook
- Custom webhooks for payment providers (when integrated)

## 🛡️ Security Features

### Data Protection
- **Encrypted storage** for sensitive data
- **Secure file uploads** with validation
- **CSRF protection** on all forms
- **SQL injection prevention**
- **XSS protection**

### Privacy Compliance
- **GDPR-inspired** privacy practices
- **Data retention policies**
- **User consent management**
- **Right to deletion**

## 📈 Monitoring & Analytics

### Logging
- **Application logs** - User actions and errors
- **Payment logs** - Transaction tracking
- **Telegram logs** - Message history
- **AI validation logs** - Validation results

### Metrics
- Application success rates
- Payment processing times
- User engagement metrics
- AI validation accuracy

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is proprietary software developed for DV Portal Ethiopia.

## 📞 Support

- **Email:** support@dvportal-ethiopia.com
- **Telegram:** @anvilutech
- **Website:** https://dvportal-ethiopia.com

## ⚠️ Important Disclaimers

1. **Not affiliated with US Government** - This is an independent service provider
2. **No guarantee of selection** - DV lottery selection is entirely up to US Department of State
3. **Service fee is non-refundable** - Payment is for assistance services only
4. **Accurate information required** - False information may lead to disqualification

## 🎯 Roadmap

- [ ] Multi-language support (Amharic)
- [ ] Mobile app development
- [ ] Advanced analytics dashboard
- [ ] Automated document verification
- [ ] Integration with more payment providers
- [ ] SMS notification system
- [ ] Video call support integration

---

**Built with ❤️ for the Ethiopian community pursuing the American Dream**
