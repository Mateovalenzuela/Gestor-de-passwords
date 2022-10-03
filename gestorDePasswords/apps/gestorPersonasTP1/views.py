from django.shortcuts import render, redirect
from django.contrib import messages
from negocio.personaDao import *
from negocio.persona import *


# Create your views here.

def home(request):
    varPersonas = ClsPersonaDao.obtenerTodos()
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

    varObjPersona = ClsPersonas(None, varNombre, varApellido, varApodo, varSexo, varNacionalidad, varFechaNac,
                                varEsFeliz, varEdad, varDni, varAltura)
    ClsPersonaDao.insertarPersona(varObjPersona)

    messages.success(request, '¡Persona registrada!')
    print(varFechaNac)
    print(varEsFeliz)
    return redirect('/trabajoPractico1/')


def edicionPersona(request, varId):
    varObjPersona = ClsPersonas(varId)
    varPersona = ClsPersonaDao.obtenerPorId(varObjPersona)

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

    varObjPersona = ClsPersonas(varId, varNombre, varApellido, varApodo, varSexo, varNacionalidad, varFechaNac,
                                varEsFeliz, varEdad, varDni, varAltura)

    ClsPersonaDao.actualizarPersona(varObjPersona)

    messages.success(request, '¡Persona actualizada!')

    return redirect('/trabajoPractico1/')


def eliminarPersona(request, varId):
    varObjPersona = ClsPersonas(varId, None, None, None, None, None, None, None, None, None, None)
    ClsPersonaDao.eliminarPersona(varObjPersona)

    messages.success(request, '¡Persona eliminada!')
    return redirect('/trabajoPractico1/')
