from django.contrib import admin
from .models import DVApplication, DVSpouse, DVChild, ApplicationStatus


class DVSpouseInline(admin.StackedInline):
    model = DVSpouse
    can_delete = True
    verbose_name_plural = 'Spouse Information'
    extra = 0


class DVChildInline(admin.TabularInline):
    model = DVChild
    can_delete = True
    verbose_name_plural = 'Children Information'
    extra = 0


class ApplicationStatusInline(admin.TabularInline):
    model = ApplicationStatus
    can_delete = True
    verbose_name_plural = 'Status Updates'
    extra = 0


@admin.register(DVApplication)
class DVApplicationAdmin(admin.ModelAdmin):
    list_display = ('dv_id', 'first_name', 'last_name', 'status', 'created_at', 'payment_verified')
    list_filter = ('status', 'payment_verified', 'created_at', 'photo_validation_passed')
    search_fields = ('dv_id', 'first_name', 'last_name', 'email', 'phone_number')
    readonly_fields = ('dv_id', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    inlines = [DVSpouseInline, DVChildInline, ApplicationStatusInline]
    fieldsets = (
        ('Application Information', {
            'fields': ('dv_id', 'status', 'created_at', 'updated_at')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'middle_name', 'last_name', 'gender', 'date_of_birth',
                      'city_of_birth', 'country_of_birth', 'country_of_citizenship')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone_number', 'telegram_username')
        }),
        ('Current Address', {
            'fields': ('current_address', 'city', 'state_province', 'postal_code')
        }),
        ('Education and Work', {
            'fields': ('education_level', 'occupation', 'marital_status')
        }),
        ('Documents', {
            'fields': ('photo', 'payment_proof', 'payment_verified')
        }),
        ('AI Validation', {
            'fields': ('photo_validation_passed', 'photo_validation_message', 
                      'data_validation_passed', 'data_validation_message')
        }),
    )
    actions = ['mark_payment_verified', 'mark_photo_validated', 'change_status_to_under_review', 
               'change_status_to_approved', 'change_status_to_rejected']
    
    def mark_payment_verified(self, request, queryset):
        queryset.update(payment_verified=True)
        self.message_user(request, f"{queryset.count()} applications marked as payment verified.")
    mark_payment_verified.short_description = "Mark selected applications as payment verified"
    
    def mark_photo_validated(self, request, queryset):
        queryset.update(photo_validation_passed=True)
        self.message_user(request, f"{queryset.count()} applications marked as photo validated.")
    mark_photo_validated.short_description = "Mark selected applications as photo validated"
    
    def change_status_to_under_review(self, request, queryset):
        queryset.update(status='under_review')
        for application in queryset:
            ApplicationStatus.objects.create(
                application=application,
                status='under_review',
                created_by=request.user.username
            )
        self.message_user(request, f"{queryset.count()} applications marked as under review.")
    change_status_to_under_review.short_description = "Change status to Under Review"
    
    def change_status_to_approved(self, request, queryset):
        queryset.update(status='approved')
        for application in queryset:
            ApplicationStatus.objects.create(
                application=application,
                status='approved',
                created_by=request.user.username
            )
        self.message_user(request, f"{queryset.count()} applications marked as approved.")
    change_status_to_approved.short_description = "Change status to Approved"
    
    def change_status_to_rejected(self, request, queryset):
        queryset.update(status='rejected')
        for application in queryset:
            ApplicationStatus.objects.create(
                application=application,
                status='rejected',
                created_by=request.user.username
            )
        self.message_user(request, f"{queryset.count()} applications marked as rejected.")
    change_status_to_rejected.short_description = "Change status to Rejected"


@admin.register(DVSpouse)
class DVSpouseAdmin(admin.ModelAdmin):
    list_display = ('application', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'application__dv_id')


@admin.register(DVChild)
class DVChildAdmin(admin.ModelAdmin):
    list_display = ('application', 'first_name', 'last_name', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'application__dv_id')


@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    list_display = ('application', 'status', 'created_at', 'created_by')
    list_filter = ('status', 'created_at')
    search_fields = ('application__dv_id', 'created_by')
    readonly_fields = ('created_at',)