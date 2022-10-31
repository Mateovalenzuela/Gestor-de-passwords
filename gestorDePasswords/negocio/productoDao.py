from negocio.producto import ClsProductos
from datos.conexion import ClsConexion


class ClsProductosDao:
    SELECCIONAR_POR_ID = 'SELECT * FROM Productos WHERE '
    INSERTAR = 'INSERT INTO Productos(producto, cantidad, descripcion, precio_unitario, importe) VALUES'
    UPDATE = 'UPDATE Productos SET '

    @classmethod
    def insertarProductos(cls, listaDeProductos):
        varCadenaDeIdsDeProductosInsertados = []
        varContadorDeProductosInsertados = 0
        for objProducto in listaDeProductos:
            varProducto = objProducto.producto
            varCantidad = objProducto.cantidad
            varDescripcion = objProducto.descripcion
            varPrecioUnitario = objProducto.precioUnitario
            varimporte = objProducto.importe

            INSERT = cls.INSERTAR + f'''(\'{varProducto}\', {varCantidad}, \'{varDescripcion}\', {varPrecioUnitario},
             {varimporte})'''

            ClsConexion.ejecutarSql(INSERT)
            varContadorDeProductosInsertados += 1

        SELECCIONAR_POR_ID = f'SELECT id FROM Productos ORDER BY id DESC LIMIT {varContadorDeProductosInsertados}'
        varCursor = ClsConexion.ejecutarSql(SELECCIONAR_POR_ID)
        varIds = varCursor.fetchall()
        varIds.sort()
        for i in varIds:
            list(i)
            varCadenaDeIdsDeProductosInsertados.append(i[0])

        return varCadenaDeIdsDeProductosInsertados

    @classmethod
    def obtenerProductosPorListaDeId(cls, listaDeId):
        listaDeProductos = []
        for id in listaDeId:
            SELECCIONAR_POR_ID = ClsProductosDao.SELECCIONAR_POR_ID + f'id={id}'
            varCursor = ClsConexion.ejecutarSql(SELECCIONAR_POR_ID)
            varProducto = varCursor.fetchone()

            varObjProducto = ClsProductos(varProducto[0], varProducto[1], varProducto[2], varProducto[3], varProducto[4])
            listaDeProductos.append(varObjProducto)

        return listaDeProductos

    @classmethod
    def actualizarProducto(cls, listaDeId, listaDeProductos):
        varIndiceParaListaDeId = 0
        if len(listaDeId) != len(listaDeProductos):
            return False
        else:
            for objProducto in listaDeProductos:
                varProducto = objProducto.producto
                varCantidad = objProducto.cantidad
                varDescripcion = objProducto.descripcion
                varPrecioUnitario = objProducto.precioUnitario
                varimporte = objProducto.importe

                UPDATE = cls.UPDATE + f'''producto=\'{varProducto}\', cantidad={varCantidad}, 
                descripcion=\'{varDescripcion}\', precio_unitario={varPrecioUnitario}, importe={varimporte} 
                WHERE id={listaDeId[varIndiceParaListaDeId]}'''

                ClsConexion.listaDeTransaccionSql.append(UPDATE)
                varIndiceParaListaDeId += 1
            return True


if __name__ == '__main__':
    salame = ClsProductos(None, 'salame', 1, 'salame', 150.00)
    manzana = ClsProductos(None, 'manzana', 3, 'medido en Kg', 100.00)

    listaDeProductos = [salame, manzana]
    ids = [28, 38]
    print(ids)

    # cadenaDeID = '1-2-3-456'

    ClsProductosDao.actualizarProducto(ids, listaDeProductos)
    productos = ClsProductosDao.obtenerProductosPorListaDeId(ids)

    for i in productos:
        print(i.producto)
