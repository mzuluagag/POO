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
        self._obrasCompradas = dict()
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

    def getArticulosComprados(self):
        return self._obrasCompradas

    # -----------------------------------FUNCIONALIDADES----------------------------------------------
    def RecargarPresupuesto(self, recarga):
            self._presupuesto += recarga

    def RestarPresupuesto(self, resta):
            self._presupuesto -= resta

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

    @staticmethod
    def BuscarUsuarioNombre(nombre):
        related = dict()
        palabras = nombre.split(' ')
        for palabra in palabras:
            for i in Usuario.dictUsuariosID:
                if ((Usuario.dictUsuariosID[i].getNombres().find(palabra) >= 0 or
                    Usuario.dictUsuariosID[i].getSobrenombre().find(palabra) >= 0) and
                    not(i in related.keys())):
                        related[i] = Usuario.dictUsuariosID[i]
        return related

    @staticmethod
    def GenerarDatosFicticios():
        Usuario("Sergio","Arboleda","Checho","serg@gmail.com","1","Ayer",900)
        Usuario("Carlos","Torres","C4T0","carl@gmail.com","2","Hoy", 899)
        Usuario("Mateo","Zuluaga","M4T3","mat@gmail.com","3","Mañana",901)
