from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import loginView, logoutView

urlpatterns = [
    re_path('', include(('store.urls', 'store'), namespace='store')),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)