from django.db import models
import random
import string


def generate_dv_id():
    """Generate a unique DV ID starting with DV2027-"""
    random_part = ''.join(random.choices(string.digits + string.ascii_uppercase, k=11))
    return f"DV2027-{random_part}"


class DVApplication(models.Model):
    """Main DV application model"""
    
    # Application ID and status
    dv_id = models.CharField(max_length=20, default=generate_dv_id, unique=True, editable=False)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('incomplete', 'Incomplete')
    ], default='pending')
    
    # Personal Information
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ])
    date_of_birth = models.DateField()
    city_of_birth = models.CharField(max_length=100)
    country_of_birth = models.CharField(max_length=100)
    country_of_citizenship = models.CharField(max_length=100)
    
    # Contact Information
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    telegram_username = models.CharField(max_length=100, blank=True, null=True)
    telegram_chat_id = models.CharField(max_length=100, blank=True, null=True)
    
    # Current Address
    current_address = models.TextField()
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    
    # Education and Work
    education_level = models.CharField(max_length=50, choices=[
        ('primary', 'Primary School Only'),
        ('secondary', 'High School, No Degree'),
        ('vocational', 'Vocational School'),
        ('university', 'University Degree'),
        ('graduate', 'Graduate Degree'),
        ('doctorate', 'Doctorate Degree'),
    ])
    occupation = models.CharField(max_length=100)
    
    # Marital Status
    marital_status = models.CharField(max_length=20, choices=[
        ('single', 'Single, Never Married'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
        ('separated', 'Legally Separated'),
    ])
    
    # Photo and Payment
    photo = models.ImageField(upload_to='applicant_photos/%Y/%m/')
    payment_proof = models.ImageField(upload_to='payment_proofs/%Y/%m/')
    payment_verified = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # AI Validation
    photo_validation_passed = models.BooleanField(default=False)
    photo_validation_message = models.TextField(blank=True, null=True)
    data_validation_passed = models.BooleanField(default=False)
    data_validation_message = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.dv_id})"


class DVSpouse(models.Model):
    """Spouse information for married applicants"""
    
    application = models.OneToOneField(DVApplication, on_delete=models.CASCADE, related_name='spouse')
    
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ])
    date_of_birth = models.DateField()
    city_of_birth = models.CharField(max_length=100)
    country_of_birth = models.CharField(max_length=100)
    country_of_citizenship = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='spouse_photos/%Y/%m/')
    
    def __str__(self):
        return f"Spouse of {self.application.dv_id}: {self.first_name} {self.last_name}"


class DVChild(models.Model):
    """Child information for applicants with children"""
    
    application = models.ForeignKey(DVApplication, on_delete=models.CASCADE, related_name='children')
    
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ])
    date_of_birth = models.DateField()
    city_of_birth = models.CharField(max_length=100)
    country_of_birth = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='child_photos/%Y/%m/', blank=True, null=True)
    
    def __str__(self):
        return f"Child of {self.application.dv_id}: {self.first_name} {self.last_name}"


class ApplicationStatus(models.Model):
    """Status updates for an application"""
    
    application = models.ForeignKey(DVApplication, on_delete=models.CASCADE, related_name='status_updates')
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('incomplete', 'Incomplete')
    ])
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Application Statuses"
    
    def __str__(self):
        return f"{self.application.dv_id} - {self.status} ({self.created_at.strftime('%Y-%m-%d')})"