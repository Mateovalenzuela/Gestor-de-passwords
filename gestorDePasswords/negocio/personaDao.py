from datos.conexion import *
from .persona import *


class ClsPersonaDao:
    SELECCIONAR = 'SELECT * FROM Personas ORDER BY id'
    SELECCIONAR_POR_ID = 'SELECT * FROM Personas WHERE '
    INSERTAR = 'INSERT INTO Personas(nombre, apellido, apodo, sexo, nacionalidad, nacimiento, feliz, edad, dni, altura) VALUES'
    UPDATE = 'UPDATE Personas SET '
    ELIMINAR = 'DELETE FROM Personas WHERE '

    @classmethod
    def obtenerTodos(cls):
        varCursor = ClsConexion.ejecutarSql(cls.SELECCIONAR)
        varRegistros = varCursor.fetchall()
        varListPersonas = []
        for registro in varRegistros:
            varPersona = ClsPersonas(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5],
                                     registro[6], registro[7], registro[8], registro[9], registro[10])
            varListPersonas.append(varPersona)
        return varListPersonas

    @classmethod
    def insertarPersona(cls, objPersona):
        varNombre = objPersona.nombre
        varApellido = objPersona.apellido
        varApodo = objPersona.apodo
        varSexo = objPersona.sexo
        varNacionalidad = objPersona.nacionalidad
        varFechaNacimiento = objPersona.nacimiento
        varEsFeliz = objPersona.feliz
        varEdad = objPersona.edad
        varDni = objPersona.dni
        varAltura = objPersona.altura
        INSERT = cls.INSERTAR + f'''(\'{varNombre}\', \'{varApellido}\', \'{varApodo}\', \'{varSexo}\', \'{varNacionalidad}\',
\'{varFechaNacimiento}\', {varEsFeliz}, {varEdad}, {varDni}, {varAltura})'''
        ClsConexion.ejecutarSql(INSERT)
        print(f'password insertada: {objPersona}')

    @classmethod
    def actualizarPersona(cls, objPersona):
        varId = objPersona.id
        varNombre = objPersona.nombre
        varApellido = objPersona.apellido
        varApodo = objPersona.apodo
        varSexo = objPersona.sexo
        varNacionalidad = objPersona.nacionalidad
        varFechaNacimiento = objPersona.nacimiento
        varEsFeliz = objPersona.feliz
        varEdad = objPersona.edad
        varDni = objPersona.dni
        varAltura = objPersona.altura
        UPDATE = cls.UPDATE + f'''nombre=\'{varNombre}\', apellido=\'{varApellido}\', apodo=\'{varApodo}\', 
        sexo=\'{varSexo}\', nacionalidad=\'{varNacionalidad}\', nacimiento=\'{varFechaNacimiento}\', feliz={varEsFeliz}, 
        edad={varEdad}, dni={varDni}, altura={varAltura} WHERE id={varId}'''
        ClsConexion.ejecutarSql(UPDATE)
        print(f'password actualizada: {objPersona}')

    @classmethod
    def eliminarPersona(cls, objPersona):
        varId = objPersona.id
        ELIMINAR = cls.ELIMINAR + f'id={varId}'
        ClsConexion.ejecutarSql(ELIMINAR)
        print(f'persona eliminada {objPersona}')

    @classmethod
    def obtenerPorId(cls, objPersona):
        varId = objPersona.id
        SELECCIONAR_POR_ID = cls.SELECCIONAR_POR_ID + f'id={varId}'
        varCursor = ClsConexion.ejecutarSql(SELECCIONAR_POR_ID)
        varRegistro = varCursor.fetchone()
        varObjPersona = ClsPersonas(varRegistro[0], varRegistro[1], varRegistro[2], varRegistro[3], varRegistro[4],
                                    varRegistro[5], varRegistro[6], varRegistro[7], varRegistro[8], varRegistro[9],
                                    varRegistro[10])
        return varObjPersona


if __name__ == '__main__':
    objPassword = ClsPersonas(1)
    print(ClsPersonaDao.obtenerPorId(objPassword))

    # passwords = ClsPasswordDao.obtenerTodos()

    # for i in passwords:
    # print(i)
