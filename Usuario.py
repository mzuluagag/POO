from datetime import date
from Textos import Texto

class Usuario():
    dictUsuariosID = {}
    dictUsuariosEmail = {}

    def __init__(self):
        self._nombres = None
        self._apellidos = None
        self._sobrenombre = None
        self._email = None
        self._iden = None
        self._ubicacion = None
        self._fechaDeNacimiento = None
        self._presupuesto = None


    # ----------------------------------------------SETTERS---------------------------------------------

    def setNombres(self, nombres):
        self._nombres = nombres

    def setApellidos(self, apellidos):
        self._apellidos = apellidos

    def setSobrenombre(self, sobrenombre):
        self._sobrenombre = sobrenombre

    def setEmail(self, email, fromRegister = False):
        aux = email
        while(True):

            if(aux in Usuario.dictUsuariosEmail.keys() and fromRegister):
                print(Texto.mensajesRegistro["aemail"])
                aux = input(Texto.mensajesRegistro["email"])
            else:
                self._email = email
                Usuario.dictUsuariosEmail[email] = self
                break

    def setId(self, iden, fromRegister = False):
        aux = iden
        while(True):
            if(aux in Usuario.dictUsuariosID.keys() and fromRegister):
                print(Texto.mensajesRegistro["aiden"])
                aux = input(Texto.mensajesRegistro["id"])
            else:
                self._iden = iden
                Usuario.dictUsuariosID[iden] = self
                break

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def setFechaDeNacimiento(self, fdn):
        self._fechaDeNacimiento = fdn

    def setPresupuesto(self, presupuesto, fromRegister = False):
        aux = presupuesto
        while(True):
            if(aux < 0 and fromRegister):
                print(Texto.mensajesRegistro["apresupuesto"])
                aux = int(input(Texto.mensajesRegistro[8]))
            else:
                self._presupuesto = presupuesto
                break

    # -------------------------------------------GETTERS----------------------------------------------

    def getNombres(self):
        return self._nombres

    def getApellidos(self):
        return self._apellidos

    def getSobrenombre(self):
        return self._sobrenombre

    def getEmail(self):
        return self._email

    def getId(self):
        return self._iden

    def getUbicacion(self):
        return self._ubicacion

    def getFechaDeNacimiento(self):
        return self._fechaDeNacimiento

    def getPresupuesto(self):
        return self._presupuesto

    # -----------------------------------FUNCIONALIDADES----------------------------------------------
    def RecargarPresupuesto(self, recarga):
        pass

    def RestarPresupuesto(self, resta):
        pass

    def RegistrarComoArtista(self, *newdata):
        pass

    #------------------------------------METODOS ESTATICOS---------------------------------------------

    @staticmethod
    def Registro():

        while(True):
            print(Texto.mensajesRegistro["instruccionU"])
            nuevoUsuario = Usuario()
            nuevoUsuario.setNombres(input(Texto.mensajesRegistro["nombre"]))
            nuevoUsuario.setApellidos(input(Texto.mensajesRegistro["apellido"]))
            nuevoUsuario.setSobrenombre(input(Texto.mensajesRegistro["sobrenombre"]))
            nuevoUsuario.setEmail(input(Texto.mensajesRegistro["email"]), True)
            nuevoUsuario.setId(input(Texto.mensajesRegistro["id"]), True)
            nuevoUsuario.setUbicacion(input(Texto.mensajesRegistro["ubic"]))
            nuevoUsuario.setFechaDeNacimiento(input(Texto.mensajesRegistro["fdn"]))
            nuevoUsuario.setPresupuesto(int(input(Texto.mensajesRegistro["presupuesto"])), True)
            print(Texto.mensajesRegistro["registrocorrectoU"])
            return nuevoUsuario


    @staticmethod
    def IngresoValido():
        while(True):
            iden = input(Texto.mensajesValidacion["id"])
            if (iden in Usuario.dictUsuariosID.keys()):
                return Usuario.dictUsuariosID[iden]
            else:
                print(Texto.mensajesValidacion["nousuario"])












