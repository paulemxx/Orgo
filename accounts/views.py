from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from . import models
from siteConfig.datamanager import mergeData
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.forms import RegisterForm


# Create your views here.

def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:dashboard')
    else:
        form = RegisterForm()

    return render(request, 'pages/accounts/register.html', {'form': form})


def logins(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/accounts/login.html', mergeData(request, data))


def dashboard(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/accounts/dashboard.html', mergeData(request, data))
