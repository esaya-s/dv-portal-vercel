from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class SystemSettings(models.Model):
    """System-wide settings"""
    
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    description = models.CharField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.key}: {self.value[:50]}"
    
    class Meta:
        verbose_name_plural = "System Settings"


class FAQ(models.Model):
    """Frequently Asked Questions"""
    
    question = models.CharField(max_length=500)
    answer = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ('general', 'General'),
        ('application', 'Application Process'),
        ('payment', 'Payment'),
        ('documents', 'Documents'),
        ('eligibility', 'Eligibility'),
        ('technical', 'Technical Support'),
    ])
    
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['category', 'order', 'question']
        
    def __str__(self):
        return self.question


class ContactMessage(models.Model):
    """Contact form messages"""
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Status
    status = models.CharField(max_length=20, choices=[
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ], default='new')
    
    responded = models.BooleanField(default=False)
    response = models.TextField(blank=True)
    responded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='contact_responses'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.name} - {self.subject[:50]}"


class Announcement(models.Model):
    """System announcements"""
    
    title = models.CharField(max_length=300)
    content = models.TextField()
    
    announcement_type = models.CharField(max_length=20, choices=[
        ('info', 'Information'),
        ('warning', 'Warning'),
        ('success', 'Success'),
        ('danger', 'Important Alert'),
    ], default='info')
    
    # Display settings
    show_on_homepage = models.BooleanField(default=True)
    show_on_dashboard = models.BooleanField(default=True)
    show_until = models.DateTimeField(null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title
