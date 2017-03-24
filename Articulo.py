from datetime import date
from Textos import Texto
from Usuario import Usuario
from Artista import Artista

class Articulo():
    dictArticulos = {}

    def __init__(self):
        self._precio = None
        self._nombre = None
        self._artista = None
        self._descripcion = None
        self._comentarios = dict()
        self._puntuacion = 0
        self._fechaPublicacion = date.today()
        self._tipo = None
        Articulo.dictArticulos[self._nombre] = self


    #------------------------------------------SETTERS------------------------------------------------------------------

    def setPrecio(self, precio):
        while(True):
            if (precio >= 0):
                self._precio = precio
                break
            else:
                print(Texto.mensajesObras["aprecio"])


    def setNombre(self, nombre):
        while(True):
            if(nombre in Articulo.dictArticulos.keys()):
                print(Texto.mensajesObras["anombre"])
            else:
                self._nombre = nombre
                break

    def setArtista(self, artista):
        self._artista = artista

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def addComentario(self, comentario):
        self._comentarios.append(comentario)

    def setPuntuacion(self):
        pass

    def setFechaPublicacion(self):
        self._fechaPublicacion = date.today()

    def setTipo(self, tipo):
        self._tipo = tipo

    #-------------------------------------GETTERS-----------------------------------------------------------------------

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
    def AgregarArticulo(artista):
        while(True):
            print(Texto.mensajesObras["instrucciones:"])
            nuevoArticulo = Articulo()
            nuevoArticulo.setNombre(input(Texto.mensajesObras[1]))
            nuevoArticulo.setPrecio(int(input(Texto.mensajesObras[2])))
            nuevoArticulo.setTipo(input(Texto.mensajesObras[3]))
            nuevoArticulo.setDescripcion(input(Texto.mensajesObras[4]))
            nuevoArticulo.setArtista(artista)
            artista.addArticulo(nuevoArticulo)
            print(Texto.mensajesObras["registrocorrecto"])
            return nuevoArticulo

    @staticmethod
    def EditarArticulo(articulo,artista):
        if(artista.getId() == articulo.getArtista().getId()):
            Articulo.info(articulo)
            print(Texto.mensajesObras["edit"])
            articulo.setNombre(input(Texto.mensajesObras[1]))
            articulo.setPrecio(int(input(Texto.mensajesObras[2])))
            articulo.setTipo(input(Texto.mensajesObras[3]))
            articulo.setDescripcion(input(Texto.mensajesObras[4]))
            return articulo
        else:
            print(Texto.mensajesObras["nopuedeedit"])

    @staticmethod
    def EliminarArticulo(articulo, artista):
        if(artista.getId() == articulo.getArtista().getId()):
            artista = articulo.getArtista()
            nombre = articulo.getNombre()
            artista._articulos.pop(nombre)
            Articulo.dictArticulos.pop(nombre)
            print(Texto.mensajesObras["elim"])
        else:
            print(Texto.mensajesObras["nopuedeedit"])

    @staticmethod
    def info(articulo):
        print(Texto.mensajesObras["datos"])
        print(Texto.mensajesObras["artista"] + articulo.getArtista().getSobrenombre())
        print(Texto.mensajesObras["nombre"] + articulo.getNombre())
        print(Texto.mensajesObras["precio"] + articulo.getPrecio())
        print(Texto.mensajesObras["tipo"] + articulo.getTipo())
        print(Texto.mensajesObras["descripcion"] + articulo.getDescripcion())
        print(Texto.mensajesObras["fdp"] + articulo.getFechaPublicacion())
        print(Texto.mensajesObras["puntuacion"] + articulo.getPuntuacion())





