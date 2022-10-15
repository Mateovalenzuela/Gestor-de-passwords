from django.shortcuts import render, redirect
from django.contrib import messages
from negocio.factura import ClsFacturas
from negocio.detalleFactura import ClsDetallesFactura
from negocio.producto import ClsProductos


# Create your views here.

def home(request):
    varObjDetalle = ClsDetallesFactura.varObjetoDetalle
    varListaObjCabecera = ClsFacturas.listaObjetosCabecera
    # messages.success(request, '¡Personas listadas!')

    if varObjDetalle is None:
        varObjDetalle = ClsDetallesFactura()

    return render(request, "gestionFacturas.html",
                  {"productos": varObjDetalle.listaDeProductos, "listaCabecera": varListaObjCabecera})


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
    if ClsDetallesFactura.varObjetoDetalle is None:
        ClsDetallesFactura.varObjetoDetalle = ClsDetallesFactura(None, [], 0)
    varListaProductos = ClsProductos.listaObjetosProductos
    varImpuesto = ClsDetallesFactura.varObjetoDetalle.impuesto
    return render(request, "agregarDetalle.html", {"productos": varListaProductos, "impuesto": varImpuesto})


def agregarDetalle(request):
    varImpuesto = request.POST['txtImpuesto']
    varListaProductos = ClsProductos.listaObjetosProductos

    varObjDetalleDeFactura = ClsDetallesFactura(None, varListaProductos, varImpuesto)
    ClsDetallesFactura.varObjetoDetalle = varObjDetalleDeFactura

    return redirect('/maestroDetalleTP2/')


def edicionProducto(request, indice):

    varIndice = int(indice) - 1
    varObjProducto = ClsProductos.listaObjetosProductos[varIndice]
    ClsProductos.varGlIndiceProductoParaEditar = varIndice
    return render(request, "editarProducto.html", {"producto": varObjProducto})


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


def eliminarProducto(request, indice):
    varIndice = int(indice) - 1
    ClsProductos.listaObjetosProductos.pop(varIndice)
    return redirect('/maestroDetalleTP2/gestionDetalle')
