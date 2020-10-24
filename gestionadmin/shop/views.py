from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest

from siteConfig.datamanager import mergeData

# Create your views here.

def ajoutproduit(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/administration/shop/ajoutproduit.html', mergeData(request, data))


def ajoutcategorie(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/administration/shop/ajoutcategorie.html', mergeData(request, data))



def ajouttag(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/administration/shop/ajouttag.html', mergeData(request, data))



def listeproduit(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/administration/shop/listeproduit.html', mergeData(request, data))



def listecategorie(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/administration/shop/listecategorie.html', mergeData(request, data))



def listetag(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/administration/shop/listetag.html', mergeData(request, data))
