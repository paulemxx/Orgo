from django.urls import path
from gestionadmin.blogs import views

app_name = 'blogs'

urlpatterns = [

    path('ajoutarticle', views.ajoutarticle, name='ajoutarticle'),
    path('ajoutcategorie', views.ajoutcategorie, name='ajoutcategorie'),
    path('ajouttag', views.ajouttag, name='ajouttag'),
    path('listearticle', views.listearticle, name='listearticle'),
    path('listecategorie', views.listecategorie, name='listecategorie'),
    path('listetag', views.listetag, name='listetag'),

]