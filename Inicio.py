from time import sleep
from Usuario import Usuario
#from Comentario import Comentario
from Artista import Artista
from Articulo import Articulo
from Textos import Texto

def ValidarUsuario(usuario):
	if (usuario == "usuario" or usuario == "artista"):
		return True
	else:
		return False

def ValidarOpcion(numero,rango):
	if(numero > 0 and numero <= rango):
		return True
	else:
		return False
		

def MensajesInicio():
	print(Texto.mensajesMenuInicio["1"])
	print(Texto.mensajesMenuInicio["2"])
	print(Texto.mensajesMenuInicio["3"])

def MensajesArtista():
	print(Texto.mensajesMenuArtista["1"])
	print(Texto.mensajesMenuArtista["2"])
	print(Texto.mensajesMenuArtista["3"])
	print(Texto.mensajesMenuArtista["4"])
	print(Texto.mensajesAdvertencias["n"])

def MensajesComprador():
	pass

def MensajesAdaministrarArticulos():
	print(Texto.mensajesAdministracionArticulos["1"])
	print(Texto.mensajesAdministracionArticulos["2"])
	print(Texto.mensajesAdministracionArticulos["3"])
	print(Texto.mensajesAdministracionArticulos["4"])
	print(Texto.mensajesAdvertencias["n"])

def MensajesSocial():
	print(Texto.mensajesSocial["1"])
	print(Texto.mensajesSocial["2"])
	print(Texto.mensajesSocial["3"])
	print(Texto.mensajesAdvertencias["n"])

def MensajesReputacion():
	print(Texto.mensajesReputacion["1"])
	print(Texto.mensajesReputacion["2"])
	print(Texto.mensajesReputacion["3"])
	print(Texto.mensajesAdvertencias["n"])

def MensajesCompras():
	print(Texto.mensajesCompras["1"])
	print(Texto.mensajesCompras["2"])
	print(Texto.mensajesCompras["3"])
	print(Texto.mensajesAdvertencias["n"])

def MenuRegistro():
	rol = str(input(Texto.mensajesRegistro["rol"]))
	fin = True
	while(fin):
		if(ValidarUsuario(rol)):
			fin = False
		else:
			print(Texto.mensajesAdvertencias["usuarioInvalido"])
			rol = str(input())
	if rol == "artista":
		DatosRegistroArtista()
	elif rol == "usuario":
		DatosRegistro()
	print(" ")
	MensajesInicio()


def MenuValidacionIngreso():
	rol = str(input(Texto.mensajesRegistro["rol"]))
	fin = True
	while(fin):
		if(ValidarUsuario(rol)):
			fin = False
		else:
			print(Texto.mensajesAdvertencias["usuarioInvalido"])
			rol = str(input())
	if rol == "artista":
		user = DatosValidacion(rol)
		MenuArtista()
	else:
		user = DatosValidacion(rol)
		MenuComprador()

def MenuAdministrarArticulos():
	MensajesAdaministrarArticulos()
	opcion = str(input())
	while(opcion!="n"):
		if(opcion!="n"):
			print("not yet :V")
		opcion = str(input())
	MensajesArtista()

def MenuSocial():
	MensajesSocial()
	opcion = str(input())
	while(opcion !="n"):
		if(opcion !="n"):
			print("not yet :V")
		opcion = str(input())
	MensajesArtista()

def MenuReputacion():
	MensajesReputacion()
	opcion = str(input())
	while(opcion !="n"):
		if(opcion !="n"):
			print("not yet :V")
		opcion = str(input())
	MensajesArtista()

def MenuCompras():
	MensajesCompras()
	opcion = str(input())
	while(opcion !="n"):
		if(opcion !="n"):
			print("not yet :V")
		opcion = str(input())
	MensajesArtista()

def OpcionesMenuArtista(opcion):
	opciones = {"1":MenuAdministrarArticulos,
				"2":MenuSocial,
				"3":MenuReputacion,
				"4":MenuCompras}
	opciones[opcion]()

def MenuArtista():
	print(" ")
	MensajesArtista()
	opcion = str(input())
	while(opcion != "n"):
		OpcionesMenuArtista(opcion)
		opcion = str(input())
	MensajesInicio()

def OpcionesMenuComprador(opcion):
	opciones = {"1":MenuAdministrarArticulos,
				"2":MenuSocial,
				"3":MenuReputacion,
				"4":MenuCompras}
	opciones[opcion]()

def MenuComprador():
	print(" ")
	print("esta pasando por el menu del comprador")
	sleep(0.3)
	print(".")
	sleep(0.3)
	print(".")
	sleep(0.3)
	print(".")
	sleep(0.3)
	print(".")
	sleep(0.3)
	print(".")
	sleep(0.3)
	print(".")
	sleep(0.3)
	print(".")
	sleep(0.3)
	print(".")
	sleep(0.3)
	print("Salio del menu del comprador :V")
	MensajesInicio()

def OpcionesMenuInicial(opcion):
	opciones = {"1":MenuRegistro,
				"2":MenuValidacionIngreso}

	opciones[str(opcion)]()

def MenuInicial():
	fin = True
	print(Texto.mensajesMenuInicio["bienvenida"])
	MensajesInicio()
	while(fin):
		opcion = int(input())
		if opcion == 3:
			fin = False
		else:
			OpcionesMenuInicial(str(opcion))

def MenuAgregarComentario(usuario, articulo):
	descripcion = input(Texto.mensajesComentarios["descripcion"])
	puntuacion = input(Texto.mensajesComentarios["puntuacion"])
	Comentario.agregarCometarios(articulo, usuario, puntuacion, descripcion)

def MenuEditarComentario(comentario):
	opcion = input(Texto.mensajesComentarios["editC"])
	if(opcion == 1):
		puntuacion = input(Texto.mensajesComentarios["puntuacionN"])
		comentario.editarComentario(puntuacion)
	elif(opcion == 2):
		puntuacion = comentario.getPuntuacion()
		descripcion = input(Texto.mensajesComentarios["descripcionN"])
		comentario.editarComentario(puntuacion, descripcion)
	else:
		puntuacion = input(Texto.mensajesComentarios["puntuacionN"])
		descripcion = input(Texto.mensajesComentarios["descripcionN"])
		comentario.editarComentario(puntuacion, descripcion)

def DatosRegistro():
	print(Texto.mensajesRegistro["instruccionU"])
	nombres = (input(Texto.mensajesRegistro["nombre"]))
	apellidos = (input(Texto.mensajesRegistro["apellido"]))
	sobrenombre = (input(Texto.mensajesRegistro["sobrenombre"]))
	email = (input(Texto.mensajesRegistro["email"]))
	iden = (input(Texto.mensajesRegistro["id"]))
	fechaDeNacimiento = (input(Texto.mensajesRegistro["fdn"]))
	presupuesto = (int(input(Texto.mensajesRegistro["presupuesto"])))
	nuevoUsuario = Usuario.Registro(nombres,apellidos,sobrenombre,email,iden,fechaDeNacimiento,presupuesto)
	print(Texto.mensajesRegistro["registrocorrectoU"])
	return nuevoUsuario

def DatosRegistroArtista():
	usuarioActual = DatosRegistro()
	print(Texto.mensajesRegistro["instruccionA"])
	nombres = usuarioActual.getNombres()
	apellidos=usuarioActual.getApellidos()
	sobrenombre = usuarioActual.getSobrenombre()
	iden = usuarioActual.getId()
	email = usuarioActual.getEmail()
	fechaDeNacimiento = usuarioActual.getFechaDeNacimiento()
	presupuesto =usuarioActual.getPresupuesto()
	ocupacion = (input(Texto.mensajesRegistro["ocupacion"]))
	telefono = (input(Texto.mensajesRegistro["tel"]))
	nuevoArtista = Artista.RegistroArtista(nombres,apellidos,sobrenombre,
						email,iden,fechaDeNacimiento,
						presupuesto,ocupacion,telefono)
	print(Texto.mensajesRegistro["registrocorrectoA"])
	return nuevoArtista

def DatosValidacion(rol):
	while(True):
		iden = input(Texto.mensajesValidacion["id"])
		if(rol == "usuario"):
			user = Usuario.IngresoValido(iden)
			if isinstance(user , Usuario):
				print(Texto.mensajesValidacion["correcto"])
				return user
			else:
				print(Texto.mensajesValidacion["nousuario"])
		elif(rol == "artista"):
			user = Artista.IngresoValido(iden)
			if isinstance(user, Artista):
				print(Texto.mensajesValidacion["correcto"])
				return user
			else:
				print(Texto.mensajesValidacion["noartista"])











MenuInicial()


