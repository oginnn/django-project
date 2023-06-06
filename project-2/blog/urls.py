from django.contrib import admin
from django.urls import path, re_path, include
from .views import BlogHomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('artikel/', include(('artikel.urls', 'artikel'), namespace='artikel')),
    re_path('', BlogHomeView.as_view(), name='home'),
]