from django.urls import path, re_path
from .views import (
    sosmedListView,
    sosmedDeleteView,
    sosmedFormView,
)

urlpatterns = [
    re_path('delete/(?P<delete_id>[0-9]+)$', sosmedDeleteView.as_view(), name='delete'),
    re_path('update/(?P<update_id>[0-9]+)$', sosmedFormView.as_view(mode='update'), name='update'),
    path('create/', sosmedFormView.as_view(), name='create'),
    path('', sosmedListView.as_view(), name='list'),
]