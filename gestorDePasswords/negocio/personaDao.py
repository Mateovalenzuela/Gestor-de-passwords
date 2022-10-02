from datos.conexion import *
from .persona import *

class ClsPersonaDao:
    SELECCIONAR = 'SELECT * FROM Personas ORDER BY id'
    SELECCIONAR_POR_ID = 'SELECT * FROM Personas WHERE '
    INSERTAR = 'INSERT INTO Personas(nombre, password, descripcion) VALUES'
    UPDATE = 'UPDATE Personas SET '
    ELIMIAR = 'DELETE FROM Personas WHERE '

    @classmethod
    def obtenerTodos(cls):
        varListaTodosPersonas = ClsConexion.ejecutarSelect(cls.SELECCIONAR)
        return varListaTodosPersonas

    @classmethod
    def insertarPassword(cls, objPassword):
        varNombre = objPassword.nombre
        varPassword = objPassword.password
        varDescripcion = objPassword.descripcion
        INSERT = cls.INSERTAR + f'(\'{varNombre}\', \'{varPassword}\', \'{varDescripcion}\')'
        ClsConexion.ejecutarSql(INSERT)
        print(f'password insertada: {objPassword}')

    @classmethod
    def actualizarPassword(cls, objPassword):
        varId = objPassword.id
        varNombre = objPassword.nombre
        varPassword = objPassword.password
        varDescripcion = objPassword.descripcion
        UPDATE = cls.UPDATE + f'nombre=\'{varNombre}\', password=\'{varPassword}\', descripcion=\'{varDescripcion}\' WHERE id={varId}'
        ClsConexion.ejecutarSql(UPDATE)
        print(f'password actualizada: {objPassword}')

    @classmethod
    def eliminarPassword(cls, objPassword):
        varId = objPassword.id
        ELIMINAR = cls.ELIMIAR + f'id={varId}'
        ClsConexion.ejecutarSql(ELIMINAR)
        print(f'persona eliminada {objPassword}')

    @classmethod
    def obtenerPorId(cls, objPassword):
        varId = objPassword.id
        SELECCIONAR_POR_ID = cls.SELECCIONAR_POR_ID + f'id={varId}'
        varPassword = ClsConexion.ejecutarSelectPorId(SELECCIONAR_POR_ID)
        return varPassword


if __name__ == '__main__':
    objPassword = ClsPasswords(5, None, None, None)
    print(ClsPasswordDao.obtenerPorId(objPassword))

    # passwords = ClsPasswordDao.obtenerTodos()

    # for i in passwords:
    # print(i)

