
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('daenamuapp/', include('daenamuapp.urls')), # http://localhost:8000/blog/
    path('account/', include('account.urls')), # http://localhost:8000/account/
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
