"""
URL configuration for bookstore project.

All API endpoints are versioned under /api/v1/.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),

    # API v1 — app-level URL confs will be included here as apps are created
    # e.g.:
    #   path("api/v1/auth/", include("apps.accounts.urls")),
    #   path("api/v1/catalog/", include("apps.catalog.urls")),
    #   path("api/v1/orders/", include("apps.orders.urls")),
    #   path("api/v1/payments/", include("apps.payments.urls")),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
