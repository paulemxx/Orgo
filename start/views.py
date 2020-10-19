from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from . import models
from siteConfig.datamanager import mergeData

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/index.html', mergeData(request, data))



def about(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/about.html', mergeData(request, data))



def gallery(request: HttpRequest) -> HttpResponse:

    data = {


    }
    return render(request, 'pages/gallery.html',mergeData(request, data))


def faq(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/faq.html', mergeData(request, data))



def team(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/team.html', mergeData(request, data))



def services(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/services.html', mergeData(request, data))


def contact(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/contact.html', mergeData(request, data))



