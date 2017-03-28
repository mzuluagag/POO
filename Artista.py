from Usuario import Usuario
from Textos import Texto
from Ordenar import mergeSort

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
		self._articulos[articulo._id] = articulo

	def addArticuloVendido(self, articuloVendido):
		self._articulosVendidos[articuloVendido._id] = articuloVendido

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

	def CalcularReputacion(self):
		articulos = self.getArticulos()
		suma = 0
		cantidad = 0
		for i in articulos:
			puntuacion = articulos[i].getPuntuacion()
			if(puntuacion != None):
				suma += puntuacion
		reputacion = suma




	def ObtenerMejorArticulo(self):
		dictArticulos = self.getArticulos()
		max = 0
		id = None
		for i in dictArticulos:
			if (dictArticulos[i].getPuntuacion() > max):
				max = dictArticulos[i].getPuntuacion()
				id = i
		return dictArticulos[id]

	def ObternerArticuloMasBarato(self):
		dictArticulos = self.getArticulos()
		min = 9999999999
		id = None
		for i in dictArticulos:
			if(dictArticulos[i].getPrecio() < min):
				min = dictArticulos[i].getPrecio()
				id = i
		return dictArticulos[id]

	def ObtenerArticuloMasCaro(self):
		dictArticulos = self.getArticulos()
		max = 0
		id = None
		for i in dictArticulos:
			if(dictArticulos[i].getPrecio() > max):
				max = dictArticulos[i].getPrecio()
				id = i
		return dictArticulos[id]

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

	@staticmethod
	def BuscarArtistaNombre(nombre):
		related = dict()
		palabras = nombre.split(' ')
		for palabra in palabras:
			for i in Artista.dictArtistasID:
				if ((palabra.find(Artista.dictArtistasID[i].getNombre()) >= 0 or
					palabra.find(Artista.dictArtistasID[i].getSobrenombre()) >= 0) and
					not(i in related.keys())):
						related[i] = Artista.dictArtistasID[i]
		return related

	@staticmethod
	def OrdenarPorReputacion():
		artistas = []
		for i in Artista.dictArtistasID:
			artistas.append(Artista.dictArtistasID[i])
		mergeSort(artistas)
		return artistas













