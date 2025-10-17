from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.PaymentListView.as_view(), name='list'),
    path('instructions/', views.PaymentInstructionsView.as_view(), name='instructions'),
    path('upload/<str:confirmation_number>/', views.PaymentUploadView.as_view(), name='upload'),
    path('<int:payment_id>/', views.PaymentDetailView.as_view(), name='detail'),
    path('<int:payment_id>/status/', views.PaymentStatusView.as_view(), name='status'),
    
    # Admin views
    path('admin/pending/', views.AdminPendingPaymentsView.as_view(), name='admin_pending'),
    path('admin/<int:payment_id>/approve/', views.AdminPaymentApproveView.as_view(), name='admin_approve'),
    path('admin/<int:payment_id>/reject/', views.AdminPaymentRejectView.as_view(), name='admin_reject'),
]
