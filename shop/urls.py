from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop, name='index'),
    path('shop/<slug:titre_slug>', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('cart/<slug:titre_slug>', views.update_cart, name='update_cart'),
]