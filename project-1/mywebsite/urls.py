from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('sosmed.urls', 'sosmed'), namespace='sosmed')),
    # path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
