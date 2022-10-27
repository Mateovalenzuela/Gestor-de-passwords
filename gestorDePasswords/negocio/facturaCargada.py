from negocio.facturaDao import ClsFacturasDao
from negocio.factura import ClsFacturas


class ClsFacturaCargada:

    def __init__(self, id):
        varIdFactura = ClsFacturas(id)
        varObjFactura = ClsFacturasDao.obtenerFacturaPorId(varIdFactura)

        self._id = varObjFactura.id
        self._titular = varObjFactura.titular
        self._direccion = varObjFactura.direccion
        self._fechaEmision = varObjFactura.fechaEmision
        self._fechaVencimiento = varObjFactura.fechaVencimiento
        self._detalleFactura = varObjFactura.detalleFactura

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
