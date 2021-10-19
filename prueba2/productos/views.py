from django import template
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.template import context, loader
from productos.forms import UsuarioForm
from .models import Usuario
from django.contrib import messages

# Create your views here.

def home(request):
    template =loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def index(request):
    template = loader.get_template('productos/index.html')
    context ={}
    return HttpResponse(template.render(context, request))

def catalogo(request):
    template = loader.get_template('productos/catalogo.html')
    context = {}
    return HttpResponse(template.render(context,request))
    
def new_usuario(request):
    if request.method=='POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            correo = form.cleaned_data['correo']
            clave = form.cleaned_data['clave']
            usuario = Usuario(nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono,correo=correo, clave=clave)
            usuario.save()
            messages.success(request, "Te has registrado correctamente")
            return HttpResponseRedirect(reverse('catalogo'))
    else: 
        form = UsuarioForm()  
    return render(request, 'productos/crear_usuario.html', {'form':form})

def producto(request):
    template =loader.get_template('productos/producto.html')
    context = {}
    return HttpResponse(template.render(context,request))

def bases(request):
    template =loader.get_template('productos/bases.html')
    context = {}
    return HttpResponse(template.render(context,request))

def iluminador(request):
    template =loader.get_template('productos/iluminador.html')
    context = {}
    return HttpResponse(template.render(context,request))

def pestanina(request):
    template =loader.get_template('productos/pestanina.html')
    context = {}
    return HttpResponse(template.render(context,request))




