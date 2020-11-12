from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect
from django.http.request import HttpRequest
from . import models
from siteConfig.datamanager import mergeData
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from accounts.forms import RegisterForm
from shop import models

# Create your views here.

def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']

        if password == password1 :
            if User.objects.filter(username=username).exists():
                print("Username pris")
            elif User.objects.filter(email=email).exists():
                print("Email pris")

            else :
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("Utilisateur crée")
    else:

        data = {

        }
        return render(request, 'pages/accounts/register.html', mergeData(request, data))




def logins(request: HttpRequest) -> HttpResponse:
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    g1 = Group.objects.get(name="Utilisateurs").user_set.all()
    if user is not None and user.is_active:
        if user in g1:
            login(request, user)
            return redirect('accounts:dashboard')
        else:
            login(request, user)
            return redirect('gestionadmin:index')


    else:
        data = {

        }
    return render(request, 'pages/accounts/login.html', mergeData(request, data))


def dashboard(request: HttpRequest) -> HttpResponse:
    data = {
        'prod': models.Produit.objects.filter(statut=True).order_by('-date_add')

    }
    return render(request, 'pages/accounts/dashboard.html', mergeData(request, data))


def logouts(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('start:index')
