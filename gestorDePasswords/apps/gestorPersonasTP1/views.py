from django.shortcuts import render, redirect
from django.contrib import messages
from negocio.personaDao import *


# Create your views here.

def home(request):
    varPersonas = ClsPersonaDao.obtenerTodasLasPersonas()
    messages.success(request, '¡Personas listadas!')
    return render(request, "gestionPersonas.html", {"personas": varPersonas})


def registrarPersona(request):
    varNombre = request.POST['txtNombre']
    varApellido = request.POST['txtApellido']
    varApodo = request.POST['txtApodo']
    varSexo = request.POST['txtSexo']
    varNacionalidad = request.POST['txtNacionalidad']
    varFechaNac = request.POST['txtFechaNac']
    varEsFeliz = request.POST.get('txtEsFeliz')
    varEdad = request.POST['txtEdad']
    varDni = request.POST['txtDni']
    varAltura = request.POST['txtAltura']

    if not varEsFeliz:
        varEsFeliz = False

    ClsPersonaDao.registrarPersona(varNombre, varApellido, varApodo, varSexo, varNacionalidad, varFechaNac,
                                   varEsFeliz, varEdad, varDni, varAltura)

    messages.success(request, '¡Persona registrada!')
    return redirect('/trabajoPractico1/')


def edicionPersona(request, varId):
    varPersona = ClsPersonaDao.obtenerPersonaPorId(varId)

    return render(request, "edicionPersona.html", {"persona": varPersona})


def editarPersona(request):
    varId = request.POST['txtId']
    varNombre = request.POST['txtNombre']
    varApellido = request.POST['txtApellido']
    varApodo = request.POST['txtApodo']
    varSexo = request.POST['txtSexo']
    varNacionalidad = request.POST['txtNacionalidad']
    varFechaNac = request.POST['txtFechaNac']
    varEsFeliz = request.POST.get('txtEsFeliz')
    varEdad = request.POST['txtEdad']
    varDni = request.POST['txtDni']
    varAltura = request.POST['txtAltura']

    if not varEsFeliz:
        varEsFeliz = False

    ClsPersonaDao.actualizarPersona(varId, varNombre, varApellido, varApodo, varSexo, varNacionalidad, varFechaNac,
                                    varEsFeliz, varEdad, varDni, varAltura)

    messages.success(request, '¡Persona actualizada!')

    return redirect('/trabajoPractico1/')


def eliminarPersona(request, varId):
    ClsPersonaDao.eliminarPersona(varId)

    messages.success(request, '¡Persona eliminada!')
    return redirect('/trabajoPractico1/')


