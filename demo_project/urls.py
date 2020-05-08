from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/', include('sendemail.urls')),
    path('posts/', include('posts.urls')),
    path('', include('pages.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)