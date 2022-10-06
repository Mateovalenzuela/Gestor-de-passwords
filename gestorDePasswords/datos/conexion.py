import sqlite3
import sys


class ClsConexion:
    varRutaBd = '../dataBases/dbPrincipal.s3db'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = sqlite3.connect(cls.varRutaBd, check_same_thread=False)
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
            return varCursor


if __name__ == '__main__':
    ClsConexion.obtenerConexion()
    ClsConexion.obtenerCursor()
