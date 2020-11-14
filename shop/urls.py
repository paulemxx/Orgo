from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop, name='index'),
    path('shop/<slug:titre_slug>', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path(r'^add/(?P<product_id>\d+)/$',views.cart_add,name='cart_add'),
    path(r'^remove/(?P<product_id>\d+)/$',views.cart_remove,name='cart_remove'),
]