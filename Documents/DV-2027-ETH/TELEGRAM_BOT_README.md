# DV-2027 Ethiopia Portal - Telegram Bot Integration

## 🤖 Telegram Bot Features

The DV-2027 Ethiopia Portal includes a comprehensive Telegram bot integration that provides:

### For Applicants:
- **Application Confirmation**: Automatic confirmation messages when applications are submitted
- **Status Checking**: Check application status by sending your Application ID to the bot
- **Real-time Updates**: Receive notifications when application status changes
- **Deep Link Support**: Click links to start conversations with the bot

### For Administrators (@anvilutech):
- **Admin Panel**: Access admin controls via Telegram
- **Application Search**: Search applications by phone number
- **Status Management**: Update application statuses directly from Telegram
- **Statistics**: View application statistics and pending applications
- **Real-time Notifications**: Get notified of new applications instantly

## 🚀 Bot Configuration

### Bot Details:
- **Bot Name**: DV2027
- **Bot Username**: @dv20272etbot
- **Admin Username**: @anvilutech

### Environment Variables Required:
```bash
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_ADMIN_USERNAME=anvilutech
TELEGRAM_BOT_NAME=DV2027
TELEGRAM_BOT_USERNAME=dv20272etbot
TELEGRAM_ADMIN_CHAT_ID=your_admin_chat_id_here
```

## 📱 Bot Commands

### User Commands:
- `/start` - Start the bot and get welcome message
- `/status [application_id]` - Check application status
- `/help` - Show help message
- Send Application ID directly - Quick status check

### Admin Commands (for @anvilutech):
- `/admin` - Access admin panel with inline keyboard
- `/search [phone_number]` - Search applications by phone number
- `/update [application_id] [status]` - Update application status
- `/stats` - View application statistics

### Admin Panel Options:
- 🔍 Search Applications
- 📊 Application Stats
- ⏳ Pending Applications
- 🕒 Recent Applications

## 🔧 Setup Instructions

### 1. Create Telegram Bot:
1. Message @BotFather on Telegram
2. Use `/newbot` command
3. Set bot name: "DV2027"
4. Set bot username: "dv20272etbot"
5. Copy the bot token

### 2. Configure Environment:
Add the bot token to your `.env` file:
```bash
TELEGRAM_BOT_TOKEN=your_bot_token_from_botfather
TELEGRAM_ADMIN_USERNAME=anvilutech
TELEGRAM_BOT_NAME=DV2027
TELEGRAM_BOT_USERNAME=dv20272etbot
```

### 3. Start the Bot:
```bash
# Start the bot in background
python manage.py start_telegram_bot

# Or test the bot configuration
python test_telegram_bot.py
```

## 📋 Application Flow

### When User Submits Application:
1. **Web Form Submission**: User fills out application form
2. **Telegram Notification**: Bot sends confirmation to user (if username provided)
3. **Admin Alert**: Bot notifies admin (@anvilutech) of new application
4. **Deep Link**: If direct message fails, bot generates deep link for user

### When Admin Updates Status:
1. **Admin Command**: Admin uses `/update` command
2. **Status Change**: Application status updated in database
3. **User Notification**: Bot automatically notifies applicant of status change
4. **Confirmation**: Admin receives confirmation of update

## 🔍 Search Functionality

### Phone Number Search:
```
/search +251911234567
```
Returns all applications with matching phone numbers.

### Application ID Search:
Users can send their Application ID directly to get status:
```
DV2027-XXXXXXXXXX
```

## 📊 Status Management

### Available Statuses:
- `pending` - Application submitted, awaiting processing
- `under_review` - Application being reviewed by team
- `approved` - Application approved
- `rejected` - Application rejected
- `incomplete` - Application missing required information

### Status Update Command:
```
/update DV2027-XXXXXXXXXX approved
```

## 🛠️ Technical Implementation

### Files Structure:
```
notifications/
├── telegram_bot.py          # Main bot logic
├── models.py               # Database models
├── admin.py                # Django admin configuration
└── management/
    └── commands/
        └── start_telegram_bot.py  # Management command to start bot
```

### Key Functions:
- `send_application_notification_to_admin()` - Notify admin of new applications
- `send_confirmation_to_applicant()` - Send confirmation to applicants
- `handle_start()` - Handle /start command
- `handle_status()` - Handle status checking
- `handle_admin()` - Handle admin panel
- `handle_search()` - Handle application search
- `handle_update()` - Handle status updates

## 🚨 Error Handling

The bot includes comprehensive error handling:
- **Chat Not Found**: Falls back to deep links
- **Invalid Commands**: Provides helpful error messages
- **Database Errors**: Logs errors and notifies users
- **Network Issues**: Retries and graceful degradation

## 📝 Logging

All bot activities are logged with timestamps:
- Application notifications
- Status updates
- Admin commands
- Error messages

## 🔐 Security

- **Admin Verification**: Only @anvilutech can access admin commands
- **Input Validation**: All inputs are validated before processing
- **Error Messages**: Sensitive information is not exposed in error messages

## 🎯 Usage Examples

### For Users:
1. Submit application on website
2. Receive confirmation message on Telegram
3. Send Application ID to bot to check status
4. Receive updates when status changes

### For Admin:
1. Receive notification of new application
2. Use `/search` to find specific applications
3. Use `/update` to change application status
4. Use `/stats` to view overall statistics

## 🚀 Deployment

The bot runs as a background process and can be deployed alongside the Django application. Use the management command to start it:

```bash
python manage.py start_telegram_bot
```

The bot will continue running until manually stopped or the server restarts.
