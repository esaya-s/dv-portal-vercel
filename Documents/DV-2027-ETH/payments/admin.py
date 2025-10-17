from django.contrib import admin
from django.utils.html import format_html
from .models import Payment, PaymentInstruction, PaymentNotification


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Payment admin with verification tools"""
    
    list_display = ('id', 'user', 'amount', 'currency', 'payment_method', 'status', 'created_at', 'view_proof')
    list_filter = ('status', 'payment_method', 'currency', 'created_at')
    search_fields = ('user__email', 'user__phone_number', 'sender_name', 'transaction_id')
    readonly_fields = ('created_at', 'updated_at', 'verified_at')
    raw_id_fields = ('user', 'application', 'verified_by')
    
    fieldsets = (
        ('Payment Info', {
            'fields': ('user', 'application', 'amount', 'currency', 'payment_method')
        }),
        ('Transaction Details', {
            'fields': ('transaction_id', 'sender_name', 'sender_phone', 'bank_name', 'account_number')
        }),
        ('Proof', {
            'fields': ('payment_proof',)
        }),
        ('Verification', {
            'fields': ('status', 'verified_by', 'verification_notes', 'verified_at')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['approve_payments', 'reject_payments']
    
    def view_proof(self, obj):
        if obj.payment_proof:
            return format_html(
                '<a href="{}" target="_blank">View Proof</a>',
                obj.payment_proof.url
            )
        return "No proof"
    view_proof.short_description = "Payment Proof"
    
    def approve_payments(self, request, queryset):
        count = queryset.update(status='approved', verified_by=request.user)
        self.message_user(request, f'{count} payments approved.')
    approve_payments.short_description = "Approve selected payments"
    
    def reject_payments(self, request, queryset):
        count = queryset.update(status='rejected', verified_by=request.user)
        self.message_user(request, f'{count} payments rejected.')
    reject_payments.short_description = "Reject selected payments"


@admin.register(PaymentInstruction)
class PaymentInstructionAdmin(admin.ModelAdmin):
    """Payment instruction admin"""
    
    list_display = ('instruction_type', 'title', 'is_active', 'updated_at')
    list_filter = ('instruction_type', 'is_active')


@admin.register(PaymentNotification)
class PaymentNotificationAdmin(admin.ModelAdmin):
    """Payment notification admin"""
    
    list_display = ('payment', 'notification_type', 'sent_via_telegram', 'sent_via_email', 'created_at')
    list_filter = ('notification_type', 'sent_via_telegram', 'sent_via_email')
    raw_id_fields = ('payment',)
