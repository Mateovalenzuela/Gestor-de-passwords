from negocio.producto import ClsProductos


class ClsProductosDao:

    @classmethod
    def buscarIndiceProducto(cls, producto):
        varCont = 0
        varListaProductos = ClsProductos.listaObjetosProductos
        for i in varListaProductos:
            if i.producto == producto:
                return varCont
            else:
                varCont += 1
