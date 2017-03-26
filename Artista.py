from Usuario import Usuario
from Textos import Texto


class Artista(Usuario):
	dictArtistasID = {}
	dictArtistasEmail = {}

	def __init__(self, nombres, apellidos, sobrenombre, email, iden, fechaDeNacimiento, presupuesto, ocupacion,
				 telefono, fromRegister=False):
		super().__init__(nombres, apellidos, sobrenombre, email, iden, fechaDeNacimiento, presupuesto)
		self._ocupacion = None
		self._reputacion = None
		self._articulos = dict()
		self._telefono = None
		self._articulosVendidos = dict()
		self.setTelefono(telefono)
		self.setOcupacion(ocupacion)
		Artista.dictArtistasID[self._iden] = self
		Artista.dictArtistasEmail[self._email] = self

	# --------------------------------SETTERS---------------------------------------------

	def setOcupacion(self, ocupacion):
		self._ocupacion = ocupacion

	def setTelefono(self, telefono):
		self._telefono = telefono

	def addArticulo(self, articulo):
		self._articulos[articulo.getNombre()] = articulo

	def addArticuloVendido(self, articuloVendido):
		self._articulosVendidos[articuloVendido.getNombre()] = articuloVendido

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

	# --------------------------------------------------------------------------------------
	def info(self):
		return {self._nombres, self._apellidos,self._sobrenombre,
				self._email,self._iden, self._fechaDeNacimiento,
				self._presupuesto, self._ocupacion,self._telefono}
	
		def info(self):
		return {self._nombres, self._apellidos,self._sobrenombre,
				self._email,self._iden, self._fechaDeNacimiento,
				self._presupuesto, self._ocupacion,self._telefono}

	def CalcularReputacion(self):
		pass

	def ObtenerMejorArticulo(self):
		dictArticulos = self.getArticulos()
		max = 0
		nombre = None
		for i in dictArticulos:
			if (dictArticulos[i].getPuntuacion() > max):
				max = dictArticulos[i].getPuntuacion()
				nombre = dictArticulos[i].getNombre()
		return dictArticulos[nombre]

	def ObternerArticuloMasBarato(self):
		dictArticulos = self.getArticulos()
		min = 9999999999
		nombre = None
		for i in dictArticulos:
			if(dictArticulos[i].getPrecio() < min):
				min = dictArticulos[i].getPrecio()
				nombre = dictArticulos[i].getNombre()
		return dictArticulos[nombre]

	def ObtenerArticuloMasCaro(self):
		dictArticulos = self.getArticulos()
		max = 0
		nombre = None
		for i in dictArticulos:
			if(dictArticulos[i].getPrecio() > max):
				max = dictArticulos[i].getPrecio()
				nombre = dictArticulos[i].getNombre()
		return dictArticulos[nombre]

	def ObtenerArticulosDigitales(self):
		pass

	def ObtenerArticulosFisicos(self):
		pass

	# --------------------------------METODOSESTATICOS--------------------------------------

	@staticmethod
	def RegistroArtista(nombres, apellidos, sobrenombre,
						email, iden, fechaDeNacimiento,
						presupuesto, ocupacion, telefono):
		artista = Artista(nombres, apellidos, sobrenombre,
						  email, iden, fechaDeNacimiento,
						  presupuesto, ocupacion, telefono, True)
		return artista

	@staticmethod
	def IngresoValido(iden):
		if (iden in Artista.dictArtistasID.keys()):
			return Artista.dictArtistasID[iden]
		else:
			return None



