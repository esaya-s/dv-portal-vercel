import telebot
import logging
from django.conf import settings
from applications.models import DVApplication
from telebot import types
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize bot
try:
    bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
    logger.info("Telegram bot initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Telegram bot: {e}")
    bot = None

# Admin username for special commands
ADMIN_USERNAME = settings.TELEGRAM_ADMIN_USERNAME  # 'anvilutech'
BOT_NAME = settings.TELEGRAM_BOT_NAME  # 'DV2027'
BOT_USERNAME = settings.TELEGRAM_BOT_USERNAME  # 'dv20272etbot'


def send_contact_notification_to_admin(contact_message):
    """Send contact form notification to admin via Telegram"""
    try:
        if not bot:
            logger.error("Bot not initialized")
            return False
        
        admin_chat_id = settings.TELEGRAM_ADMIN_CHAT_ID
        
        # Format the contact message
        message_text = f"""
📧 *New Contact Message Received*

👤 *From:* {contact_message.name}
📧 *Email:* {contact_message.email}
📞 *Phone:* {contact_message.phone or 'Not provided'}
📝 *Subject:* {contact_message.subject}

💬 *Message:*
{contact_message.message}

⏰ *Received:* {contact_message.created_at.strftime('%Y-%m-%d %H:%M:%S')}

🔗 *Admin Panel:* /admin/core/contactmessage/
        """
        
        # Send message to admin
        bot.send_message(
            chat_id=admin_chat_id,
            text=message_text,
            parse_mode='Markdown'
        )
        
        logger.info(f"Contact notification sent to admin for message: {contact_message.subject}")
        return True
        
    except Exception as e:
        logger.error(f"Error sending contact notification: {e}")
        return False


def send_application_notification_to_admin(application):
    """
    Send notification to admin about new application
    
    Args:
        application (DVApplication): The application instance
    """
    if not bot:
        logger.error("Telegram bot not initialized")
        return False
    
    try:
        admin_chat_id = settings.TELEGRAM_ADMIN_CHAT_ID
        
        # Create message
        message = f"🔔 *NEW APPLICATION RECEIVED*\n\n"
        message += f"📝 *Application ID:* `{application.dv_id}`\n"
        message += f"👤 *Applicant:* {application.first_name} {application.last_name}\n"
        message += f"📧 *Email:* {application.email}\n"
        message += f"📱 *Phone:* {application.phone_number}\n"
        message += f"🌍 *Country:* {application.country_of_citizenship}\n"
        message += f"⏰ *Date:* {application.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        message += f"Check admin panel for more details."
        
        # Send message
        bot.send_message(admin_chat_id, message, parse_mode="Markdown")
        logger.info(f"Admin notification sent for application {application.dv_id}")
        return True
    except Exception as e:
        logger.error(f"Failed to send admin notification: {e}")
        
        # Try to find admin by username
        try:
            admin_username = ADMIN_USERNAME
            if admin_username.startswith('@'):
                admin_username = admin_username[1:]
                
            admin_chat = bot.get_chat('@' + admin_username)
            bot.send_message(admin_chat.id, message, parse_mode="Markdown")
            logger.info(f"Admin notification sent to @{admin_username} for application {application.dv_id}")
            return True
        except Exception as e2:
            logger.error(f"Failed to send admin notification via username: {e2}")
            return False


def send_confirmation_to_applicant(application):
    """
    Send confirmation message to applicant via Telegram
    
    Args:
        application (DVApplication): The application instance
    """
    if not bot:
        logger.error("Telegram bot not initialized")
        return False
    
    # Check if applicant has provided a Telegram username
    if not application.telegram_username:
        logger.warning(f"No Telegram username provided for application {application.dv_id}")
        return False
    
    try:
        # Format username (remove @ if present)
        username = application.telegram_username
        if username.startswith('@'):
            username = username[1:]
        
        # Create message
        message = f"✅ *DV-2027 Application Confirmation*\n\n"
        message += f"Dear *{application.first_name} {application.last_name}*,\n\n"
        message += f"Thank you for submitting your DV-2027 application through DV Portal Ethiopia.\n\n"
        message += f"📝 *Your Application ID:* `{application.dv_id}`\n\n"
        message += f"Please save this ID for checking your application status.\n\n"
        message += f"Your application is currently under review. We will notify you of any updates.\n\n"
        message += f"You can check your status anytime by sending your Application ID to this bot.\n\n"
        message += f"If you have any questions, please contact us through our website or reply to this message.\n\n"
        message += f"Best regards,\nDV Portal Ethiopia Team"
        
        # Try to find user by username and send message
        try:
            user_info = bot.get_chat('@' + username)
            bot.send_message(user_info.id, message, parse_mode="Markdown")
            
            # Save the chat_id for future communications
            application.telegram_chat_id = str(user_info.id)
            application.save(update_fields=['telegram_chat_id'])
            
            logger.info(f"Confirmation sent to applicant {application.dv_id} via Telegram")
            return True
        except Exception as e:
            logger.error(f"Failed to send confirmation via username: {e}")
            
            # Alternative approach: create a deep link for the user to start the bot
            start_payload = f"application_{application.dv_id}"
            bot_link = f"https://t.me/{BOT_USERNAME}?start={start_payload}"
            
            logger.info(f"Created bot link for application {application.dv_id}: {bot_link}")
            return bot_link
            
    except Exception as e:
        logger.error(f"Failed to send confirmation to applicant: {e}")
        return False


@bot.message_handler(commands=['start'])
def handle_start(message):
    """Handle /start command"""
    try:
        # Check if there's a payload (application ID)
        payload = message.text.split()
        if len(payload) > 1 and payload[1].startswith('application_'):
            application_id = payload[1].replace('application_', '')
            
            try:
                application = DVApplication.objects.get(dv_id=application_id)
                
                # Save the chat_id for future communications
                application.telegram_chat_id = str(message.chat.id)
                application.save(update_fields=['telegram_chat_id'])
                
                # Send confirmation message
                welcome_msg = f"✅ *DV-2027 Application Confirmation*\n\n"
                welcome_msg += f"Dear *{application.first_name} {application.last_name}*,\n\n"
                welcome_msg += f"Thank you for submitting your DV-2027 application through DV Portal Ethiopia.\n\n"
                welcome_msg += f"📝 *Your Application ID:* `{application.dv_id}`\n\n"
                welcome_msg += f"Please save this ID for checking your application status.\n\n"
                welcome_msg += f"Your application is currently under review. We will notify you of any updates.\n\n"
                welcome_msg += f"You can check your status anytime by sending your Application ID to this bot.\n\n"
                welcome_msg += f"If you have any questions, please contact us through our website or reply to this message.\n\n"
                welcome_msg += f"Best regards,\nDV Portal Ethiopia Team"
                
                bot.send_message(message.chat.id, welcome_msg, parse_mode="Markdown")
                
            except DVApplication.DoesNotExist:
                bot.send_message(message.chat.id, "Sorry, we couldn't find your application. Please contact support.")
        else:
            # Regular welcome message
            welcome_msg = f"Welcome to {BOT_NAME} Bot!\n\n"
            welcome_msg += "This bot will help you receive notifications about your DV-2027 application.\n\n"
            welcome_msg += "You can:\n"
            welcome_msg += "• Send your Application ID to check your status\n"
            welcome_msg += "• Use /status command followed by your application ID\n"
            welcome_msg += "• Use /help to see all available commands\n\n"
            welcome_msg += "To check your application status, simply send your Application ID (e.g., DV2027-XXXXXXXXXX)"
            
            bot.send_message(message.chat.id, welcome_msg)
    except Exception as e:
        logger.error(f"Error in start handler: {e}")
        bot.send_message(message.chat.id, "An error occurred. Please try again later.")


@bot.message_handler(commands=['status'])
def handle_status(message):
    """Handle /status command"""
    try:
        # Check if there's an application ID
        parts = message.text.split()
        if len(parts) > 1:
            application_id = parts[1]
            
            # Add prefix if not present
            if not application_id.startswith('DV2027-'):
                application_id = f"DV2027-{application_id}"
            
            try:
                application = DVApplication.objects.get(dv_id=application_id)
                
                # Send status message
                status_msg = f"📊 *Application Status*\n\n"
                status_msg += f"📝 *Application ID:* `{application.dv_id}`\n"
                status_msg += f"👤 *Applicant:* {application.first_name} {application.last_name}\n"
                status_msg += f"📅 *Submitted on:* {application.created_at.strftime('%Y-%m-%d')}\n\n"
                status_msg += f"*Current Status:* {application.get_status_display()}\n\n"
                
                if application.status == 'pending':
                    status_msg += "Your application is being processed. Please check back later."
                elif application.status == 'under_review':
                    status_msg += "Your application is currently under review by our team."
                elif application.status == 'approved':
                    status_msg += "Congratulations! Your application has been approved."
                elif application.status == 'rejected':
                    status_msg += "We're sorry, your application has been rejected."
                    if application.data_validation_message:
                        status_msg += f"\n\nReason: {application.data_validation_message}"
                
                bot.send_message(message.chat.id, status_msg, parse_mode="Markdown")
                
            except DVApplication.DoesNotExist:
                bot.send_message(message.chat.id, "Sorry, we couldn't find an application with that ID. Please check and try again.")
        else:
            bot.send_message(message.chat.id, "Please provide your application ID. Example: /status DV2027-XXXXXXXXXX")
    except Exception as e:
        logger.error(f"Error in status handler: {e}")
        bot.send_message(message.chat.id, "An error occurred. Please try again later.")


@bot.message_handler(commands=['help'])
def handle_help(message):
    """Handle /help command"""
    help_msg = f"*{BOT_NAME} Bot Help*\n\n"
    help_msg += "Available commands:\n\n"
    help_msg += "• /start - Start the bot\n"
    help_msg += "• /status [application_id] - Check your application status\n"
    help_msg += "• /help - Show this help message\n\n"
    help_msg += "You can also simply send your Application ID to check your status.\n\n"
    
    # Add admin commands if the message is from admin
    if message.from_user.username and message.from_user.username.lower() == ADMIN_USERNAME.lower().replace('@', ''):
        help_msg += "\n*Admin Commands:*\n\n"
        help_msg += "• /admin - Access admin panel\n"
        help_msg += "• /search [phone_number] - Search applications by phone number\n"
        help_msg += "• /update [application_id] [status] - Update application status\n"
        help_msg += "• /stats - View application statistics\n"
    
    help_msg += "\nIf you need further assistance, please contact us through our website."
    
    bot.send_message(message.chat.id, help_msg, parse_mode="Markdown")


@bot.message_handler(commands=['admin'])
def handle_admin(message):
    """Handle /admin command - Admin only"""
    if not message.from_user.username or message.from_user.username.lower() != ADMIN_USERNAME.lower().replace('@', ''):
        bot.send_message(message.chat.id, "Sorry, this command is only available for administrators.")
        return
    
    # Create admin panel keyboard
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Add buttons
    search_btn = types.InlineKeyboardButton("🔍 Search Applications", callback_data="admin_search")
    stats_btn = types.InlineKeyboardButton("📊 Application Stats", callback_data="admin_stats")
    pending_btn = types.InlineKeyboardButton("⏳ Pending Applications", callback_data="admin_pending")
    recent_btn = types.InlineKeyboardButton("🕒 Recent Applications", callback_data="admin_recent")
    
    markup.add(search_btn, stats_btn)
    markup.add(pending_btn, recent_btn)
    
    admin_msg = "👨‍💼 *Admin Panel*\n\n"
    admin_msg += "Welcome to the admin panel. Please select an option below:"
    
    bot.send_message(message.chat.id, admin_msg, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(commands=['search'])
def handle_search(message):
    """Handle /search command - Admin only"""
    if not message.from_user.username or message.from_user.username.lower() != ADMIN_USERNAME.lower().replace('@', ''):
        bot.send_message(message.chat.id, "Sorry, this command is only available for administrators.")
        return
    
    parts = message.text.split()
    if len(parts) > 1:
        search_term = parts[1]
        
        # Check if it's a phone number
        if re.match(r'^\+?[0-9]+$', search_term):
            try:
                applications = DVApplication.objects.filter(phone_number__contains=search_term)
                
                if applications.exists():
                    response = f"🔍 *Search Results for Phone: {search_term}*\n\n"
                    
                    for app in applications[:10]:  # Limit to 10 results
                        response += f"📝 *ID:* `{app.dv_id}`\n"
                        response += f"👤 *Name:* {app.first_name} {app.last_name}\n"
                        response += f"📱 *Phone:* {app.phone_number}\n"
                        response += f"📅 *Date:* {app.created_at.strftime('%Y-%m-%d')}\n"
                        response += f"🔹 *Status:* {app.get_status_display()}\n\n"
                    
                    if applications.count() > 10:
                        response += f"_...and {applications.count() - 10} more results._"
                    
                    bot.send_message(message.chat.id, response, parse_mode="Markdown")
                else:
                    bot.send_message(message.chat.id, f"No applications found with phone number containing: {search_term}")
            except Exception as e:
                logger.error(f"Error in search handler: {e}")
                bot.send_message(message.chat.id, "An error occurred while searching.")
        else:
            bot.send_message(message.chat.id, "Please provide a valid phone number to search.")
    else:
        bot.send_message(message.chat.id, "Please provide a phone number to search. Example: /search +251911234567")


@bot.message_handler(commands=['update'])
def handle_update(message):
    """Handle /update command - Admin only"""
    if not message.from_user.username or message.from_user.username.lower() != ADMIN_USERNAME.lower().replace('@', ''):
        bot.send_message(message.chat.id, "Sorry, this command is only available for administrators.")
        return
    
    parts = message.text.split()
    if len(parts) >= 3:
        application_id = parts[1]
        new_status = parts[2].lower()
        
        # Add prefix if not present
        if not application_id.startswith('DV2027-'):
            application_id = f"DV2027-{application_id}"
        
        # Validate status
        valid_statuses = {'pending', 'under_review', 'approved', 'rejected', 'incomplete'}
        if new_status not in valid_statuses:
            bot.send_message(message.chat.id, 
                            f"Invalid status. Please use one of: {', '.join(valid_statuses)}")
            return
        
        try:
            application = DVApplication.objects.get(dv_id=application_id)
            old_status = application.status
            
            # Update status
            application.status = new_status
            application.save(update_fields=['status'])
            
            # Send confirmation to admin
            bot.send_message(message.chat.id, 
                           f"✅ Status updated for {application_id}\n"
                           f"From: {old_status}\n"
                           f"To: {new_status}")
            
            # Notify applicant if they have a telegram_chat_id
            if application.telegram_chat_id:
                try:
                    notify_msg = f"📣 *Application Status Update*\n\n"
                    notify_msg += f"Dear *{application.first_name} {application.last_name}*,\n\n"
                    notify_msg += f"Your application status has been updated.\n\n"
                    notify_msg += f"📝 *Application ID:* `{application.dv_id}`\n"
                    notify_msg += f"🔹 *New Status:* {application.get_status_display()}\n\n"
                    
                    if new_status == 'approved':
                        notify_msg += "🎉 Congratulations! Your application has been approved.\n\n"
                        notify_msg += "Our team will contact you with further instructions."
                    elif new_status == 'rejected':
                        notify_msg += "We're sorry, your application has been rejected.\n\n"
                        notify_msg += "Please contact our support team for more information."
                    elif new_status == 'under_review':
                        notify_msg += "Your application is now under review by our team.\n\n"
                        notify_msg += "We will notify you once the review is complete."
                    
                    bot.send_message(application.telegram_chat_id, notify_msg, parse_mode="Markdown")
                    bot.send_message(message.chat.id, "✅ Applicant has been notified of the status change.")
                except Exception as e:
                    logger.error(f"Error notifying applicant: {e}")
                    bot.send_message(message.chat.id, "⚠️ Failed to notify applicant.")
            
        except DVApplication.DoesNotExist:
            bot.send_message(message.chat.id, f"Application with ID {application_id} not found.")
        except Exception as e:
            logger.error(f"Error in update handler: {e}")
            bot.send_message(message.chat.id, "An error occurred while updating the application.")
    else:
        bot.send_message(message.chat.id, 
                        "Please provide both application ID and new status.\n"
                        "Example: /update DV2027-XXXXXXXXXX approved")


@bot.message_handler(commands=['stats'])
def handle_stats(message):
    """Handle /stats command - Admin only"""
    if not message.from_user.username or message.from_user.username.lower() != ADMIN_USERNAME.lower().replace('@', ''):
        bot.send_message(message.chat.id, "Sorry, this command is only available for administrators.")
        return
    
    try:
        total_count = DVApplication.objects.count()
        pending_count = DVApplication.objects.filter(status='pending').count()
        review_count = DVApplication.objects.filter(status='under_review').count()
        approved_count = DVApplication.objects.filter(status='approved').count()
        rejected_count = DVApplication.objects.filter(status='rejected').count()
        
        stats_msg = "📊 *Application Statistics*\n\n"
        stats_msg += f"📝 *Total Applications:* {total_count}\n"
        stats_msg += f"⏳ *Pending:* {pending_count}\n"
        stats_msg += f"🔍 *Under Review:* {review_count}\n"
        stats_msg += f"✅ *Approved:* {approved_count}\n"
        stats_msg += f"❌ *Rejected:* {rejected_count}\n"
        
        bot.send_message(message.chat.id, stats_msg, parse_mode="Markdown")
    except Exception as e:
        logger.error(f"Error in stats handler: {e}")
        bot.send_message(message.chat.id, "An error occurred while fetching statistics.")


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    """Handle callback queries from inline keyboards"""
    try:
        if call.data == "admin_search":
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, 
                           "Please use the /search command followed by a phone number.\n"
                           "Example: /search +251911234567")
        
        elif call.data == "admin_stats":
            bot.answer_callback_query(call.id)
            handle_stats(call.message)
        
        elif call.data == "admin_pending":
            bot.answer_callback_query(call.id)
            try:
                pending_apps = DVApplication.objects.filter(status='pending').order_by('-created_at')[:10]
                
                if pending_apps.exists():
                    response = "⏳ *Pending Applications*\n\n"
                    
                    for app in pending_apps:
                        response += f"📝 *ID:* `{app.dv_id}`\n"
                        response += f"👤 *Name:* {app.first_name} {app.last_name}\n"
                        response += f"📱 *Phone:* {app.phone_number}\n"
                        response += f"📅 *Date:* {app.created_at.strftime('%Y-%m-%d')}\n\n"
                    
                    # Add update instructions
                    response += "_To update status, use:_\n"
                    response += "`/update [application_id] [new_status]`"
                    
                    bot.send_message(call.message.chat.id, response, parse_mode="Markdown")
                else:
                    bot.send_message(call.message.chat.id, "No pending applications found.")
            except Exception as e:
                logger.error(f"Error fetching pending applications: {e}")
                bot.send_message(call.message.chat.id, "An error occurred while fetching pending applications.")
        
        elif call.data == "admin_recent":
            bot.answer_callback_query(call.id)
            try:
                recent_apps = DVApplication.objects.all().order_by('-created_at')[:10]
                
                if recent_apps.exists():
                    response = "🕒 *Recent Applications*\n\n"
                    
                    for app in recent_apps:
                        response += f"📝 *ID:* `{app.dv_id}`\n"
                        response += f"👤 *Name:* {app.first_name} {app.last_name}\n"
                        response += f"🔹 *Status:* {app.get_status_display()}\n"
                        response += f"📅 *Date:* {app.created_at.strftime('%Y-%m-%d')}\n\n"
                    
                    bot.send_message(call.message.chat.id, response, parse_mode="Markdown")
                else:
                    bot.send_message(call.message.chat.id, "No applications found.")
            except Exception as e:
                logger.error(f"Error fetching recent applications: {e}")
                bot.send_message(call.message.chat.id, "An error occurred while fetching recent applications.")
    
    except Exception as e:
        logger.error(f"Error in callback handler: {e}")
        bot.send_message(call.message.chat.id, "An error occurred. Please try again later.")


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    """Handle all other messages - Check if it's an application ID"""
    try:
        text = message.text.strip()
        
        # Check if it looks like an application ID
        if re.match(r'^DV2027-[A-Z0-9]+$', text):
            application_id = text
        elif re.match(r'^[A-Z0-9]+$', text):
            # Add prefix if not present
            application_id = f"DV2027-{text}"
        else:
            # Not an application ID, send help message
            bot.send_message(message.chat.id, 
                           "I don't understand that command. Please send your Application ID to check status, or use /help to see available commands.")
            return
        
        try:
            application = DVApplication.objects.get(dv_id=application_id)
            
            # Save the chat_id if not already saved
            if not application.telegram_chat_id:
                application.telegram_chat_id = str(message.chat.id)
                application.save(update_fields=['telegram_chat_id'])
            
            # Send status message
            status_msg = f"📊 *Application Status*\n\n"
            status_msg += f"📝 *Application ID:* `{application.dv_id}`\n"
            status_msg += f"👤 *Applicant:* {application.first_name} {application.last_name}\n"
            status_msg += f"📅 *Submitted on:* {application.created_at.strftime('%Y-%m-%d')}\n\n"
            status_msg += f"*Current Status:* {application.get_status_display()}\n\n"
            
            if application.status == 'pending':
                status_msg += "Your application is being processed. Please check back later."
            elif application.status == 'under_review':
                status_msg += "Your application is currently under review by our team."
            elif application.status == 'approved':
                status_msg += "Congratulations! Your application has been approved."
            elif application.status == 'rejected':
                status_msg += "We're sorry, your application has been rejected."
                if application.data_validation_message:
                    status_msg += f"\n\nReason: {application.data_validation_message}"
            
            bot.send_message(message.chat.id, status_msg, parse_mode="Markdown")
            
        except DVApplication.DoesNotExist:
            bot.send_message(message.chat.id, f"Sorry, we couldn't find an application with ID: {application_id}. Please check and try again.")
    except Exception as e:
        logger.error(f"Error in message handler: {e}")
        bot.send_message(message.chat.id, "An error occurred. Please try again later.")


# Start the bot in a separate thread (if this file is imported)
def start_bot():
    """Start the bot in a separate thread"""
    if bot:
        try:
            logger.info("Starting Telegram bot polling...")
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except Exception as e:
            logger.error(f"Error starting Telegram bot: {e}")
    else:
        logger.error("Cannot start bot - not initialized")


# If this file is run directly, start the bot
if __name__ == "__main__":
    start_bot()