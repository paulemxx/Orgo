from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from django.contrib.auth.models import User
from siteConfig.datamanager import mergeData

# Create your views here.


def ajoutadmin(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/administration/users/ajoutadmin.html', mergeData(request, data))


def ajoutuser(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/administration/users/ajoutuser.html', mergeData(request, data))

def listeadmin(request: HttpRequest) -> HttpResponse:
    data = {
        #'admins': auth_models.User.objects.filter(statut=True).order_by('date_add'),

    }
    return render(request, 'pages/administration/users/listeadmin.html', mergeData(request, data))


def listeuser(request: HttpRequest) -> HttpResponse:
    data = {

        # 'admins': auth_models.User.objects.filter(statut=True).order_by('date_add'),

    }
    return render(request, 'pages/administration/users/listeuser.html', mergeData(request, data))
