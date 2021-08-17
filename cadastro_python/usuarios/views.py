from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm


def inicio(request) :
  usuarios = Usuario.objects.all()
  context = {
    'usuarios' : usuarios
  }
  return render(request, 'usuarios/inicio.html', context)

def detail(request, id) :
  detail_usuario = get_object_or_404(Usuario , pk = id)
  context = {
    'detail_usuario' : detail_usuario
  }
  return render(request , 'usuarios/detail.html', context)

def create_usuario(request) :
  if request.method == 'POST' :
    usuario_form = UsuarioForm(request.POST)
    if usuario_form.is_valid() :
        usuario_form.save()
        return redirect('aplication:inicio')
  else :
    usuario_form = UsuarioForm()
  return render(request , 'usuarios/create.html' , {'usuario_form' : usuario_form})

def update_usuario(request, id) :
  usuario = get_object_or_404(Usuario, id = id)
  if request.method == "POST" :
    usuario_form = UsuarioForm(request.POST , instance = usuario)
    if usuario_form.is_valid() :
        usuario_form.save()
        return redirect('aplication:inicio')
  else :
    usuario_form = UsuarioForm()
    return render(request, 'usuarios/editar.html', {'usuario_form' : usuario_form} )

def delete_usuario(request, id) :
  usuario = get_object_or_404(Usuario, id = id)

  if usuario : 
    usuario.delete()

  return redirect('aplication:inicio')