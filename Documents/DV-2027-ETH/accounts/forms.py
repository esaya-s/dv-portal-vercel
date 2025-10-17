from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Field, HTML


class CustomUserCreationForm(UserCreationForm):
    """Custom user registration form with additional fields"""
    
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h3 class="mb-4">Create Your Account</h3>'),
            Row(
                Column('first_name', css_class='form-group col-md-6'),
                Column('last_name', css_class='form-group col-md-6'),
            ),
            Row(
                Column('username', css_class='form-group col-md-6'),
                Column('email', css_class='form-group col-md-6'),
            ),
            Field('phone_number', css_class='form-group'),
            Row(
                Column('password1', css_class='form-group col-md-6'),
                Column('password2', css_class='form-group col-md-6'),
            ),
            HTML('''
                <div class="form-check mb-3">
                    <input class="form-check-input" type="checkbox" id="terms" name="terms" required>
                    <label class="form-check-label" for="terms">
                        I agree to the <a href="/terms-of-service/" target="_blank">Terms of Service</a> 
                        and <a href="/privacy-policy/" target="_blank">Privacy Policy</a>
                    </label>
                </div>
            '''),
            Submit('submit', 'Create Account', css_class='btn btn-primary btn-lg w-100')
        )
        
        # Add Bootstrap classes and placeholders
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'First Name'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'your.email@example.com'
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '+251911234567'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    """Custom login form with better styling"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h3 class="mb-4">Log In to Your Account</h3>'),
            Field('username', css_class='form-control mb-3', placeholder='Username or Email'),
            Field('password', css_class='form-control mb-3', placeholder='Password'),
            HTML('''
                <div class="form-check mb-3">
                    <input class="form-check-input" type="checkbox" id="remember" name="remember">
                    <label class="form-check-label" for="remember">
                        Remember me
                    </label>
                </div>
            '''),
            Submit('submit', 'Log In', css_class='btn btn-primary btn-lg w-100'),
            HTML('''
                <div class="text-center mt-3">
                    <a href="#" class="text-decoration-none">Forgot password?</a>
                </div>
            ''')
        )
        
        # Add Bootstrap classes
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username or Email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })


class UserProfileForm(forms.Form):
    """User profile form with additional fields"""
    
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=True
    )
    country_of_birth = forms.CharField(max_length=100, required=True)
    country_of_citizenship = forms.CharField(max_length=100, required=True)
    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female')],
        widget=forms.RadioSelect,
        required=True
    )
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)
    city = forms.CharField(max_length=100, required=True)
    postal_code = forms.CharField(max_length=20, required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML('<h3 class="mb-4">Complete Your Profile</h3>'),
            HTML('<h5 class="text-primary">Personal Information</h5>'),
            Row(
                Column('date_of_birth', css_class='form-group col-md-6'),
                Column('gender', css_class='form-group col-md-6'),
            ),
            Row(
                Column('country_of_birth', css_class='form-group col-md-6'),
                Column('country_of_citizenship', css_class='form-group col-md-6'),
            ),
            HTML('<h5 class="text-primary mt-4">Address Information</h5>'),
            Field('address', css_class='form-group'),
            Row(
                Column('city', css_class='form-group col-md-6'),
                Column('postal_code', css_class='form-group col-md-6'),
            ),
            Submit('submit', 'Update Profile', css_class='btn btn-primary btn-lg')
        )
        
        # Add Bootstrap classes
        for field_name, field in self.fields.items():
            if field_name != 'gender':
                field.widget.attrs.update({'class': 'form-control'})
        
        # Add specific placeholders
        self.fields['country_of_birth'].widget.attrs['placeholder'] = 'Country of Birth'
        self.fields['country_of_citizenship'].widget.attrs['placeholder'] = 'Country of Citizenship'
        self.fields['address'].widget.attrs['placeholder'] = 'Your current address'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['postal_code'].widget.attrs['placeholder'] = 'Postal/ZIP Code (optional)'