from datos.conexion import ClsConexion
from .password import ClsPasswords


class ClsPasswordDao:
    SELECCIONAR = 'SELECT * FROM Passwords ORDER BY id'
    SELECCIONAR_POR_ID = 'SELECT * FROM Passwords WHERE '
    INSERTAR = 'INSERT INTO Passwords(nombre, password, descripcion) VALUES'
    UPDATE = 'UPDATE Passwords SET '
    ELIMIAR = 'DELETE FROM Passwords WHERE '

    @classmethod
    def obtenerTodos(cls):
        varCursor = ClsConexion.ejecutarSql(cls.SELECCIONAR)
        varRegistros = varCursor.fetchall()
        varListPasswords = []
        for registro in varRegistros:
            password = ClsPasswords(registro[0], registro[1], registro[2], registro[3])
            varListPasswords.append(password)
        return varListPasswords

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
        varCursor = ClsConexion.ejecutarSql(SELECCIONAR_POR_ID)
        varRegistro = varCursor.fetchone()
        objPassword = ClsPasswords(varRegistro[0], varRegistro[1], varRegistro[2], varRegistro[3])
        return objPassword



if __name__ == '__main__':
    objPassword = ClsPasswords(5, None, None, None)
    print(ClsPasswordDao.obtenerPorId(objPassword))

    # passwords = ClsPasswordDao.obtenerTodos()

    # for i in passwords:
    # print(i)
