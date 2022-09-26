from django.shortcuts import render, redirect
from django.contrib import messages
from negocio.passwordDao import *


# Create your views here.

def home(request):
    varPasswords = ClsPasswordDao.obtenerTodasLasPasswords()
    messages.success(request, '¡Contraseñas listadas!')
    return render(request, "gestionPasswords.html", {"passwords": varPasswords})


def registrarPassword(request):
    varNombre = request.POST['txtNombre']
    varPassword = request.POST['txtPassword']
    varDescripcion = request.POST['txtDescripcion']

    ClsPasswordDao.registrarPassword(varNombre, varPassword, varDescripcion)

    messages.success(request, '¡Contraseña registrada!')
    return redirect('/')


def edicionPassword(request, varId):
    varPassword = ClsPasswordDao.obtenerPasswordPorId(varId)

    return render(request, "edicionPassword.html", {"password": varPassword})


def editarPassword(request):
    varId = request.POST['txtId']
    varNombre = request.POST['txtNombre']
    varPassword = request.POST['txtPassword']
    varDescripcion = request.POST['txtDescripcion']

    ClsPasswordDao.actualizarPassword(varId, varNombre, varPassword, varDescripcion)

    messages.success(request, '¡Contraseña actualizada!')

    return redirect('/')


def eliminarPassword(request, varId):
    ClsPasswordDao.eliminarPassword(varId)

    messages.success(request, '¡Contraseña eliminada!')
    return redirect('/')


