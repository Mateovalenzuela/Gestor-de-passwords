from django.shortcuts import render, redirect
from django.contrib import messages
from negocio.factura import ClsFacturas
from negocio.detalleFactura import ClsDetallesFactura


# Create your views here.

def home(request):
    varObjDetalle = ClsDetallesFactura.listaObjetosDetalle
    # messages.success(request, '¡Personas listadas!')
    return render(request, "gestionFacturas.html", {"detalles": varObjDetalle})


def gestionCabecera(request):
    return render(request, "agregarCabecera.html")


def agregarCabecera(request):
    varTitular = request.POST['txtTitular']
    varDireccion = request.POST['txtDireccion']
    varFechaVencimiento = request.POST['txtFechaVencimiento']

    objCabeceraFactura = ClsFacturas(None, varTitular, varDireccion, None, varFechaVencimiento, None)

    print(objCabeceraFactura.titular)

    return redirect('/maestroDetalleTP2/')


def gestionDetalle(request):
    return render(request, "agregarDetalle.html")


def agregarDetalle(request):
    varProducto = request.POST['txtProducto']
    varCantidad = request.POST['txtCantidad']
    varDescripcion = request.POST['txtDescripcion']
    varPrecioUnitario = request.POST['txtPrecioUnitario']
    varImpuesto = request.POST['txtImpuesto']

    objDetalleFactura = ClsDetallesFactura(None, varProducto, varCantidad, varDescripcion, varPrecioUnitario,
                                           varImpuesto)
    ClsDetallesFactura.listaObjetosDetalle.append(objDetalleFactura)

    print(objDetalleFactura.producto)

    return redirect('/maestroDetalleTP2/')


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
