class Texto():
	mensajesAdvertencias = {"usuarioInvalido": "Usuario incorrecto",
							"n": "n. Atras"}

	mensajesMenuInicio = {"bienvenida": "Bienvenidos a Desvararte",
						  "1": "1. Registrarse",
						  "2": "2. Ingresar",
						  "3": "3. Salir"}

	mensajesRegistro = {"instruccionU": "Esto es el registro para usuario, por favor ingrese los siguientes datos:",
						"instruccionA": "Se procederá ahora a llenar los datos adicionales para Artista",
						"aiden": "Ya existe un usuario con esa identificacion",
						"aemail": "El e-mail ingresado ya está registrado para otro usuario",
						"apresupuesto": "El valor del presupuesto no puede ser negativo",
						"registrocorrectoU": "Los datos se han registrado correctamente",
						"registrocorrectoA": "Se ha completado el registro del artista de forma satisfactoria",
						"nombre": "Nombres: ",
						"apellido": "Apellidos: ",
						"sobrenombre": "Sobrenombre: ",
						"email": "E-mail: ",
						"id": "ID: ",
						"ubic": "Ubicacion: ",
						"fdn": "Fecha de nacimiento en el siguiente formato: AAAA/MM/DD: ",
						"presupuesto": "Presupuesto: ",
						"ocupacion": "Ocupacion: ",
						"tel": "Telefono: ",
						"rol": "Ingrese su rol: "}

	mensajesValidacion = {"id": "Ingrese su identificacion: ",
						  "nousuario": "No se encontro ningun usuario con esa identificacion: ",
						  "noartista": "No se encontro ningun artista con esa identificacion: ",
						  "correcto":"Identificacion correcta"}

	mensajesMenuArtista = {"1": "1. Administrar obras",
						   "2": "2. Social",
						   "3": "3. Compras/Presupuesto"}

	mensajesAdministracionArticulos = {"1": "1. Publicar obra",
									   "2": "2. Eliminar obra",
									   "3": "3. Modificar obra",
									   "4": "4. Ver obras publicadas"}

	mensajesSocial = {"1": "1. Comentar obra",
					  "2": "2. Ver comentarios obra",
					  "3": "3. Buscar artistas",
					  "4": "4. Ver obras publicadas por artista"}

	mensajesReputacion = {"1": "1. Ver reputacion",
						  "2": "2. Ver puntuacion obra"}

	mensajesObras = {"instrucciones:": "Se pediran los datos pertinentes para registrar el articulo",
					 "errornombre": "Los datos son errones, puede que ya exista una obra con ese nombre",
					 "registrocorrecto": "El articulo se ha registrado correctamente",
					 "editcorrecto":"El articulo se editó correctamente",
					 "datos": "Datos actuales de la articulo",
					 "edit": "Ingrese los nuevos datos del articulo",
					 "aprecio": "El precio no puede ser negativo, ingrese un valor positivo.",
					 "anombre": "Ya existe un articulo con ese nombre, ingrese un nombre válido",
					 "elim": "Se eliminó el articulo satisfactoriamente",
					 "nopuedeedit": "No puede editar la obra, no es el dueño",
					 "nombre": "Nombre de la obra: ",
					 "precio": "Precio de la obra: ",
					 "tipo": "Tipo de obra: ",
					 "descripcion": "Añada una descripcion: ",
					 "puntuacion": "La puntuación promedio es: ",
					 "fdp": "La fecha de publicacion es: ",
					 "id":"ID de la obra: ",
					 "artista": "Artista: "}


	mensajesMCompras = {"1": "1. Comprar obra",
					    "2": "2. Recargar presupuesto",
					    "3": "3. Ver obras compradas"}


	mensajesComentarios = {"descripcion": "Escriba su comentario: ",
					   "puntuacion": "Que puntuacion le da a este articulo: ",
					   "editC": "Si desea editar puntuación oprima 1\nSi desea editar el contenido del comentario oprima 2\nSi desea editar ambos oprima 3\n",
					   "descripcionN": "agregue su nuevo comentario: ",
					   	"puntuacionN": "agregue su nueva puntuacion: ",
					   	"invalido": "Este usuario no puede realizar esta accion!",
					   	"buscarnombre": "Ingrese el nombre de la obra que desea comentar: ",
					   	"ingresarid": "Ingrese el ID de la obra que desea comentar: ",
						"user":"Usuario: ",
						"punt":"Puntuacion: ",
						"desc":"Descripcion: ",
					    "encontrados": "Obras encontradas: ",
						"buscarnombreV":"Ingrese el nombre de la obra: ",
						"ingresaridV":"Ingrese el id de la obra: "}

	mensajesBuscador = {"id": ", ID del artista:",
						"nombre": "Nombre del artista:",
						"sobrenombre": ", Sobrenombre del artista:",
						"1": "Ingrese el nombre o sobrenombre que desea buscar: ",
						"idb": "Ingrese el ID del artista: "}

	mensajesMenuUsuario = {"1": "1. Menu Social",
						   "2": "2. Menu compras"}

	mensajesCompras = {"buscar": "Ingrese el nombre de la obra que desea comprar: ",
					   "ide": "Ingrese el ID de la obra que desea comprar: ",
					   "comprado": "Operacion exitosa, gracias por usar Desvararte =D ;*",
					   "error": "Error, su presupuesto es insuficiente",
					   "saldo": "Presupuesto actual:",
					   "recarga": "Ingrese el saldo que desea recargar: ",
					   "errorRecarga": "Error, el saldo a recargar no puede ser negativo o nulo"}
