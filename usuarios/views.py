from django.http.response import JsonResponse

from django.shortcuts import render, redirect
from usuarios.forms import UsuarioForm, BeneficiarioForm, AcudienteForm, PadrinoForm, ReferenciaForm
from usuarios.models import Usuario, Beneficiario, Acudiente, Padrino, Referencia

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import make_password

# Usuarios registrados y autenticados por el Administrador con clave y usuario para ingresar al SISTEMA


@login_required(login_url='inicio')
def usuarios(request):
    titulo="Usuarios"
    usuarios= Usuario.objects.all()
    context={
        'titulo':titulo,
        'usuarios':usuarios
    }
    return render(request,'usuarios/usuarios.html',context)

def usuarios_crear(request):
    titulo="Usuario - Registrar" 
    if request.method == "POST":
        form= UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, '¡usuario registrado!')
            if not User.objects.filter(username=request.POST['documento']):
                user = User.objects.create_user('nombre','email@email','pass')
                user.username= request.POST['documento']
                user.first_name= request.POST['nombres']
                user.last_name= request.POST['apellidos']
                user.email= request.POST['email']
                user.password=make_password("@" + request.POST['nombres'][0] + request.POST['apellidos'][0] + request.POST['documento'][-4:])
                user.save()
              
            else:
                user=User.objects.get(username=request.POST['documento'])

            usuario= Usuario.objects.create(
                nombres=request.POST['nombres'],
                apellidos=request.POST['apellidos'],
                foto=form.cleaned_data.get('foto'),
                email=request.POST['email'],
                tipoDocumento=request.POST['tipoDocumento'],
                documento=request.POST['documento'],
                telefono=request.POST['telefono'],
                direccion=request.POST['direccion'],                
                fecha_nacimiento=request.POST['fecha_nacimiento'],                
                user=user,
                rol=request.POST['rol'],
            )
            return redirect('usuarios')
        else:
            form = UsuarioForm(request.POST,request.FILES)
    else:
        form= UsuarioForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'partials/crear.html',context)

def usuarios_editar(request, pk):
    titulo="Usuario - Editar"
    usuario= Usuario.objects.get(id=pk)
    if request.method == "POST":
        form= UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            messages.success(request, '¡usuario editado!') 
            form.save()
            return redirect('usuarios')
        else:
            print("Error al guardar")
    else:
        form= UsuarioForm(instance=usuario)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'partials/crear.html',context)

def usuarios_eliminar(request, pk):
    titulo="Usuario - Eliminar"
    usuarios= Usuario.objects.all()

    Usuario.objects.filter(id=pk).update(
            estado='Inactivo'
        )
    return redirect('usuarios')
        
   
    context={
        'usuarios':usuarios,
        'titulo':titulo,
     
    }
    return render(request,'usuarios/usuarios.html',context)


# Vistas del Beneficiario segun el Programa que se encuentre en la Fundación Un Lugar Donde Puedes Crecer

def beneficiario(request):  #este codigo muestra la lista de beneficiarios
    titulo="Beneficiarios"  
    beneficiarios= Beneficiario.objects.all()
    context={
        'titulo':titulo,
        'beneficiarios':beneficiarios        
    }
    return render(request, "usuarios/beneficiario.html", context)

def beneficiarios_crear(request):    #este codigo muestra el formulario para registrar un beneficiario
    titulo="Beneficiario - Registrar"
      
    if request.method == 'POST':
        form=BeneficiarioForm(request.POST, request.FILES)        
      
        if form.is_valid():
            messages.success(request, '¡beneficiario registrado!')
            form.save()
            return redirect('beneficiario')                                                                        
                       
    else:
        form=BeneficiarioForm()              
    context={
        'titulo':titulo,
        'form':form
    }
    
    return render(request,'partials/crear.html',context)


def beneficiario_editar(request, pk): #este codigo muestra el formulario para editar un beneficiario
    titulo="Beneficiario - Editar"
    beneficiario= Beneficiario.objects.get(id=pk)                  
    
    if request.method == "POST":
        form= BeneficiarioForm(request.POST, instance=beneficiario)
        if form.is_valid():
            messages.success(request, '¡beneficiario editado!')  
            form.save()
            return redirect('beneficiario')  
        else:
            print("El beneficiario no se guardo")
    else:
        form= BeneficiarioForm(instance=beneficiario)
    context={
        'titulo':titulo,
        'form':form       
        
    }
    return render(request,'partials/crear.html',context)


def beneficiario_eliminar(request, pk): #este codigo elimina un beneficiario
    titulo="Beneficiario - Eliminar"
    beneficiario = Beneficiario.objects.get(id=pk)
    beneficiario.delete()
    
    messages.success(request, '¡beneficiario eliminado!')    

    return redirect('/usuarios/beneficiario')

# Vistas del Acudiente del Beneficiario

def acudiente(request): #este codigo muestra la lista de acudientes
    titulo="Acudientes" 
    acudientes= Acudiente.objects.all()
    context={
        'titulo':titulo,
        'acudientes':acudientes
    }
    return render(request, "usuarios/acudiente.html", context)

def acudientes_crear(request):     #este codigo muestra el formulario para registrar un acudiente
    titulo="Acudiente - Registrar"
    if request.method == 'POST':
        form=AcudienteForm(request.POST)
        if form.is_valid():
            messages.success(request, '¡acudiente registrado!')
            form.save()
            return redirect('acudiente')
        else:
            print("el acudiente no se guardo")
    else:
        form=AcudienteForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request, "partials/crear.html", context)

def acudiente_editar(request, pk):   #este codigo muestra el formulario para editar un acudiente
    titulo="Acudiente - Editar"
    acudiente= Acudiente.objects.get(id=pk)
    if request.method == "POST":
        form= AcudienteForm(request.POST, instance=acudiente)
        if form.is_valid():
            messages.success(request, '¡acudiente editado!')
            form.save()
            return redirect('acudiente')  
        else:
            print("El acudiente no se guardo")
    else:
        form= AcudienteForm(instance=acudiente)
    context={
        'titulo':titulo,
        'form':form       
        
    }
    return render(request,'partials/crear.html',context)

# Vistas del Padrino del Beneficiario

def padrino(request): #este codigo muestra la lista de Padrinos
    titulo="Padrinos"
    padrinos= Padrino.objects.all()
    context={
        'titulo':titulo,
        'padrinos':padrinos
    }
    return render(request, "usuarios/padrino.html", context)

def padrinos_crear(request):   #este codigo muestra el formulario para registrar un Padrino
    titulo="Padrino - Registrar"
    if request.method == 'POST':
        form=PadrinoForm(request.POST)
        if form.is_valid():
            messages.success(request, '¡padrino registrado!')
            form.save()
            return redirect('padrino')
        else:
            print("el padrino no se guardo")
    else:
        form=PadrinoForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request, "partials/crear.html", context)

def padrino_editar(request, pk): #este codigo muestra el formulario para editar un padrino
    titulo="Padrino - Editar"
    padrino= Padrino.objects.get(id=pk)
    if request.method == "POST":
        form= PadrinoForm(request.POST, instance=padrino)
        if form.is_valid():
            messages.success(request, '¡padrino editado!') 
            form.save()
            return redirect('padrino')  
        else:
            print("El padrino no se guardo")
    else:
        form= PadrinoForm(instance=padrino)
    context={
        'titulo':titulo,
        'form':form       
        
    }
    return render(request,'partials/crear.html',context)

# Vistas de las Referencias del beneficiario

def referencia(request):   #este codigo muestra la lista de Referencias
    titulo="Referencias"
    referencias= Referencia.objects.all()
    context={
        'titulo':titulo,
        'referencias':referencias
    }
    return render(request, "usuarios/referencia.html", context)

def referencias_crear(request):    #este codigo muestra el formulario para registrar una Referencia
    titulo="Referencia - Registrar"
    if request.method == 'POST':
        form=ReferenciaForm(request.POST)
        if form.is_valid():
            messages.success(request, '¡referencia registrada!')
            form.save()
            return redirect('referencia')
        else:
            print("la referencia no se guardo")
    else:
        form=ReferenciaForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request, "partials/crear.html", context)

def referencia_editar(request, pk):   #este codigo muestra el formulario para editar una Referencia
    titulo="Referencia - Editar"
    referencia= Referencia.objects.get(id=pk)
    if request.method == "POST":
        form= ReferenciaForm(request.POST, instance=referencia)
        if form.is_valid():
            messages.success(request, '¡referencia editada!') 
            form.save()
            return redirect('referencia')  
        else:
            print("El padrino no se guardo")
    else:
        form= ReferenciaForm(instance=referencia)
    context={
        'titulo':titulo,
        'form':form       
        
    }
    return render(request,'partials/crear.html',context)
