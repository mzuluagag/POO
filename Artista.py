from Usuario import Usuario
from Textos import Texto
class Artista (Usuario):
    dictArtistasID = {}
    dictArtistasEmail = {}

    def __init__(self):
        super().__init__()
        self._ocupacion = None
        self._reputacion = None
        self._articulos = dict()
        self._telefono = None
        self._articulosVendidos = dict()


    # --------------------------------SETTERS---------------------------------------------
    def setId(self, iden, fromRegister = False):
        aux = iden
        while(True):
            if(aux in Usuario.dictUsuariosID.keys() and fromRegister):
                print(Texto.mensajesRegistro["aiden"])
                aux = input(Texto.mensajesRegistro["id"])
            else:
                self._iden = iden
                Usuario.dictUsuariosID[iden] = self
                Artista.dictUsuariosID[iden] = self
                break
    def setEmail(self, email, fromRegister = False):
        aux = email
        while(True):
            if(aux in Usuario.dictUsuariosEmail.keys() and fromRegister):
                print(Texto.mensajesRegistro["aemail"])
                aux = input(Texto.mensajesRegistro["email"])
            else:
                self._email = email
                Usuario.dictUsuariosEmail[email] = self
                Artista.dictArtistasEmail[email] = self
                break

    def setOcupacion(self, ocupacion):
        self._ocupacion = ocupacion

    def setTelefono(self, telefono):
        self._telefono = telefono

    def addArticulo(self, articulo):
        self._articulos[articulo.getNombre()] = articulo

    def addArticuloVendido(self, articuloVendido):
        self._articulosVendidos[articuloVendido.getNombre()]= articuloVendido

    def setReputation(self):
        pass

    # ---------------------------------GETTERS---------------------------------------------

    def getOcupacion(self):
        return self._ocupacion

    def getReputacion(self):
        return self._reputacion

    def getArticulos(self):
        return self._articulos

    def getTelefono(self):
        return self._telefono

    def getArticulosVendidos(self):
        return self._articulosVendidos

    # --------------------------------METODOSESTATICOS--------------------------------------

    @staticmethod
    def RegistroArtista():
        usuarioActual = super(Artista,Artista).Registro()
        print(Texto.mensajesRegistro["instruccionA"])
        nuevoArtista = Artista()
        nuevoArtista.setNombres(usuarioActual.getNombres())
        nuevoArtista.setApellidos(usuarioActual.getApellidos())
        nuevoArtista.setSobrenombre(usuarioActual.getSobrenombre())
        nuevoArtista.setId(usuarioActual.getId())
        nuevoArtista.setEmail(usuarioActual.getEmail())
        nuevoArtista.setFechaDeNacimiento(usuarioActual.getFechaDeNacimiento())
        nuevoArtista.setUbicacion(usuarioActual.getUbicacion())
        nuevoArtista.setPresupuesto(usuarioActual.getPresupuesto())
        nuevoArtista.setOcupacion(input(Texto.mensajesRegistro["ocupacion"]))
        nuevoArtista.setTelefono(input(Texto.mensajesRegistro["tel"]))
        print(Texto.mensajesRegistro["registrocorrectoA"])
        return nuevoArtista






    @staticmethod
    def IngresoValidoArtista():
        while(True):
            iden = input(Texto.mensajesValidacion["id"])
            if(iden in Artista.dictArtistasID.keys()):
                return Artista.dictArtistasID[iden]
            else:
                print(Texto.mensajesValidacion["noartista"])


