class ClsFacturas:

    listaObjetosCabecera = []
    varObjCabeceraSeleccionado = None
    varObjFacturaFinal = None

    listaDeTodasLasFacturas = []
    varObjFacturaSeleccionada = None

    def __init__(self, id=None, tituar=None, direccion=None, fechaEmision=None, fechaVencimiento=None,
                 detalleFactura=None):
        self._id = id
        self._titular = tituar
        self._direccion = direccion
        self._fechaEmision = fechaEmision
        self._fechaVencimiento = fechaVencimiento
        self._detalleFactura = detalleFactura

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def fechaEmision(self):
        return self._fechaEmision

    @fechaEmision.setter
    def fechaEmision(self, fechaEmision):
        self._fechaEmision = fechaEmision

    @property
    def fechaVencimiento(self):
        return self._fechaVencimiento

    @fechaVencimiento.setter
    def fechaVencimiento(self, fechaVencimiento):
        self._fechaVencimiento = fechaVencimiento

    @property
    def detalleFactura(self):
        return self._detalleFactura

    @detalleFactura.setter
    def detalleFactura(self, detalleFactura):
        self._detalleFactura = detalleFactura
