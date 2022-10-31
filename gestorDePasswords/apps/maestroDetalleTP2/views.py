from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date
from negocio.factura import ClsFacturas
from negocio.detalleFactura import ClsDetallesFactura
from negocio.producto import ClsProductos
from negocio.facturaDao import ClsFacturasDao
from negocio.facturaCargada import ClsFacturaCargada


# Create your views here.

def home(request):
    varObjDetalle = ClsDetallesFactura.varObjetoDetalle
    varListaObjCabecera = ClsFacturas.listaObjetosCabecera
    # messages.success(request, '¡Personas listadas!')

    if varObjDetalle is None:
        varObjDetalle = ClsDetallesFactura()

    varObjCabecera = ClsFacturas.varObjCabeceraSeleccionado
    if varObjCabecera is None:
        varObjCabecera = ClsFacturas()

    varObjFactura = ClsFacturas(None, varObjCabecera.titular, varObjCabecera.direccion, varObjCabecera.fechaEmision,
                                varObjCabecera.fechaVencimiento, varObjDetalle)
    ClsFacturas.varObjFacturaFinal = varObjFactura

    return render(request, "gestionFacturas.html",
                  {"productos": varObjFactura.detalleFactura.listaDeProductos, "listaCabecera": varListaObjCabecera,
                   "cabecera": varObjFactura, "subDetalle": varObjFactura.detalleFactura})


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
        ClsDetallesFactura.varObjetoDetalle = ClsDetallesFactura(None, [], None, 0)
    varListaProductos = ClsProductos.listaObjetosProductos
    ClsDetallesFactura.varObjetoDetalle.listaDeProductos = varListaProductos
    varImpuesto = ClsDetallesFactura.varObjetoDetalle.impuesto
    return render(request, "agregarDetalle.html", {"productos": varListaProductos, "impuesto": varImpuesto})


def agregarDetalle(request):
    varImpuesto = request.POST['txtImpuesto']
    varListaProductos = ClsDetallesFactura.varObjetoDetalle.listaDeProductos

    varObjDetalleDeFactura = ClsDetallesFactura(None, varListaProductos, None, varImpuesto)
    varObjDetalleDeFactura.calcularSubtotal()
    varObjDetalleDeFactura.calcularTotal()

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


def seleccionarCabecera(request, indice):
    varIndice = int(indice) - 1
    varObjCabecera = ClsFacturas.listaObjetosCabecera[varIndice]
    varObjCabecera.fechaEmision = date.today()
    ClsFacturas.varObjCabeceraSeleccionado = varObjCabecera
    return redirect('/maestroDetalleTP2/')


def guardarFacturaEnBd(request):
    ClsFacturasDao.insertarFactura(ClsFacturas.varObjFacturaFinal)
    ClsFacturas.varObjFacturaFinal = None
    ClsFacturas.listaObjetosCabecera = []
    ClsFacturas.varObjFacturaSeleccionada = None
    ClsDetallesFactura.varObjetoDetalle = None
    ClsProductos.listaObjetosProductos = []
    ClsFacturas.varObjCabeceraSeleccionado = None

    return redirect('/maestroDetalleTP2/')


def verTodasLasFacturas(request):
    ClsFacturas.listaDeTodasLasFacturas = ClsFacturasDao.obtenerTodasLasFacturas()
    listaDeTodasLasFacturas = ClsFacturas.listaDeTodasLasFacturas

    if ClsFacturas.varObjFacturaSeleccionada is None:
        varDetalleFactura = ClsDetallesFactura(None, [], None, None)
        varFacturaSeleccionada = ClsFacturas.varObjFacturaSeleccionada = ClsFacturas(detalleFactura=varDetalleFactura)

    else:
        varFacturaSeleccionada = ClsFacturas.varObjFacturaSeleccionada

    return render(request, "verTodasLasFacturas.html",
                  {"listaDeFacturas": listaDeTodasLasFacturas, "cabeceraFactura": varFacturaSeleccionada,
                   "detalleFactura": varFacturaSeleccionada.detalleFactura, "productosFactura":
                       varFacturaSeleccionada.detalleFactura.listaDeProductos})


def seleccionarFactura(request, indice):
    varIndice = int(indice) - 1
    varObjFactura = ClsFacturas.listaDeTodasLasFacturas[varIndice]
    varObjFactura = ClsFacturaCargada(varObjFactura.id)
    ClsFacturas.varObjFacturaSeleccionada = varObjFactura
    return redirect('/maestroDetalleTP2/verTodasLasFacturas/')


def modificacionDeFactura(request):
    varListaDeProductos = ClsFacturas.varObjFacturaSeleccionada.detalleFactura.listaDeProductos
    ClsProductos.listaObjetosProductos = varListaDeProductos
    if ClsDetallesFactura.varObjetoDetalle is None:
        ClsDetallesFactura.varObjetoDetalle = ClsDetallesFactura(impuesto=0)

    ClsDetallesFactura.varObjetoDetalle.listaDeProductos = varListaDeProductos
    ClsDetallesFactura.varObjetoDetalle.impuesto = ClsFacturas.varObjFacturaSeleccionada.detalleFactura.impuesto
    ClsDetallesFactura.varObjetoDetalle.calcularSubtotal()
    ClsDetallesFactura.varObjetoDetalle.calcularTotal()

    varListaProductos = ClsProductos.listaObjetosProductos
    varImpuesto = ClsDetallesFactura.varObjetoDetalle.impuesto
    varCabecera = ClsFacturas.varObjFacturaSeleccionada
    return render(request, "modificarFactura.html", {"productos": varListaProductos, "impuesto": varImpuesto,
                                                     "cabecera": varCabecera})


def modificarFactura(request):
    varImpuesto = request.POST['txtImpuesto']
    varListaProductos = ClsProductos.listaObjetosProductos

    ClsFacturas.varObjFacturaSeleccionada.detalleFactura.impuesto = varImpuesto
    ClsFacturas.varObjFacturaSeleccionada.detalleFactura.listaDeProductos = varListaProductos

    return redirect('/maestroDetalleTP2/')


def modificacionProducto(request, indice):
    varIndice = int(indice) - 1
    varObjProducto = ClsProductos.listaObjetosProductos[varIndice]
    ClsProductos.varGlIndiceProductoParaEditar = varIndice
    return render(request, "modificarProducto.html", {"producto": varObjProducto})


def modificarProducto(request):
    varProducto = request.POST['txtProducto']
    varCantidad = request.POST['txtCantidad']
    varDescripcion = request.POST['txtDescripcion']
    varPrecioUnitario = request.POST['txtPrecioUnitario']

    varObjProducto = ClsProductos(None, varProducto, varCantidad, varDescripcion, varPrecioUnitario)

    varIndice = ClsProductos.varGlIndiceProductoParaEditar
    ClsProductos.listaObjetosProductos[varIndice] = varObjProducto

    # messages.success(request, '¡Persona actualizada!')

    return redirect('/maestroDetalleTP2/modificacionFactura/')


def modificacionCabecera(request):
    return render(request, "modificarCabecera.html")


def modificarCabecera(request):
    varTitular = request.POST['txtTitular']
    varDireccion = request.POST['txtDireccion']
    varFechaVencimiento = request.POST['txtFechaVencimiento']

    ClsFacturas.varObjFacturaSeleccionada.titular = varTitular
    ClsFacturas.varObjFacturaSeleccionada.direccion = varDireccion
    ClsFacturas.varObjFacturaSeleccionada.fechaVencimiento = varFechaVencimiento

    return redirect('/maestroDetalleTP2/modificacionFactura/')


def actualizarFacturaEbBd(request):
    varImpuesto = request.POST['txtImpuesto']
    varListaProductos = ClsProductos.listaObjetosProductos

    varObjDetalleDeFactura = ClsDetallesFactura(None, varListaProductos, None, varImpuesto)
    varObjDetalleDeFactura.calcularSubtotal()
    varObjDetalleDeFactura.calcularTotal()

    ClsFacturas.varObjFacturaSeleccionada.detalleFactura = varObjDetalleDeFactura
    ClsFacturasDao.actualizarFactura(ClsFacturas.varObjFacturaSeleccionada)
    ClsFacturas.varObjFacturaFinal = None
    ClsFacturas.listaObjetosCabecera = []
    ClsFacturas.varObjFacturaSeleccionada = None
    ClsDetallesFactura.varObjetoDetalle = None
    ClsProductos.listaObjetosProductos = []
    ClsFacturas.varObjCabeceraSeleccionado = None

    return redirect('/maestroDetalleTP2/verTodasLasFacturas/')
