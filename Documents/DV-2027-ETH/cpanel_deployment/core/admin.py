from django.contrib import admin
from .models import SystemSettings, FAQ, ContactMessage, Announcement


@admin.register(SystemSettings)
class SystemSettingsAdmin(admin.ModelAdmin):
    """System settings admin"""
    
    list_display = ('key', 'value', 'is_active', 'updated_at')
    list_filter = ('is_active', 'updated_at')
    search_fields = ('key', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """FAQ admin"""
    
    list_display = ('question', 'category', 'order', 'is_active', 'updated_at')
    list_filter = ('category', 'is_active')
    search_fields = ('question', 'answer')
    ordering = ('category', 'order', 'question')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Contact message admin"""
    
    list_display = ('name', 'email', 'subject', 'status', 'responded', 'created_at')
    list_filter = ('status', 'responded', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'updated_at')
    raw_id_fields = ('user', 'responded_by')
    
    fieldsets = (
        ('Message Info', {
            'fields': ('name', 'email', 'phone', 'subject', 'message', 'user')
        }),
        ('Status', {
            'fields': ('status', 'responded', 'response', 'responded_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    """Announcement admin"""
    
    list_display = ('title', 'announcement_type', 'show_on_homepage', 'show_on_dashboard', 'is_active', 'created_at')
    list_filter = ('announcement_type', 'show_on_homepage', 'show_on_dashboard', 'is_active', 'created_at')
    search_fields = ('title', 'content')
    raw_id_fields = ('created_by',)
    readonly_fields = ('created_at', 'updated_at')
