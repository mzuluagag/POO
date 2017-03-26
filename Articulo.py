from datetime import date
from Textos import Texto
from Usuario import Usuario
from Artista import Artista


class Articulo():
    dictArticulos = {}

    def __init__(self, nombre, precio, artista, tipo, descripcion,  fromRegister = False, puntuacion=0, comentarios=None):
        self._precio = None
        self._nombre = None
        self._artista = None
        self._descripcion = None
        self._puntuacion = None
        self._comentarios = comentarios
        self._fechaPublicacion = date.today()
        self._tipo = None
        self.setPuntuacion(puntuacion)
        self.setNombre(nombre, fromRegister)
        self.setPrecio(precio, fromRegister)
        self.setArtista(artista)
        self.setTipo(tipo)
        self.setDescripcion(descripcion)
        self.setPuntuacion(puntuacion)
        Articulo.dictArticulos[self._nombre] = self

    # ------------------------------------------SETTERS------------------------------------------------------------------

    def setPrecio(self, precio, fromRegister):
        aux = precio
        while (True):
            if (precio >= 0 and fromRegister==False):
                self._precio = precio
                break
            else:
                print(Texto.mensajesObras["aprecio"])
                aux = int(input(Texto.mensajesObras["precio"]))

    def setNombre(self, nombre, fromRegister):
        aux = nombre
        while (True):
            if (nombre in Articulo.dictArticulos.keys() and fromRegister):
                print(Texto.mensajesObras["anombre"])
                aux = input(Texto.mensajesObras["nombre"])
            else:
                self._nombre = nombre
                break

    def setArtista(self, artista):
        self._artista = artista

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def addComentario(self, comentario):
        self._comentarios.append(comentario)

    def setPuntuacion(self, puntuacion):
        if(puntuacion == 5):
            _puntuacion = puntuacion
        elif(puntuacion == 4):
            _puntuacion = puntuacion
        elif(puntuacion == 3):
            _puntuacion = puntuacion
        elif(puntuacion == 2):
            _puntuacion = puntuacion
        elif(puntuacion == 1):
            _puntuacion = puntuacion
        else:
            _puntuacion = 0
    
    def setFechaPublicacion(self):
        self._fechaPublicacion = date.today()

    def setTipo(self, tipo):
        self._tipo = tipo

    # -------------------------------------GETTERS-----------------------------------------------------------------------

    def getPrecio(self):
        return self._precio

    def getNombre(self):
        return self._nombre

    def getArtista(self):
        return self._artista

    def getDescripcion(self):
        return self._descripcion

    def getComentarios(self):
        return self._comentarios

    def getPuntuacion(self):
        return self._puntuacion

    def getFechaPublicacion(self):
        return self._fechaPublicacion

    def getTipo(self):
        return self._tipo

    # --------------------------------------METODOS ESTATICOS---------------------------------
    @staticmethod
    def AgregarArticulo(nombre, precio, artista, tipo, descripcion):
        nuevoArticulo = Articulo(nombre,precio,artista,tipo,descripcion, True)
        artista.addArticulo(nuevoArticulo)
        return nuevoArticulo

    # -----------------------------------FUNCIONALIDADES----------------------------------------
    def EditarArticulo(self, artista, nombre, precio, tipo, descripcion):
        if (artista.getId() == self.getArtista().getId()):
            self.setNombre(nombre)
            self.setPrecio(precio)
            self.setTipo(tipo)
            self.setDescripcion(descripcion)
            return True
        else:
            return False

    def EliminarArticulo(self, artista):
        if (artista.getId() == self.getArtista().getId()):
            artista = self.getArtista()
            nombre = self.getNombre()
            artista._articulos.pop(nombre)
            Articulo.dictArticulos.pop(nombre)
            return True
        else:
            return False

    def info(self):
        return {self._nombre, self._precio, self._tipo, self._descripcion, self._puntuacion}

    def CalcularPuntuacionPromedio(self):
        cont = 0
        for x in dictArticulos:
            cont += dictArticulos[x].getPuntuacion
        return cont / len(dictArticulos)

    def ObtenerMejorComentario(self):
        pass
            
        
    def ObtenerNumeroVistas(self):
        pass

    def MostrarMejorArticulo(self):
        mejoresArticulos = []
        for x in range(5,0):
            for i in dictArticulos:
                if(dictArticulos[i].getPuntuacion == x):
                    mejoresArticulos.append(i)
            if(len(mejoresArticulos) > 0):
                break
        return mejoresArticulos







