from datos.models import *

class ClsPasswordDao:

    def __init__(self):
        pass

    @classmethod
    def obtenerTodasLasPasswords(cls):
        return ClsPasswords.objects.all()

    @classmethod
    def registrarPassword(cls, nombre, password, descripcion):
        ClsPasswords.objects.create(nombre=nombre, password=password,
                           descripcion=descripcion)


    @classmethod
    def obtenerPasswordPorId(cls, id):
        return ClsPasswords.objects.get(id=id)


    @classmethod
    def actualizarPassword(cls,id, nombre, password, descripcion):
        varPasswords = cls.obtenerPasswordPorId(id)
        varPasswords.nombre = nombre
        varPasswords.password = password
        varPasswords.descripcion = descripcion
        varPasswords.save()


    @classmethod
    def eliminarPassword(cls,id):
        varPassword = cls.obtenerPasswordPorId(id)
        varPassword.delete()