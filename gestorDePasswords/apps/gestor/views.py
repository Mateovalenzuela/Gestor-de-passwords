from django.shortcuts import render, redirect
from django.contrib import messages
from negocio.passwordDao import *
from negocio.password import *


# Create your views here.

def home(request):
    varPasswords = ClsPasswordDao.obtenerTodos()
    messages.success(request, '¡Contraseñas listadas!')
    return render(request, "gestionPasswords.html", {"passwords": varPasswords})


def registrarPassword(request):
    varNombre = request.POST['txtNombre']
    varPassword = request.POST['txtPassword']
    varDescripcion = request.POST['txtDescripcion']

    varObjPassword = ClsPasswords(None, varNombre, varPassword, varDescripcion)

    ClsPasswordDao.insertarPassword(varObjPassword)

    messages.success(request, '¡Contraseña registrada!')
    return redirect('/')


def edicionPassword(request, varId):
    varObjPassword = ClsPasswords(varId, None, None, None)
    varPassword = ClsPasswordDao.obtenerPorId(varObjPassword)

    return render(request, "edicionPassword.html", {"password": varPassword})


def editarPassword(request):
    varId = request.POST['txtId']
    varNombre = request.POST['txtNombre']
    varPassword = request.POST['txtPassword']
    varDescripcion = request.POST['txtDescripcion']

    varObjPassword = ClsPasswords(varId, varNombre, varPassword, varDescripcion)
    ClsPasswordDao.actualizarPassword(varObjPassword)

    messages.success(request, '¡Contraseña actualizada!')

    return redirect('/')


def eliminarPassword(request, varId):
    varObjPassword = ClsPasswords(varId, None, None, None)
    ClsPasswordDao.eliminarPassword(varObjPassword)

    messages.success(request, '¡Contraseña eliminada!')
    return redirect('/')


