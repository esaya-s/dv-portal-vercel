from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
from .models import UserProfile


class RegisterView(CreateView):
    """User registration view"""
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        # Save the user
        user = form.save()
        
        # Create profile entry with phone number
        UserProfile.objects.create(
            user=user,
            phone_number=form.cleaned_data['phone_number']
        )
        
        messages.success(
            self.request,
            'Registration successful! Please log in to continue.'
        )
        return super().form_valid(form)


class CustomLoginView(LoginView):
    """Custom login view with better form"""
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('core:dashboard')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'Welcome back, {form.get_user().first_name}!'
        )
        return super().form_valid(form)


def logout_view(request):
    """Logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('core:home')


class ProfileView(LoginRequiredMixin, TemplateView):
    """User profile view"""
    template_name = 'accounts/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context


class ProfileEditView(LoginRequiredMixin, FormView):
    """Edit user profile"""
    form_class = UserProfileForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')
    
    def get_initial(self):
        # Pre-populate form with existing data
        user = self.request.user
        initial = {}
        # If we had a UserProfile model, we would get data from there
        return initial
    
    def form_valid(self, form):
        user = self.request.user
        # Save profile data
        # In the future, save to UserProfile model
        
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)


class EmailVerifyView(TemplateView):
    """Email verification view"""
    template_name = 'accounts/email_verify.html'
    
    def get(self, request, token, *args, **kwargs):
        # Implement email verification logic
        messages.success(request, 'Email verification feature coming soon!')
        return redirect('accounts:profile')


@login_required
def phone_verify_view(request):
    """Phone verification view"""
    if request.method == 'POST':
        # Implement phone verification logic
        messages.success(request, 'Phone verification feature coming soon!')
        return redirect('accounts:profile')
    
    return render(request, 'accounts/phone_verify.html')