from django.db import models
from django.conf import settings
from decimal import Decimal


class Payment(models.Model):
    """Payment model for DV application fees"""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('refunded', 'Refunded'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('bank_transfer', 'Bank Transfer'),
        ('mobile_money', 'Mobile Money'),
        ('cash_deposit', 'Cash Deposit'),
        ('telebirr', 'TeleBirr'),
        ('cbe_birr', 'CBE Birr'),
        ('other', 'Other'),
    ]
    
    # Payment Information
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    application = models.OneToOneField('applications.DVApplication', on_delete=models.CASCADE, related_name='payment')
    
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('800.00'))
    currency = models.CharField(max_length=3, default='ETB')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    
    # Payment Proof
    payment_proof = models.ImageField(
        upload_to='payment_proofs/',
        help_text="Upload screenshot or photo of payment receipt"
    )
    
    # Transaction Details
    transaction_id = models.CharField(max_length=200, blank=True, help_text="Bank/Mobile transaction ID")
    sender_name = models.CharField(max_length=200, help_text="Name of person who made the payment")
    sender_phone = models.CharField(max_length=20, blank=True, help_text="Phone number used for payment")
    
    # Bank Details (if bank transfer)
    bank_name = models.CharField(max_length=100, blank=True)
    account_number = models.CharField(max_length=50, blank=True)
    
    # Status and Verification
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    verified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='verified_payments'
    )
    verification_notes = models.TextField(blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Payment {self.id} - {self.user.get_full_name()} - {self.amount} {self.currency}"
    
    def is_verified(self):
        return self.status == 'approved'


class PaymentInstruction(models.Model):
    """Payment instructions for users"""
    
    instruction_type = models.CharField(max_length=20, choices=[
        ('bank_transfer', 'Bank Transfer'),
        ('mobile_money', 'Mobile Money'),
        ('cash_deposit', 'Cash Deposit'),
        ('telebirr', 'TeleBirr'),
        ('cbe_birr', 'CBE Birr'),
    ], unique=True)
    
    title = models.CharField(max_length=200)
    instructions = models.TextField()
    account_details = models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Instructions for {self.get_instruction_type_display()}"


class PaymentNotification(models.Model):
    """Track payment-related notifications"""
    
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=50, choices=[
        ('payment_received', 'Payment Received'),
        ('payment_approved', 'Payment Approved'),
        ('payment_rejected', 'Payment Rejected'),
        ('refund_processed', 'Refund Processed'),
    ])
    
    message = models.TextField()
    sent_via_telegram = models.BooleanField(default=False)
    sent_via_email = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.notification_type} - Payment {self.payment.id}"
