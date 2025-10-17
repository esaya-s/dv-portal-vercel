from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Field
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Contact form for user inquiries"""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6'),
                Column('email', css_class='form-group col-md-6'),
            ),
            Row(
                Column('phone', css_class='form-group col-md-6'),
                Column('subject', css_class='form-group col-md-6'),
            ),
            Field('message', css_class='form-group'),
            Submit('submit', 'Send Message', css_class='btn btn-primary btn-lg')
        )
        
        # Add Bootstrap classes and placeholders
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your Full Name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'your.email@example.com'
        })
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '+251911234567'
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Subject of your inquiry'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Please provide details about your question or concern...'
        })
