from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'start'

urlpatterns = [

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('team', views.team, name='team'),
]