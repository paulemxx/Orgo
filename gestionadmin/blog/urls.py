from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [

    path('ajoutarticle', views.ajoutarticle, name='ajoutarticle'),
    path('ajoutcategorie', views.ajoutcategorie, name='ajoutcategorie'),
    path('ajouttag', views.ajouttag, name='ajouttag'),
    path('listearticle', views.listearticle, name='listearticle'),
    path('listecategorie', views.listecategorie, name='listecategorie'),
    path('listetag', views.listetag, name='listetag'),

]