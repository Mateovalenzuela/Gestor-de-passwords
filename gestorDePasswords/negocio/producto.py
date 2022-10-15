class ClsProductos:
    listaObjetosProductos = []
    varGlIndiceProductoParaEditar = None

    def __init__(self, id=None, producto=None, cantidad=None, descripcion=None, precioUnitario=None):
        self._id = id
        self._producto = producto
        self._cantidad = cantidad
        self._descripcion = descripcion
        self._precioUnitario = float(precioUnitario)
        self._importe = (self._precioUnitario * float(self._cantidad))

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def producto(self):
        return self._producto

    @producto.setter
    def producto(self, producto):
        self._producto = producto

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def precioUnitario(self):
        return str(self._precioUnitario)

    @precioUnitario.setter
    def precioUnitario(self, precioUnitario):
        self._precioUnitario = precioUnitario

    @property
    def importe(self):
        return str(self._importe)

    @importe.setter
    def importe(self, importe):
        self._importe = importe
