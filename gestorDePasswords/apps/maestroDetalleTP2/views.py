from django.shortcuts import render, redirect
from django.contrib import messages
from negocio.factura import ClsFacturas
from negocio.detalleFactura import ClsDetallesFactura
from negocio.producto import ClsProductos
from negocio.productoDao import ClsProductosDao


# Create your views here.

def home(request):
    varObjDetalle = ClsDetallesFactura.varObjetoDetalle
    varObjCabecera = ClsFacturas.listaObjetosCabecera
    # messages.success(request, '¡Personas listadas!')

    if varObjDetalle is None:
        varObjDetalle = ClsDetallesFactura()

    return render(request, "gestionFacturas.html",
                  {"productos": varObjDetalle.listaDeProductos, "cabecera": varObjCabecera})


def gestionCabecera(request):
    return render(request, "agregarCabecera.html")


def agregarCabecera(request):
    varTitular = request.POST['txtTitular']
    varDireccion = request.POST['txtDireccion']
    varFechaVencimiento = request.POST['txtFechaVencimiento']

    objCabeceraFactura = ClsFacturas(None, varTitular, varDireccion, None, varFechaVencimiento, None)

    ClsFacturas.listaObjetosCabecera.append(objCabeceraFactura)

    return redirect('/maestroDetalleTP2/')


def gestionProducto(request):
    return render(request, "agregarProducto.html")


def agregarProducto(request):
    varProducto = request.POST['txtProducto']
    varCantidad = request.POST['txtCantidad']
    varDescripcion = request.POST['txtDescripcion']
    varPrecioUnitario = request.POST['txtPrecioUnitario']

    varObjProducto = ClsProductos(None, varProducto, varCantidad, varDescripcion, varPrecioUnitario)
    ClsProductos.listaObjetosProductos.append(varObjProducto)

    return redirect('/maestroDetalleTP2/gestionDetalle')


def gestionDetalle(request):
    varListaProductos = ClsProductos.listaObjetosProductos
    return render(request, "agregarDetalle.html", {"productos": varListaProductos})


def agregarDetalle(request):
    varImpuesto = request.POST['txtImpuesto']
    varListaProductos = ClsProductos.listaObjetosProductos

    varObjDetalleDeFactura = ClsDetallesFactura(None, varListaProductos, varImpuesto)
    ClsDetallesFactura.varObjetoDetalle = varObjDetalleDeFactura

    return redirect('/maestroDetalleTP2/')


def edicionProducto(request, indice):
    varIndice = ClsProductosDao.buscarIndiceProducto(indice)
    varObjProducto = ClsDetallesFactura.listaDeProductos[varIndice]
    return render(request, "editarPersona.html", {"producto": varObjProducto})


def editarProducto(request):
    varProducto = request.POST['txtProducto']
    varCantidad = request.POST['txtCantidad']
    varDescripcion = request.POST['txtDescripcion']
    varPrecioUnitario = request.POST['txtPrecioUnitario']

    varObjProducto = ClsProductos(None, varProducto, varCantidad, varDescripcion, varPrecioUnitario)

    varIndice = ClsProductos.varGlIndiceProductoParaEditar
    ClsProductos.listaObjetosProductos[varIndice] = varObjProducto

    # messages.success(request, '¡Persona actualizada!')

    return redirect('/maestroDetalleTP2/gestionDetalle/')


def eliminarPersona(request, varId):
    varObjPersona = ClsPersonas(varId, None, None, None, None, None, None, None, None, None, None)
    ClsPersonaDao.eliminarPersona(varObjPersona)

    messages.success(request, '¡Persona eliminada!')
    return redirect('/trabajoPractico1/')
