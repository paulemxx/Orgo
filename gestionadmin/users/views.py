from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest

from siteConfig.datamanager import mergeData

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    data = {


    }
    return render(request, 'pages/administration/index.html', mergeData(request, data))
