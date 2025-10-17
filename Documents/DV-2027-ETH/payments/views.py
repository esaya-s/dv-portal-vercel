from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from .models import Payment, PaymentInstruction


class PaymentListView(LoginRequiredMixin, ListView):
    """List user's payments"""
    model = Payment
    template_name = 'payments/list.html'
    context_object_name = 'payments'
    
    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user).order_by('-created_at')


class PaymentDetailView(LoginRequiredMixin, DetailView):
    """Payment detail view"""
    model = Payment
    template_name = 'payments/detail.html'
    pk_url_kwarg = 'payment_id'
    
    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class PaymentInstructionsView(TemplateView):
    """Payment instructions"""
    template_name = 'payments/instructions.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instructions'] = PaymentInstruction.objects.filter(is_active=True)
        return context


class PaymentUploadView(LoginRequiredMixin, TemplateView):
    """Upload payment proof"""
    template_name = 'payments/upload.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['confirmation_number'] = kwargs.get('confirmation_number')
        context['message'] = "Payment upload form coming soon!"
        return context


class PaymentStatusView(LoginRequiredMixin, TemplateView):
    """Payment status view"""
    template_name = 'payments/status.html'


# Admin views (placeholder)
class AdminPendingPaymentsView(LoginRequiredMixin, TemplateView):
    template_name = 'payments/admin_pending.html'


class AdminPaymentApproveView(LoginRequiredMixin, TemplateView):
    template_name = 'payments/admin_approve.html'


class AdminPaymentRejectView(LoginRequiredMixin, TemplateView):
    template_name = 'payments/admin_reject.html'
