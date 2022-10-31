from negocio.personaDao import ClsPersonaDao
from negocio.persona import ClsPersonas


class ClsPersonaCargada:

    def __init__(self, id):
        varIdObjPersona = ClsPersonas(id=id)
        varObjPersona = ClsPersonaDao.obtenerPorId(varIdObjPersona)

        self._id = varObjPersona.id
        self._nombre = varObjPersona.nombre
        self._apellido = varObjPersona.apellido
        self._apodo = varObjPersona.apodo
        self._sexo = varObjPersona.sexo
        self._nacionalidad = varObjPersona.nacionalidad
        self._nacimiento = varObjPersona.nacimiento
        self._feliz = varObjPersona.feliz
        self._edad = varObjPersona.edad
        self._dni = varObjPersona.dni
        self._altura = varObjPersona.altura

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def apodo(self):
        return self._apodo

    @apodo.setter
    def apodo(self, apodo):
        self._apodo = apodo

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    @property
    def nacionalidad(self):
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self._nacionalidad = nacionalidad

    @property
    def nacimiento(self):
        return self._nacimiento

    @nacimiento.setter
    def nacimiento(self, nacimiento):
        self._nacimiento = nacimiento

    @property
    def feliz(self):
        return self._feliz

    @feliz.setter
    def feliz(self, feliz):
        self._feliz = feliz

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura
