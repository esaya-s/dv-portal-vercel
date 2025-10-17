from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_phone_number')
    list_select_related = ('dv_profile',)
    
    def get_phone_number(self, instance):
        try:
            return instance.dv_profile.phone_number
        except UserProfile.DoesNotExist:
            return '-'
    
    get_phone_number.short_description = 'Phone Number'


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)