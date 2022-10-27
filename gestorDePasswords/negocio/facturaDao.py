from datos.conexion import ClsConexion
from negocio.detalleFactura import ClsDetallesFactura
from negocio.factura import ClsFacturas
from negocio.detalleFacturaDao import ClsDetallesFacturaDao
from negocio.producto import ClsProductos



class ClsFacturasDao:

    SELECCIONAR_POR_ID = 'SELECT * FROM Facturas WHERE '
    SELECCIONAR = 'SELECT * FROM Facturas'
    INSERTAR = 'INSERT INTO Facturas(titular, direccion, fecha_vencimiento, id_detalle_factura) VALUES'
    UPDATE = 'UPDATE Facturas SET '

    @classmethod
    def insertarFactura(cls, objFactura):
        varTitular = objFactura.titular
        varDireccion = objFactura.direccion
        varFechaVencimiento = objFactura.fechaVencimiento
        varObjDetalleFactura = objFactura.detalleFactura

        varIdDetalleFactura = ClsDetallesFacturaDao.insertarDetalleFactura(varObjDetalleFactura)

        INSERT = cls.INSERTAR + f'(\'{varTitular}\', \'{varDireccion}\', \'{varFechaVencimiento}\', {varIdDetalleFactura})'
        ClsConexion.listaDeTransaccionSql.append(INSERT)

        ClsConexion.ejecutarTransaccionSql(ClsConexion.listaDeTransaccionSql)
        ClsConexion.listaDeTransaccionSql = []

    @classmethod
    def obtenerFacturaPorId(cls, objFactura):
        varId = objFactura.id

        SELECCIONAR_POR_ID = cls.SELECCIONAR_POR_ID + f'id={varId}'
        varCursor = ClsConexion.ejecutarSql(SELECCIONAR_POR_ID)
        varFactura = varCursor.fetchone()

        varObjDetalleFactura = ClsDetallesFactura(int(varFactura[5]))

        varObjDetalleFactura = ClsDetallesFacturaDao.obtenerDetallePorId(varObjDetalleFactura)

        varObjFactura = ClsFacturas(varFactura[0], varFactura[1], varFactura[2], varFactura[3], varFactura[4],
                                    varObjDetalleFactura)

        return varObjFactura

    @classmethod
    def obtenerTodasLasFacturas(cls):
        SELECCIONAR = 'SELECT id FROM Facturas'
        varCursor = ClsConexion.ejecutarSql(SELECCIONAR)
        varIdFacturas = varCursor.fetchall()

        varListaDeFacturas = []
        for id in varIdFacturas:
            varIdFactura = ClsFacturas(id[0])
            varObjFacturaCargada = cls.obtenerFacturaPorId(varIdFactura)
            varListaDeFacturas.append(varObjFacturaCargada)

        return varListaDeFacturas

    @classmethod
    def actualizarFactura(cls, objFactura):
        varId = objFactura.id
        varTitular = objFactura.titular
        varDireccion = objFactura.direccion
        varFechaVencimiento = objFactura.fechaVencimiento
        objFactura.detalleFactura.id = varId
        varObjDetalleFactura = ClsDetallesFacturaDao.actualizarDetalleFactura(objFactura.detalleFactura)

        UPDATE = cls.UPDATE + f'''titular=\'{varTitular}\', direccion=\'{varDireccion}\', 
        fecha_vencimiento=\'{varFechaVencimiento}\' WHERE id={varId}'''

        ClsConexion.listaDeTransaccionSql.append(UPDATE)
        ClsConexion.ejecutarTransaccionSql(ClsConexion.listaDeTransaccionSql)

        ClsConexion.listaDeTransaccionSql = []


if __name__ == '__main__':
    masitas = ClsProductos(None, 'masitas', 3, 'surtidas', 25.00)
    arroz = ClsProductos(None, 'arroz', 1, 'medido en Kg', 70.00)
    helado = ClsProductos(None, 'helado', 1, 'medido en Kg', 700)


    listaDeProductos = [masitas, arroz]

    detalleFactura1 = ClsDetallesFactura(None, listaDeProductos, None, 21.00)
    detalleFactura1.calcularSubtotal()
    detalleFactura1.calcularTotal()

    factura1 = ClsFacturas(2, 'Sergio Busquets', 'AV.ricardo 810', None, '2022-10-29', detalleFactura1)

    #ClsFacturasDao.actualizarFactura(factura1)

    #ClsFacturasDao.insertarFactura(factura1)

    #objFactura = ClsFacturasDao.obtenerFacturaPorId(factura1)
    #print(objFactura.titular)

    listaFacturas = ClsFacturasDao.obtenerTodasLasFacturas()
    for i in listaFacturas:
        print(i.titular)


