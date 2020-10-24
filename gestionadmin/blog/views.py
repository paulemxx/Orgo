from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from . import models
from siteConfig.datamanager import mergeData


# Create your views here.

def ajoutarticle(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/administration/blog/ajoutarticle.html', mergeData(request, data))


def ajoutcategorie(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/administration/blog/ajoutcategorie.html', mergeData(request, data))



def ajouttag(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/administration/blog/ajouttag.html', mergeData(request, data))



def listearticle(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/administration/blog/listearticle.html', mergeData(request, data))



def listecategorie(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/administration/blog/listecategorie.html', mergeData(request, data))



def listetag(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/administration/blog/listetag.html', mergeData(request, data))
