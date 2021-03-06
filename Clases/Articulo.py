from Usuario import Usuario
from Artista import Artista
from datetime import date
from Textos import Texto


class Articulo():
    dictArticulos = {}
    iden = 1

    def __init__(self, nombre, precio, artista, tipo, descripcion, fromRegister=False):
        self._precio = None
        self._nombre = None
        self._artista = None
        self._descripcion = None
        self._puntuacion = None
        self._comentarios = dict()
        self._fechaPublicacion = date.today()
        self._tipo = None
        self._estado = True
        self._id = str(Articulo.iden)
        self.setNombre(nombre)
        self.setPrecio(precio, fromRegister)
        self.setArtista(artista)
        self.setTipo(tipo)
        self.setDescripcion(descripcion)
        artista.addArticulo(self)
        Articulo.dictArticulos[str(Articulo.iden)] = self
        Articulo.iden += 1

    # ------------------------------------------SETTERS------------------------------------------------------------------

    def setPrecio(self, precio, fromRegister):
        aux = precio
        while (True):
            if (aux >= 0):
                self._precio = precio
                break
            else:
                print(Texto.mensajesObras["aprecio"])
                aux = int(input(Texto.mensajesObras["precio"]))

    def setNombre(self, nombre):
        self._nombre = nombre

    def setArtista(self, artista):
        self._artista = artista

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def addComentario(self, comentario):
        self._comentarios[comentario._id] = comentario

    def setPuntuacion(self):
        cont = 0
        if (len(self._comentarios) > 0):
            for x in self._comentarios:
                cont += int(self._comentarios[x].getPuntuacion())
            self._puntuacion = cont / len(self._comentarios)
        else:
            self._puntuacion = None

    def setFechaPublicacion(self):
        self._fechaPublicacion = date.today()

    def setTipo(self, tipo):
        self._tipo = tipo

    def setEstado(self, estado):
        self._estado = estado

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

    def getId(self):
        return int(self._id)

    def getTipo(self):
        return self._tipo

    def getEstado(self):
        return self._estado

        # -----------------------------------FUNCIONALIDADES----------------------------------------


    def EditarArticulo(self, artista, nombre, precio, tipo, descripcion):
        if (artista.getId() == self.getArtista().getId()):
            self.setNombre(nombre)
            self.setPrecio(precio, True)
            self.setTipo(tipo)
            self.setDescripcion(descripcion)
            return True
        else:
            return False


    def EliminarArticulo(self, artista):
        if (artista.getId() == self.getArtista().getId()):
            artista = self.getArtista()
            iden = self._id
            del artista._articulos[iden]
            del Articulo.dictArticulos[iden]
            return True
        else:
            return False


    def info(self):
        return {self._nombre, self._precio, self._tipo, self._descripcion, self._puntuacion, self._id}


    def ObtenerNumeroVistas(self):
        pass


    def MostrarMejorArticulo(self):
        mejoresArticulos = []
        for x in range(5, 0):
            for i in Articulo.dictArticulos:
                if (Articulo.dictArticulos[i].getPuntuacion == x):
                    mejoresArticulos.append(i)
            if (len(mejoresArticulos) > 0):
                break
        return mejoresArticulos


    def ComprarArticulo(self, usuario):
        if (usuario.getPresupuesto() >= self.getPrecio()):
            artista = self.getArtista()
            artista._articulosVendidos[str(self.getId())] = self
            usuario._obrasCompradas[str(self.getId())] = self
            usuario.RestarPresupuesto(self.getPrecio())
            self.setEstado(False)
            del artista._articulos[str(self.getId())]
            del Articulo.dictArticulos[str(self.getId())]
            return True
        else:
            return False

# --------------------------------------METODOS ESTATICOS------------------------------------------------------------

    @staticmethod
    def AgregarArticulo(nombre, precio, artista, tipo, descripcion):
        nuevoArticulo = Articulo(nombre, precio, artista, tipo, descripcion, True)
        return nuevoArticulo

    @staticmethod
    def BuscarArticulo(nombre):
        related = dict()
        palabras = nombre.split(' ')
        for palabra in palabras:
            for i in Articulo.dictArticulos:
                if ((Articulo.dictArticulos[i].getNombre().find(palabra)) >= 0 and
                        not (i in related.keys())):
                    related[i] = Articulo.dictArticulos[i]
        return related

    @staticmethod
    def OrdenarPorPuntuacion():
        articulos = []
        for i in Articulo.dictArticulos:
            Articulo.dictArticulos[i].setPuntuacion()
            if (Articulo.dictArticulos[i].getPuntuacion() != None):
                articulos.append(Articulo.dictArticulos[i])
        articulos.sort(key=lambda articulo: articulo._puntuacion, reverse=True)
        return articulos

    @staticmethod
    def GenerarDatosFicticios():
        Articulo("Las medias 1", 900, Artista.dictArtistasID["4"], "fisico", "gay")
        Articulo("Las camisas 2", 901, Artista.dictArtistasID["4"], "digital", "gay")
