from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class BotCommand(models.Model):
    """Bot command model"""
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class TelegramUser(models.Model):
    """Telegram user model"""
    
    chat_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    
    is_admin = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.username:
            return f"@{self.username}"
        return f"{self.chat_id}"


class TelegramNotification(models.Model):
    """Telegram notification model"""
    
    telegram_user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    application = models.ForeignKey('applications.DVApplication', on_delete=models.CASCADE, null=True, blank=True)
    
    message = models.TextField()
    sent = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Notification to {self.telegram_user} at {self.created_at}"


class AdminNotification(models.Model):
    """Admin notification model"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    application = models.ForeignKey('applications.DVApplication', on_delete=models.CASCADE, null=True, blank=True)
    
    title = models.CharField(max_length=200)
    message = models.TextField()
    
    is_read = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title