from . import views
from django.urls import path

urlpatterns = [
    path('scanhosts/', views.scan_hosts),
    path('gethosts/', views.get_hosts),
]
