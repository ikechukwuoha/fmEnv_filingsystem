from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.admin import user_site

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user_admin/", user_site.urls),
    path("users/", include("users.urls")),
    path("barcodes/", include("bar_codes.urls")),
    path("api/", include("api.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
