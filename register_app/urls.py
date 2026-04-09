from .views import *
from django.urls import path

urlpatterns = [
    path('', HomePage.as_view(), name='view-home'),
    path('dashboard/', DashboardPage.as_view(), name='home'),
    path('signup/', register, name='register'),
    path('success/', success, name='success'),
    path('export-registers/', export_csv, name='export_registers'),
]