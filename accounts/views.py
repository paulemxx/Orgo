from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from . import models
from siteConfig.datamanager import mergeData


# Create your views here.

def register(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/accounts/register.html', mergeData(request, data))


def login(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/accounts/login.html', mergeData(request, data))
