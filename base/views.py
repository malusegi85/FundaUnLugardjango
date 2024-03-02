from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import logout

from usuarios.models import Usuario
from usuarios.forms import UsuarioForm

def inicioAdmin(request):
    titulo="Tablero Principal"
       
    cantidad_usuarios= Usuario.objects.all().count()  
    
    context={
        'titulo':titulo,
        'cantidad_usuarios':cantidad_usuarios,
        
    }
    return render(request,'index-admin.html', context)

def ayuda(request):
    return render(request, "ayuda.html")

def politica(request):
    return render(request, "politica.html")

def logout_user(request):
    logout(request)       
    return redirect('inicio')

