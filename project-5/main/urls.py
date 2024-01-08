from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
	path('', views.index_view.as_view(), name="home"),
    path('certificate/', views.certificates_view.as_view(), name='certificate'),
    path('reporting/', views.reporting_view.as_view(), name='reports'),
    path('reporting/<slug:slug>', views.reporting_result_view.as_view(), name="reporting"),
]