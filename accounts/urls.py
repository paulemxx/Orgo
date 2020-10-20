from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'accounts'

urlpatterns = [

    path('register', views.register, name='register'),
    path('', views.logins, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logouts', views.logouts, name='logouts'),


    ]