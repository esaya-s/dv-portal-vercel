"""
URL configuration for dv_portal project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('applications/', include('applications.urls')),
    
    # Legal pages
    path('privacy-policy/', TemplateView.as_view(template_name='legal/privacy_policy.html'), name='privacy_policy'),
    path('terms-of-service/', TemplateView.as_view(template_name='legal/terms_of_service.html'), name='terms_of_service'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin site customization
admin.site.site_header = "DV Portal Administration"
admin.site.site_title = "DV Portal Admin"
admin.site.index_title = "Welcome to DV Portal Administration"
