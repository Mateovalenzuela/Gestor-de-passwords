from datos.models import *


class ClsPersonaDao:

    def __init__(self):
        self.__id = None
        self.__nombre = None
        self.__apellido = None
        self.__apodo = None
        self.__sexo = None
        self.__nacionalidad = None
        self.__nacimiento = None
        self.__feliz = None
        self.__edad = None
        self.__dni = None
        self.__altura = None

    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getApodo(self):
        return self.__apodo

    def setApodo(self, apodo):
        self.__apodo = apodo

    def getSexo(self):
        return self.__sexo

    def setSexo(self, sexo):
        self.__sexo = sexo

    def getNacionalidad(self):
        return self.__nacionalidad

    def setNacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    def getFeliz(self):
        return self.__feliz

    def setFeliz(self, esFeliz):
        self.__feliz = esFeliz

    def getNacimiento(self):
        return self.__nacimiento

    def setNacimiento(self, fechaNac):
        self.__nacimiento = fechaNac

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def getDni(self):
        return self.__dni

    def setDni(self, dni):
        self.__dni = dni

    def getAltura(self):
        return self.__altura

    def setAltura(self, altura):
        self.__altura = altura

    def cargarPropiedades(self, id):
        varPersona = ClsPersonas.objects.get(id=id)
        ClsPersonaDao.setNombre(self, varPersona.nombre)
        ClsPersonaDao.setApellido(self, varPersona.apellido)
        ClsPersonaDao.setApodo(self, varPersona.apodo)
        ClsPersonaDao.setSexo(self, varPersona.sexo)
        ClsPersonaDao.setNacionalidad(self, varPersona.nacionalidad)
        ClsPersonaDao.setNacimiento(self, varPersona.nacimiento)
        ClsPersonaDao.setFeliz(self, varPersona.feliz)
        ClsPersonaDao.setEdad(self, varPersona.edad)
        ClsPersonaDao.setDni(self, varPersona.dni)
        ClsPersonaDao.setAltura(self, varPersona.altura)

    @classmethod
    def obtenerTodasLasPersonas(cls):
        return ClsPersonas.objects.all()

    @classmethod
    def registrarPersona(cls, nombre, apellido, apodo, sexo, nacionalidad, fechaNac, esFeliz, edad, dni, altura):
        ClsPersonas.objects.create(nombre=nombre, apellido=apellido, apodo=apodo, sexo=sexo, nacionalidad=nacionalidad,
                                   nacimiento=fechaNac, feliz=esFeliz, edad=edad, dni=dni, altura=altura)

    @classmethod
    def obtenerPersonaPorId(cls, id):
        return ClsPersonas.objects.get(id=id)

    @classmethod
    def actualizarPersona(cls, id, nombre, apellido, apodo, sexo, nacionalidad, fechaNac, esFeliz, edad, dni, altura):
        varPersona = cls.obtenerPersonaPorId(id)
        varPersona.nombre = nombre
        varPersona.apellido = apellido
        varPersona.apodo = apodo
        varPersona.sexo = sexo
        varPersona.nacionalidad = nacionalidad
        varPersona.nacimiento = fechaNac
        varPersona.feliz = esFeliz
        varPersona.edad = edad
        varPersona.dni = dni
        varPersona.altura = altura

        varPersona.save()

    @classmethod
    def eliminarPersona(cls, id):
        varPersona = cls.obtenerPersonaPorId(id)
        varPersona.delete()

