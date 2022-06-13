from django.shortcuts import redirect, render
from urllib import request
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User

# Create your views here.
def Login(request):
    if 'login' in request.POST:
        username = request.POST['log_username']
        password = request.POST['log_password']
        try:
            a = login(request, authenticate(username=username, password=password))
            print(a)
            return redirect('prog_auth:home')
        except:
            messages.error(request, 'Usuario o contraseña incorrectos')
    elif 'register' in request.POST:
        try:
            user = User()
            user.username = request.POST['reg_username']
            user.email = request.POST['reg_email']
            user.first_name = request.POST['reg_first_name']
            user.last_name = request.POST['reg_last_name']
            user.set_password(request.POST['reg_password'])
            user.save()
            print('Usuario registrado')
            messages.success(request, 'Usuario registrado')
        except:
            messages.error(request, 'Error al registrar usuario')
    return render(request, 'login.html')

def Home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})

def Logout(request):
    logout(request)
    return redirect('prog_auth:login')