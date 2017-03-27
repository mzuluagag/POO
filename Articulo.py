class Comentario():
	listaComentarios = {}
	ID = 0

	def __init__(self, descripcion, puntuacion, articulo, usuario):
		self._descripcion = descripcion
		self._puntuacion = puntuacion
		self._articulo = articulo
		self._usuario = usuario
		self._id = Comentario.ID
		Comentario.listaComentarios[Comentario.ID] = self
		Comentario.ID += 1

	# --------------------------------SETTERS-----------------------------------

	def setDescripcion(self, descripcion):
		self._descripcion = descripcion

	def setPuntuacion(self, puntuacion):
		self._puntuacion = puntuacion

	def setArticulo(self, articulo):
		self._articulo = articulo

	def setUsuario(self, usuario):
		self._usuario = usuario

	# --------------------------------GETTERS------------------------------------

	def getDescripcion(self):
		return self._descripcion

	def getPuntuacion(self):
		return self._puntuacion

	def getArticulo(self):
		return self._articulo

	def getUsuario(self):
		return self._usuario

	def editarComentario(self, puntuacion, descripcion):
		self.setDescripcion(descripcion)
		self.setPuntuacion(puntuacion)

	def eliminarComentario(self, ID):
		comentario = Comentario.listaComentarios[ID]
		articulo = comentario.getArticulo()
		del articulo._comentarios[ID]
		del Comentario.listaComentarios[ID]

	# -----------------------------METODOS ESTÁTICOS --------------------------
	@staticmethod
	def agregarComentarios(articulo, usuario, puntuacion, descripcion):
		comentario = Comentario(descripcion, puntuacion, articulo, usuario)
		articulo.addComentario(comentario)
