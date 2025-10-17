from django.core.management.base import BaseCommand
from notifications.telegram_bot import start_bot
import threading
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Starts the Telegram bot in a background thread'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting Telegram bot...'))
        
        # Start the bot in a separate thread
        bot_thread = threading.Thread(target=start_bot)
        bot_thread.daemon = True  # This ensures the thread will exit when the main program exits
        bot_thread.start()
        
        self.stdout.write(self.style.SUCCESS('Telegram bot started in background thread'))
        self.stdout.write(self.style.WARNING('Keep this process running to maintain the bot connection'))
        
        # Keep the main thread running
        try:
            # This will keep the main thread alive until interrupted
            bot_thread.join()
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING('Received keyboard interrupt, shutting down...'))
        except Exception as e:
            logger.error(f"Error in bot thread: {e}")
            self.stdout.write(self.style.ERROR(f'Error in bot thread: {e}'))

