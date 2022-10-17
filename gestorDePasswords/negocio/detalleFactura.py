class ClsDetallesFactura:
    varObjetoDetalle = None

    def __init__(self, id=None, listaProductos=None, impuesto=None):
        if impuesto is not None:
            float(impuesto)
        self._id = id
        self._listaDeProductos = listaProductos
        self._subtotal = None
        self._impuesto = impuesto
        self._total = None

    @property
    def id(self):
        return self._id

    @property
    def listaDeProductos(self):
        return self._listaDeProductos

    @listaDeProductos.setter
    def listaDeProductos(self, listaDeProductos):
        self._listaDeProductos = listaDeProductos

    @property
    def subtotal(self):
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        self._subtotal = subtotal

    @property
    def impuesto(self):
        return str(self._impuesto)

    @impuesto.setter
    def impuesto(self, impuesto):
        self._impuesto = impuesto

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    def calcularSubtotal(self):
        varImporteTotal = 0
        for i in self._listaDeProductos:
            varImporteTotal += float(i.importe)

        varSubtotalRedondeado = round(varImporteTotal, 2)

        self.subtotal = varSubtotalRedondeado

    def calcularTotal(self):
        varImpuesto = (float(self._impuesto) / 100) + 1
        varTotalCalculado = self.subtotal * varImpuesto
        varValorTotalRedondeado = round(varTotalCalculado, 2)
        self.total = varValorTotalRedondeado
