from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.blog, name='index'),
    path('blog/<slug:titre_slug>', views.single_blog, name='single_blog'),

    ]