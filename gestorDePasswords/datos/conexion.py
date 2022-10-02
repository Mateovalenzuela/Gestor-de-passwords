import sqlite3
import sys
from negocio.password import ClsPasswords


class ClsConexion:
    varRutaBd = 'test.s3db'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = sqlite3.connect(cls.varRutaBd)
                print(f'Conexion exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                print(f'Ocurrió un error: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                print(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                print(f'Ocurrió una exepción al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor

    @classmethod
    def ejecutarSql(cls, sql):
        with ClsConexion.obtenerConexion() as conexion:
            varCursor = conexion.cursor()
            varCursor.execute(sql)

    @classmethod
    def ejecutarSelect(cls, sql):
        with ClsConexion.obtenerConexion():
            varCursor = ClsConexion.obtenerCursor()
            varCursor.execute(sql)
            varRegistros = varCursor.fetchall()
            varListPasswords = []
            for registro in varRegistros:
                password = ClsPasswords(registro[0], registro[1], registro[2], registro[3])
                varListPasswords.append(password)
            return varListPasswords

    @classmethod
    def ejecutarSelectPorId(cls, sql):
        with ClsConexion.obtenerConexion():
            varCursor = ClsConexion.obtenerCursor()
            varCursor.execute(sql)
            varRegistro = varCursor.fetchone()
            objPassword = ClsPasswords(varRegistro[0], varRegistro[1], varRegistro[2], varRegistro[3])
            return objPassword


if __name__ == '__main__':
    ClsConexion.obtenerConexion()
    ClsConexion.obtenerCursor()
