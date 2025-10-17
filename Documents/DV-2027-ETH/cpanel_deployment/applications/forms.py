from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Field, HTML, Div, Fieldset
from .models import DVApplication, DVSpouse, DVChild


class DVApplicationForm(forms.ModelForm):
    """Main application form for DV program"""
    
    class Meta:
        model = DVApplication
        exclude = ['dv_id', 'status', 'payment_verified', 'photo_validation_passed', 
                  'photo_validation_message', 'data_validation_passed', 
                  'data_validation_message', 'created_at', 'updated_at']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_method = 'post'
        self.helper.form_class = 'dv-form'
        self.helper.form_id = 'dv-application-form'
        self.helper.form_enctype = 'multipart/form-data'
        
        self.helper.layout = Layout(
            HTML('<div class="usa-alert usa-alert--info mb-4">'),
            HTML('<div class="usa-alert__body">'),
            HTML('<h3 class="usa-alert__heading">Important Information</h3>'),
            HTML('<p class="usa-alert__text">Please complete all fields marked with * accurately. Incorrect information may result in disqualification.</p>'),
            HTML('</div></div>'),
            
            Fieldset(
                'Personal Information',
                Row(
                    Column('first_name', css_class='form-group col-md-4'),
                    Column('middle_name', css_class='form-group col-md-4'),
                    Column('last_name', css_class='form-group col-md-4'),
                ),
                Row(
                    Column('gender', css_class='form-group col-md-4'),
                    Column('date_of_birth', css_class='form-group col-md-4'),
                    Column('marital_status', css_class='form-group col-md-4'),
                ),
                Row(
                    Column('city_of_birth', css_class='form-group col-md-4'),
                    Column('country_of_birth', css_class='form-group col-md-4'),
                    Column('country_of_citizenship', css_class='form-group col-md-4'),
                ),
                css_class='mb-4 p-3 border rounded'
            ),
            
            Fieldset(
                'Contact Information',
                Row(
                    Column('email', css_class='form-group col-md-6'),
                    Column('phone_number', css_class='form-group col-md-6'),
                ),
                Field('telegram_username', css_class='form-group'),
                css_class='mb-4 p-3 border rounded'
            ),
            
            Fieldset(
                'Current Address',
                Field('current_address', css_class='form-group'),
                Row(
                    Column('city', css_class='form-group col-md-4'),
                    Column('state_province', css_class='form-group col-md-4'),
                    Column('postal_code', css_class='form-group col-md-4'),
                ),
                css_class='mb-4 p-3 border rounded'
            ),
            
            Fieldset(
                'Education and Work',
                Row(
                    Column('education_level', css_class='form-group col-md-6'),
                    Column('occupation', css_class='form-group col-md-6'),
                ),
                css_class='mb-4 p-3 border rounded'
            ),
            
            Fieldset(
                'Required Documents',
                HTML('<div class="alert alert-warning mb-3">'),
                HTML('<p><strong>Photo Requirements:</strong></p>'),
                HTML('<ul>'),
                HTML('<li>Recent photograph taken within the last 6 months</li>'),
                HTML('<li>Plain white or off-white background</li>'),
                HTML('<li>Full face view directly facing the camera</li>'),
                HTML('<li>Neutral facial expression or natural smile</li>'),
                HTML('<li>Both eyes open and clearly visible</li>'),
                HTML('<li>No hats, head coverings, or glasses (unless for religious or medical reasons)</li>'),
                HTML('</ul>'),
                HTML('</div>'),
                Field('photo', css_class='form-group'),
                
                HTML('<div class="alert alert-warning mb-3">'),
                HTML('<p><strong>Payment Requirements:</strong></p>'),
                HTML('<ul>'),
                HTML('<li>Payment of 800 Birr must be made to <strong>Commercial Bank of Ethiopia (CBE) only</strong></li>'),
                HTML('<li>Account Number: <strong>1000674773319</strong></li>'),
                HTML('<li>Account Name: <strong>Mr. Esayas Desta</strong></li>'),
                HTML('<li>Upload a clear photo or scan of your payment receipt</li>'),
                HTML('<li>Ensure the receipt shows the payment date, amount, and your name</li>'),
                HTML('</ul>'),
                HTML('</div>'),
                Field('payment_proof', css_class='form-group'),
                css_class='mb-4 p-3 border rounded'
            ),
            
            HTML('<div class="form-check mb-4">'),
            HTML('<input class="form-check-input" type="checkbox" id="terms" name="terms" required>'),
            HTML('<label class="form-check-label" for="terms">'),
            HTML('I confirm that all information provided is accurate and complete. I understand that any false information may result in disqualification. I agree to the <a href="/terms-of-service/" target="_blank">Terms of Service</a> and <a href="/privacy-policy/" target="_blank">Privacy Policy</a>.'),
            HTML('</label>'),
            HTML('</div>'),
            
            Div(
                Submit('submit', 'Submit Application', css_class='btn btn-primary btn-lg'),
                css_class='text-center'
            )
        )
        
        # Add Bootstrap classes
        for field_name, field in self.fields.items():
            if field_name not in ['photo', 'payment_proof']:
                field.widget.attrs['class'] = 'form-control'


class DVSpouseForm(forms.ModelForm):
    """Form for spouse information"""
    
    class Meta:
        model = DVSpouse
        exclude = ['application']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        
        self.helper.layout = Layout(
            Fieldset(
                'Spouse Information',
                Row(
                    Column('first_name', css_class='form-group col-md-4'),
                    Column('middle_name', css_class='form-group col-md-4'),
                    Column('last_name', css_class='form-group col-md-4'),
                ),
                Row(
                    Column('gender', css_class='form-group col-md-4'),
                    Column('date_of_birth', css_class='form-group col-md-4'),
                ),
                Row(
                    Column('city_of_birth', css_class='form-group col-md-4'),
                    Column('country_of_birth', css_class='form-group col-md-4'),
                    Column('country_of_citizenship', css_class='form-group col-md-4'),
                ),
                HTML('<div class="alert alert-warning mb-3">'),
                HTML('<p><strong>Spouse Photo Requirements:</strong> Same requirements as primary applicant photo</p>'),
                HTML('</div>'),
                Field('photo', css_class='form-group'),
                css_class='mb-4 p-3 border rounded'
            )
        )
        
        # Add Bootstrap classes
        for field_name, field in self.fields.items():
            if field_name != 'photo':
                field.widget.attrs['class'] = 'form-control'


class DVChildForm(forms.ModelForm):
    """Form for child information"""
    
    class Meta:
        model = DVChild
        exclude = ['application']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        
        self.helper.layout = Layout(
            Fieldset(
                'Child Information',
                Row(
                    Column('first_name', css_class='form-group col-md-4'),
                    Column('middle_name', css_class='form-group col-md-4'),
                    Column('last_name', css_class='form-group col-md-4'),
                ),
                Row(
                    Column('gender', css_class='form-group col-md-4'),
                    Column('date_of_birth', css_class='form-group col-md-4'),
                ),
                Row(
                    Column('city_of_birth', css_class='form-group col-md-4'),
                    Column('country_of_birth', css_class='form-group col-md-4'),
                ),
                HTML('<div class="alert alert-warning mb-3">'),
                HTML('<p><strong>Child Photo Requirements:</strong> Same requirements as primary applicant photo (optional for children under 14)</p>'),
                HTML('</div>'),
                Field('photo', css_class='form-group'),
                css_class='mb-4 p-3 border rounded'
            )
        )
        
        # Add Bootstrap classes
        for field_name, field in self.fields.items():
            if field_name != 'photo':
                field.widget.attrs['class'] = 'form-control'


class DVChildFormSet(forms.BaseModelFormSet):
    """Formset for multiple children"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = DVChild.objects.none()


DVChildFormSetHelper = FormHelper()
DVChildFormSetHelper.form_tag = False
DVChildFormSetHelper.template = 'bootstrap5/table_inline_formset.html'
DVChildFormSetHelper.add_input(Submit("submit", "Save Children", css_class='btn btn-primary'))
