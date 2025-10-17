from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, FormView
from django.contrib import messages
from django.urls import reverse_lazy
from django.forms import modelformset_factory, Form
from django.http import HttpResponseRedirect
from django import forms
from .models import DVApplication, DVSpouse, DVChild
from .forms import DVApplicationForm, DVSpouseForm, DVChildForm, DVChildFormSet


class ApplicationCreateView(CreateView):
    """Create a new DV application"""
    model = DVApplication
    form_class = DVApplicationForm
    template_name = 'applications/create.html'
    success_url = reverse_lazy('applications:success')
    
    def form_valid(self, form):
        # Save the application
        application = form.save()
        
        # Process notification logic - send Telegram notifications
        try:
            from notifications.telegram_bot import send_application_notification_to_admin, send_confirmation_to_applicant
            
            # Send notification to admin
            admin_notified = send_application_notification_to_admin(application)
            
            # Send confirmation to applicant if they provided a Telegram username
            if application.telegram_username:
                applicant_notified = send_confirmation_to_applicant(application)
                
                if isinstance(applicant_notified, str) and applicant_notified.startswith('https://t.me/'):
                    # Store the bot link in session to show on success page
                    self.request.session['telegram_bot_link'] = applicant_notified
        except Exception as e:
            # Log the error but don't stop the form submission
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error sending Telegram notifications: {e}")
        
        messages.success(self.request, 'Your application has been submitted successfully!')
        
        # Store application ID in session for confirmation page
        self.request.session['application_id'] = application.dv_id
        
        return super().form_valid(form)


class ApplicationSuccessView(DetailView):
    """Success page after application submission"""
    model = DVApplication
    template_name = 'applications/success.html'
    context_object_name = 'application'
    
    def get_object(self):
        # Get application ID from session
        application_id = self.request.session.get('application_id')
        if not application_id:
            return None
        
        return get_object_or_404(DVApplication, dv_id=application_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['telegram_bot_username'] = '@anvilutech'
        
        # Add Telegram bot link if available
        if 'telegram_bot_link' in self.request.session:
            context['telegram_bot_link'] = self.request.session['telegram_bot_link']
            # Remove from session after use
            del self.request.session['telegram_bot_link']
        
        return context


class ApplicationStatusView(FormView):
    """Check application status by ID"""
    template_name = 'applications/status.html'
    form_class = type('ApplicationStatusForm', (forms.Form,), {
        'application_id': forms.CharField(max_length=11, 
                                         label='Application ID', 
                                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    })
    success_url = reverse_lazy('applications:status_result')
    
    def form_valid(self, form):
        # Get the ID part entered by the user (without the prefix)
        id_part = form.cleaned_data['application_id']
        
        # Add the prefix if not already present
        if not id_part.startswith('DV2027-'):
            application_id = f"DV2027-{id_part}"
        else:
            application_id = id_part
            
        self.request.session['check_application_id'] = application_id
        return super().form_valid(form)


class ApplicationStatusResultView(DetailView):
    """Display application status result"""
    model = DVApplication
    template_name = 'applications/status_result.html'
    context_object_name = 'application'
    
    def get(self, request, *args, **kwargs):
        # Check if we have an application ID in the session
        self.application_id = self.request.session.get('check_application_id')
        if not self.application_id:
            # If no ID in session, redirect back to the status check form
            messages.error(request, "No application ID provided. Please enter your application ID.")
            return redirect('applications:status')
        
        return super().get(request, *args, **kwargs)
    
    def get_object(self):
        try:
            return get_object_or_404(DVApplication, dv_id=self.application_id)
        except:
            # If application not found, add error message
            messages.error(self.request, f"No application found with ID: {self.application_id}")
            # Return None, the template will handle this case
            return None


def application_form_view(request):
    """Function-based view for application with spouse and children formsets"""
    
    # Create formset for children
    ChildFormSet = modelformset_factory(
        DVChild, 
        form=DVChildForm,
        formset=DVChildFormSet,
        extra=10,  # Create 10 empty forms initially
        max_num=10
    )
    
    if request.method == 'POST':
        # Process the forms
        application_form = DVApplicationForm(request.POST, request.FILES)
        spouse_form = DVSpouseForm(request.POST, request.FILES)
        child_formset = ChildFormSet(request.POST, request.FILES, prefix='children')
        
        # Check if user wants to include spouse and children
        include_spouse = request.POST.get('include_spouse') == 'on'
        include_children = request.POST.get('include_children') == 'on'
        
        # Validate forms
        forms_valid = application_form.is_valid()
        
        # Spouse form is optional - only validate if user wants to include spouse
        if include_spouse:
            forms_valid = forms_valid and spouse_form.is_valid()
        
        # Children formset is optional - only validate if user wants to include children
        if include_children:
            forms_valid = forms_valid and child_formset.is_valid()
        
        if forms_valid:
            # Save application
            application = application_form.save()
            
            # Save spouse information only if user wants to include spouse
            if include_spouse and spouse_form.is_valid():
                spouse = spouse_form.save(commit=False)
                spouse.application = application
                spouse.save()
            
            # Save children only if user wants to include children
            if include_children and child_formset.is_valid():
                children = child_formset.save(commit=False)
                for child in children:
                    # Only save if child has at least a first name
                    if child.first_name:
                        child.application = application
                        child.save()
            
            # Process notification logic - send Telegram notifications
            try:
                from notifications.telegram_bot import send_application_notification_to_admin, send_confirmation_to_applicant
                
                # Send notification to admin
                admin_notified = send_application_notification_to_admin(application)
                
                # Send confirmation to applicant if they provided a Telegram username
                if application.telegram_username:
                    applicant_notified = send_confirmation_to_applicant(application)
                    
                    if isinstance(applicant_notified, str) and applicant_notified.startswith('https://t.me/'):
                        # Store the bot link in session to show on success page
                        request.session['telegram_bot_link'] = applicant_notified
            except Exception as e:
                # Log the error but don't stop the form submission
                import logging
                logger = logging.getLogger(__name__)
                logger.error(f"Error sending Telegram notifications: {e}")
            
            # Store application ID in session
            request.session['application_id'] = application.dv_id
            
            # Redirect to success page
            return redirect('applications:success')
    else:
        # Initialize forms
        application_form = DVApplicationForm()
        spouse_form = DVSpouseForm()
        child_formset = ChildFormSet(queryset=DVChild.objects.none(), prefix='children')
    
    context = {
        'application_form': application_form,
        'spouse_form': spouse_form,
        'child_formset': child_formset,
        'include_spouse': request.POST.get('include_spouse') == 'on' if request.method == 'POST' else False,
        'include_children': request.POST.get('include_children') == 'on' if request.method == 'POST' else False,
    }
    
    return render(request, 'applications/create_full.html', context)