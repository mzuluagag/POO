from Inicio import 
from Articulo import Articulo
class Comentario():
    listaComentarios = []

    def __init__(self, descripcion, puntuacion, articulo, usuario):
        self._descripcion = descripcion
        self._puntuacion = puntuacion
        self._articulo = articulo
        self._usuario = usuario
        Comentario.listaComentarios.append(self)


    #--------------------------------SETTERS-----------------------------------

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def setPuntuacion(self, puntuacion):
        self._puntuacion = puntuacion

    def setArticulo(self, articulo):
        self._articulo = articulo

    def setUsuario(self, usuario):
        self._usuario = usuario


    #--------------------------------GETTERS------------------------------------

    def getDescripcion(self):
        return self._descripcion

    def getPuntuacion(self):
        return self._puntuacion

    def getArticulo(self):
        return self._articulo

    def getUsuario(self):
        return self._usuario

    def editarComentario(self, puntacion, descripcion):
        self.setDescripcion(descripcion)
        self.setPuntuacion(puntuacion)


    @staticmethod
    def agregarComentarios(articulo, usuario, puntuacion, descripcion):
        comentario = Comentario(descripcion, puntuacion, articulo, usuario)
        articulo.addComentario(comentario)
