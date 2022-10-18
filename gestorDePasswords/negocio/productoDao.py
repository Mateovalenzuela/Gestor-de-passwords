from negocio.producto import ClsProductos


class ClsProductosDao:

    @classmethod
    def insertarProducto(cls, objProducto):
        varProducto = objProducto.producto
        varCantidad = objProducto.cantidad
        varDescripcion = objProducto.descripcion
        varPrecioUnitario = objProducto.precioUnitario
        varimporte = objProducto.importe

        INSERT = cls.INSERTAR + f'''(\'{varNombre}\', \'{varApellido}\', \'{varApodo}\', \'{varSexo}\', \'{varNacionalidad}\',
    \'{varFechaNacimiento}\', {varEsFeliz}, {varEdad}, {varDni}, {varAltura})'''
        ClsConexion.ejecutarSql(INSERT)




    @classmethod
    def obtenerProductosPorListaDeId(cls, listaDeId):
        listaDeProductos  = []
        for i in listaDeId:
            if i == '-':
                continue
            selectProducto = f'sentencia sql con id{i}'
            #ejecutar sentencia
            productoObtenido = 'pepe'

            for registro in productoObtenido:
                producto = ClsProductos(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])
                listaDeProductos.append(producto)