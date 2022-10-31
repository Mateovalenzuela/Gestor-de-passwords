class ClsPasswords:

    def __int__(self, id=None, nombre=None, password=None, descripcion=None):
        self._id = id
        self._nombre = nombre
        self._password = password
        self._descripcion = descripcion

    def __str__(self):
        return f'id: {self._id}, nombre: {self._nombre}'

    def cargarPropiedades(self,id):
        self.nombre = None
        self.password = None
        self.descripcion = None


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
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion


if __name__ == '__main__':
    password1 = ClsPasswords()
    password1.__int__(1, 'pepe', 'pepe123', 'nombre y 123')
    password1.nombre = 'jooorge'
    print(password1)

