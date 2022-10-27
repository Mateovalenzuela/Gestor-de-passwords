from datos.conexion import ClsConexion
from detalleFactura import ClsDetallesFactura
from producto import ClsProductos
from productoDao import ClsProductosDao


class ClsDetallesFacturaDao:
    SELECCIONAR_ULTIMO_ID = 'SELECT id FROM Detalles_factura ORDER BY id DESC'
    SELECCIONAR_POR_ID = 'SELECT * FROM Detalles_factura WHERE '
    SELECCIONAR_LISTA_DE_ID = 'SELECT lista_de_id FROM Detalles_factura WHERE '
    INSERTAR = 'INSERT INTO Detalles_factura(id, lista_de_id, impuesto, total, subtotal) VALUES'
    UPDATE = 'UPDATE Detalles_factura SET '

    @classmethod
    def insertarDetalleFactura(cls, objDetalleFactura):
        varCursor = ClsConexion.ejecutarSql(cls.SELECCIONAR_ULTIMO_ID)
        varId = varCursor.fetchone()
        if varId is None:
            varId = 1
        else:
            varId = int(varId[0]) + 1  # obtiene el último id y le suma uno para agregar un nuevo registro

        varListaDeProductos = objDetalleFactura.listaDeProductos
        varListaDeIds = ClsProductosDao.insertarProductos(varListaDeProductos)
        varSubtotal = objDetalleFactura.subtotal
        varImpuesto = objDetalleFactura.impuesto
        varTotal = objDetalleFactura.total

        varListaStrDeIds = str(varListaDeIds)

        INSERT = cls.INSERTAR + f'({varId}, \'{varListaStrDeIds}\', {float(varImpuesto)}, {varTotal}, {varSubtotal})'
        ClsConexion.listaDeTransaccionSql.append(INSERT)
        return varId

    @classmethod
    def obtenerDetallePorId(cls, objDetalleFactura):
        varId = objDetalleFactura.id

        SELECCIONAR_POR_ID = cls.SELECCIONAR_POR_ID + f'id={varId}'
        varCursor = ClsConexion.ejecutarSql(SELECCIONAR_POR_ID)
        varDetalleFactura = varCursor.fetchone()
        varListaDeIds = eval(varDetalleFactura[1])  # convierte la cadena a una lista

        varObjDetalleFactura = ClsDetallesFactura(varDetalleFactura[0],
                                                  ClsProductosDao.obtenerProductosPorListaDeId(varListaDeIds),
                                                  varListaDeIds, varDetalleFactura[2])
        varObjDetalleFactura.calcularSubtotal()
        varObjDetalleFactura.calcularTotal()
        return varObjDetalleFactura

    @classmethod
    def obtenerListaDeIdPorIdDeDetalleFactura(cls, idDetalleFactura):
        varId = idDetalleFactura
        SELECCIONAR_LISTA_DE_ID = cls.SELECCIONAR_LISTA_DE_ID + f'id={varId}'
        varCursor = ClsConexion.ejecutarSql(SELECCIONAR_LISTA_DE_ID)
        varRegistro = varCursor.fetchone()  # selecciona la lista_de_id para el id de detalleFactura con el que estamos trabajando
        varListaDeIds = eval(varRegistro[0])  # convirte la cadena a lista
        return varListaDeIds

    @classmethod
    def actualizarDetalleFactura(cls, objDetalleFactura):
        varId = objDetalleFactura.id
        varListaDeProductosNueva = objDetalleFactura.listaDeProductos
        varListaDeIds = cls.obtenerListaDeIdPorIdDeDetalleFactura(varId)
        varSubtotal = objDetalleFactura.subtotal
        varImpuesto = float(objDetalleFactura.impuesto)
        varTotal = objDetalleFactura.total

        varEstadoDelUpdateDeProductos = ClsProductosDao.actualizarProducto(varListaDeIds, varListaDeProductosNueva)
        # print(varEstadoDelUpdateDeProductos)

        UPDATE = cls.UPDATE + f'''lista_de_id=\'{varListaDeIds}\', impuesto={varImpuesto}, total=\'{varTotal}\', 
                                subtotal={varSubtotal} WHERE id={varId}'''
        ClsConexion.listaDeTransaccionSql.append(UPDATE)


if __name__ == '__main__':
    salame = ClsProductos(None, 'salame', 1, 'salame', 150.00)
    pera = ClsProductos(None, 'pera', 3, 'medido en Kg', 100.00)

    listaDeProductos = [salame, pera]

    detalleFactura1 = ClsDetallesFactura(1, listaDeProductos, None, 21)
    detalleFactura1.calcularSubtotal()
    detalleFactura1.calcularTotal()

    # ClsDetallesFacturaDao.insertarDetalleFactura(detalleFactura1)

    ClsDetallesFacturaDao.actualizarDetalleFactura(detalleFactura1)

    objDetalle = ClsDetallesFacturaDao.obtenerDetallePorId(detalleFactura1)
    print(objDetalle.listaDeProductos[0].producto)
