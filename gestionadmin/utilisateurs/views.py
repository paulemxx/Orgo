from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from django.contrib.auth.models import User, Group
from siteConfig.datamanager import mergeData


# Create your views here.

def logout_views(request: HttpRequest) -> HttpResponse:
    return redirect('start:index')


def ajoutadmin(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']

        if password == password1:
            if User.objects.filter(username=username).exists():
                print("Username pris")
            elif User.objects.filter(email=email).exists():
                print("Email pris")

            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print("Utilisateur crée")
                group = Group.objects.get(name='Administrateurs')
                user.groups.add(group)
                return redirect('gestionadmin:index')
    else:
        data = {

            'Admins': User.objects,

        }
        return render(request, 'pages/administration/users/ajoutadmin.html', mergeData(request, data))


def ajoutuser(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']

        if password == password1:
            if User.objects.filter(username=username).exists():
                print("Username pris")
            elif User.objects.filter(email=email).exists():
                print("Email pris")

            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print("Utilisateur crée")
                group = Group.objects.get(name='Utilisateurs')
                user.groups.add(group)
                return redirect('gestionadmin:index')
    else:

        data = {
            'g1': Group.objects.get(name="Utilisateurs").user_set.all(),
            'Users': User.objects,

        }
        return render(request, 'pages/administration/users/ajoutuser.html', mergeData(request, data))


def listeadmin(request: HttpRequest) -> HttpResponse:
    data = {
        'g1': Group.objects.get(name="Administrateurs").user_set.all(),
        'Users': User.objects.filter(groups__name='Administrateurs'),
        # 'admins': auth_models.User.objects.filter(statut=True).order_by('date_add'),

    }
    return render(request, 'pages/administration/users/listeadmin.html', mergeData(request, data))


def listeuser(request: HttpRequest) -> HttpResponse:
    data = {
        'g1': Group.objects.get(name="Utilisateurs").user_set.all(),
        'Users': User.objects.filter(groups__name='Utilisateurs'),

        # 'admins': auth_models.User.objects.filter(statut=True).order_by('date_add'),

    }
    return render(request, 'pages/administration/users/listeuser.html', mergeData(request, data))


def profile(request: HttpRequest) -> HttpResponse:
    data = {
        'g1': Group.objects.get(name="Utilisateurs").user_set.all(),
        'Users': User.objects.filter(groups__name='Utilisateurs'),

        # 'admins': auth_models.User.objects.filter(statut=True).order_by('date_add'),

    }
    return render(request, 'pages/administration/users/page_user_profile.html', mergeData(request, data))
