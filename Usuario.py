from datetime import date
from Textos import Texto

class Usuario():
    dictUsuariosID = {}
    dictUsuariosEmail = {}

    def __init__(self, nombres, apellidos, sobrenombre, email, iden, fechaDeNacimiento, presupuesto, fromRegister = False):
        self._nombres = None
        self._apellidos = None
        self._sobrenombre = None
        self._email = None
        self._iden = None
        self._fechaDeNacimiento = None
        self._presupuesto = None
        self.setNombres(nombres)
        self.setApellidos(apellidos)
        self.setSobrenombre(sobrenombre)
        self.setEmail(email, fromRegister)
        self.setId(iden, fromRegister)
        self.setFechaDeNacimiento(fechaDeNacimiento)
        self.setPresupuesto(presupuesto, fromRegister)


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



    def setFechaDeNacimiento(self, fdn):
        self._fechaDeNacimiento = fdn

    def setPresupuesto(self, presupuesto, fromRegister = False):
        aux = presupuesto
        while(True):
            if(aux < 0 and fromRegister):
                print(Texto.mensajesRegistro["apresupuesto"])
                aux = int(input(Texto.mensajesRegistro["presupuesto"]))
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

    def info(self):
        return {self._nombres, self._apellidos,
                self._sobrenombre, self._email,
                self._iden, self._fechaDeNacimiento,
                self._presupuesto}


    # ------------------------------------METODOS ESTATICOS---------------------------------------------

    @staticmethod
    def Registro(nombre,apellidos,sobrenombre, email, iden, fechaDeNacimiento, presupuesto):
        user = Usuario(nombre,apellidos,sobrenombre, email, iden, fechaDeNacimiento, presupuesto, True)
        return user

    @staticmethod
    def IngresoValido(iden):
            if (iden in Usuario.dictUsuariosID.keys()):
                return Usuario.dictUsuariosID[iden]
            else:
                return None

