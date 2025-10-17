from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Extended user profile for DV application specific information"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dv_profile')
    
    # Additional fields
    phone_number = models.CharField(max_length=20, help_text="Enter your phone number with country code")
    telegram_username = models.CharField(max_length=100, blank=True, null=True, help_text="Optional: Your Telegram username (without @)")
    date_of_birth = models.DateField(null=True, blank=True)
    country_of_birth = models.CharField(max_length=100, blank=True, null=True)
    country_of_citizenship = models.CharField(max_length=100, blank=True, null=True)
    
    # Address information
    current_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    
    # Additional personal information
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ], blank=True, null=True)
    
    # Education and work
    education_level = models.CharField(max_length=50, choices=[
        ('primary', 'Primary School Only'),
        ('secondary', 'High School, No Degree'),
        ('vocational', 'Vocational School'),
        ('university', 'University Degree'),
        ('graduate', 'Graduate Degree'),
        ('doctorate', 'Doctorate Degree'),
    ], blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    work_experience_years = models.IntegerField(default=0)
    
    # Marital status
    marital_status = models.CharField(max_length=20, choices=[
        ('single', 'Single, Never Married'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
        ('separated', 'Legally Separated'),
    ], blank=True, null=True)
    
    # Emergency contact
    emergency_contact_name = models.CharField(max_length=200, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=100, blank=True, null=True)
    
    # Profile completion tracking
    profile_completed = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()}'s Profile"
    
    def has_completed_profile(self):
        """Check if user has completed their basic profile"""
        required_fields = [
            self.user.first_name, self.user.last_name, self.user.email,
            self.phone_number, self.date_of_birth,
            self.country_of_birth, self.country_of_citizenship
        ]
        return all(field for field in required_fields)