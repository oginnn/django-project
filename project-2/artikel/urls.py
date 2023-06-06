from django.urls import path, re_path
from .views import (
                    ArtikelListView,
                    ArtikelDetailView,
                    ArtikelKategoriListView,
                    ArtikelCreateView,
                    ArtikelManageView,
                    ArtikelDeleteView,
                    ArtikelUpdateView
                    )

urlpatterns = [
    re_path('manage/update/(?P<pk>\d+)', ArtikelUpdateView.as_view(), name='update'),
    re_path('manage/delete/(?P<pk>\d+)', ArtikelDeleteView.as_view(), name='delete'),
    re_path('manage/', ArtikelManageView.as_view(), name='manage'),
    re_path('tambah/', ArtikelCreateView.as_view(), name='create'),
    re_path('kategori/(?P<kategori>[\w]+)/(?P<page>\d+)', ArtikelKategoriListView.as_view(), name='kategori'),
    re_path('detail/(?P<slug>[\w-]+)', ArtikelDetailView.as_view(), name='detail'),
    re_path('(?P<page>\d+)', ArtikelListView.as_view(), name='list'),
]