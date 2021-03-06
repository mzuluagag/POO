from Usuario import Usuario
from Comentario import Comentario
from Artista import Artista
from Articulo import Articulo
from Textos import Texto

Usuario.GenerarDatosFicticios()
Artista.GenerarDatosFicticios()
Articulo.GenerarDatosFicticios()


def ValidarUsuario(usuario):
    if (usuario == "usuario" or usuario == "artista"):
        return True
    else:
        return False


def ValidarOpcion(numero, rango):
    if (numero > 0 and numero <= rango):
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
    print(Texto.mensajesAdvertencias["n"])


def MensajesUsuario():
    print(Texto.mensajesMenuUsuario["1"])
    print(Texto.mensajesMenuUsuario["2"])
    print(Texto.mensajesAdvertencias["n"])


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
    print(Texto.mensajesSocial["4"])
    print(Texto.mensajesSocial["5"])
    print(Texto.mensajesAdvertencias["n"])


def MensajesReputacion():
    print(Texto.mensajesReputacion["1"])
    print(Texto.mensajesReputacion["2"])
    print(Texto.mensajesAdvertencias["n"])


def MensajesCompras():
    print(Texto.mensajesMCompras["1"])
    print(Texto.mensajesMCompras["2"])
    print(Texto.mensajesMCompras["3"])
    print(Texto.mensajesAdvertencias["n"])


def MenuRegistro():
    rol = str(input(Texto.mensajesRegistro["rol"]))
    fin = True
    while (fin):
        if (ValidarUsuario(rol)):
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
    while (fin):
        if (ValidarUsuario(rol)):
            fin = False
        else:
            print(Texto.mensajesAdvertencias["usuarioInvalido"])
            rol = str(input())
    if rol == "artista":
        user = DatosValidacion(rol)
        MenuArtista(user)
    else:
        user = DatosValidacion(rol)
        MenuComprador(user)


def MenuAdministrarArticulos(artista):
    MensajesAdaministrarArticulos()
    opcion = str(input())
    while (opcion != "n"):
        OpcionesMenuArticulos(opcion, artista)
        MensajesAdaministrarArticulos()
        opcion = str(input())


def OpcionesMenuArticulos(opcion, artista):
    opciones = {"1": DatosRegistroArticulo,
                "2": MenuElimArticulo,
                "3": MenuEdicionArticulo,
                "4": VerArticulosPublicados}
    opciones[opcion](artista)


def MenuSocial(artista):
    MensajesSocial()
    opcion = str(input())
    while (opcion != "n"):
        OpcionesMenuSocial(opcion, artista)
        MensajesSocial()
        opcion = str(input())


def OpcionesMenuSocial(opcion, artista):
    opciones = {"1": ComentarObra,
                "2": VerComentariosObra,
                "3": BuscarArtista,
                "4": VerArticulosPublicadosArtista,
                "5": MenuReputacion}
    opciones[opcion](artista)


def OpcionesMenuCompras(opcion, artista):
    opciones = {"1": ComprarObra,
                "2": RecargarPresupuesto,
                "3": VerObrasCompradas}
    opciones[opcion](artista)


def MenuCompras(artista):
    MensajesCompras()
    opcion = str(input())
    while (opcion != "n"):
        OpcionesMenuCompras(opcion, artista)
        MensajesCompras()
        opcion = str(input())


def OpcionesMenuArtista(opcion, artista):
    opciones = {"1": MenuAdministrarArticulos,
                "2": MenuSocial,
                "3": MenuCompras}
    opciones[opcion](artista)


def MenuArtista(artista):
    print(" ")
    MensajesArtista()
    opcion = str(input())
    while (opcion != "n"):
        OpcionesMenuArtista(opcion, artista)
        MensajesArtista()
        opcion = str(input())
    MensajesInicio()


def OpcionesMenuUsuario(opcion, usuario):
    opciones = {"1": MenuSocial,
                "2": MenuCompras}
    opciones[opcion](usuario)


def MenuComprador(usuario):
    print(" ")
    MensajesUsuario()
    opcion = str(input())
    while (opcion != "n"):
        OpcionesMenuUsuario(opcion, usuario)
        MensajesUsuario()
        opcion = str(input())
    MensajesInicio()


def OpcionesMenuInicial(opcion):
    opciones = {"1": MenuRegistro,
                "2": MenuValidacionIngreso}

    opciones[(opcion)]()


def MenuInicial():
    fin = True
    print(Texto.mensajesMenuInicio["bienvenida"])
    MensajesInicio()
    while (fin):
        opcion = str(input())
        if opcion == "3":
            fin = False
        else:
            OpcionesMenuInicial(str(opcion))


def MenuEliminarComentario(comentario, usuario):
    if (usuario == comentario.getUsuario()):
        ID = comentario.getID()
        comentario.EliminarComentario(ID)
    else:
        print(Texto.mensajesComentarios["invalido"])


def MenuAgregarComentario(usuario, articulo):
    descripcion = input(Texto.mensajesComentarios["descripcion"])
    puntuacion = input(Texto.mensajesComentarios["puntuacion"])
    Comentario.AgregarComentarios(articulo, usuario, puntuacion, descripcion)


def MenuEditarComentario(comentario):
    opcion = input(Texto.mensajesComentarios["editC"])
    if (opcion == 1):
        descripcion = comentario.getDescripcion()
        puntuacion = input(Texto.mensajesComentarios["puntuacionN"])
        comentario.EditarComentario(puntuacion, descripcion)
    elif (opcion == 2):
        puntuacion = comentario.getPuntuacion()
        descripcion = input(Texto.mensajesComentarios["descripcionN"])
        comentario.EditarComentario(puntuacion, descripcion)
    elif (opcion == 3):
        puntuacion = input(Texto.mensajesComentarios["puntuacionN"])
        descripcion = input(Texto.mensajesComentarios["descripcionN"])
        comentario.EditarComentario(puntuacion, descripcion)
    else:
        usuario = comentario.getUsuario()
        ID = comentario.getID()
        MenuEliminarComentario(comentario, usuario, ID)


def DatosRegistro():
    print(Texto.mensajesRegistro["instruccionU"])
    nombres = (input(Texto.mensajesRegistro["nombre"]))
    apellidos = (input(Texto.mensajesRegistro["apellido"]))
    sobrenombre = (input(Texto.mensajesRegistro["sobrenombre"]))
    email = (input(Texto.mensajesRegistro["email"]))
    iden = (input(Texto.mensajesRegistro["id"]))
    fechaDeNacimiento = (input(Texto.mensajesRegistro["fdn"]))
    presupuesto = (int(input(Texto.mensajesRegistro["presupuesto"])))
    nuevoUsuario = Usuario.Registro(nombres, apellidos, sobrenombre, email, iden, fechaDeNacimiento, presupuesto)
    print(Texto.mensajesRegistro["registrocorrectoU"])
    return nuevoUsuario


def DatosRegistroArtista():
    usuarioActual = DatosRegistro()
    print(Texto.mensajesRegistro["instruccionA"])
    nombres = usuarioActual.getNombres()
    apellidos = usuarioActual.getApellidos()
    sobrenombre = usuarioActual.getSobrenombre()
    iden = usuarioActual.getId()
    email = usuarioActual.getEmail()
    fechaDeNacimiento = usuarioActual.getFechaDeNacimiento()
    presupuesto = usuarioActual.getPresupuesto()
    ocupacion = (input(Texto.mensajesRegistro["ocupacion"]))
    telefono = (input(Texto.mensajesRegistro["tel"]))
    nuevoArtista = Artista.RegistroArtista(nombres, apellidos, sobrenombre,
                                           email, iden, fechaDeNacimiento,
                                           presupuesto, ocupacion, telefono)
    print(Texto.mensajesRegistro["registrocorrectoA"])
    return nuevoArtista


def DatosValidacion(rol):
    while (True):
        iden = input(Texto.mensajesValidacion["id"])
        if (rol == "usuario"):
            user = Usuario.IngresoValido(iden)
            if isinstance(user, Usuario):
                print(Texto.mensajesValidacion["correcto"])
                return user
            else:
                print(Texto.mensajesValidacion["nousuario"])
        elif (rol == "artista"):
            user = Artista.IngresoValido(iden)
            if isinstance(user, Artista):
                print(Texto.mensajesValidacion["correcto"])
                return user
            else:
                print(Texto.mensajesValidacion["noartista"])


def DatosRegistroArticulo(artista):
    print(Texto.mensajesObras["instrucciones:"])
    nombre = (input(Texto.mensajesObras["nombre"]))
    precio = (int(input(Texto.mensajesObras["precio"])))
    tipo = (input(Texto.mensajesObras["tipo"]))
    descripcion = (input(Texto.mensajesObras["descripcion"]))
    nuevoArticulo = Articulo.AgregarArticulo(nombre, precio, artista, tipo, descripcion)
    print(Texto.mensajesObras["registrocorrecto"])
    return nuevoArticulo


def MenuEdicionArticulo(artista):
    iden = input(Texto.mensajesObras["id"])
    articulo = Articulo.dictArticulos[iden]
    print(Texto.mensajesObras["datos"])
    for i in articulo.info():
        print(i)
    print(Texto.mensajesObras["edit"])
    nombre = (input(Texto.mensajesObras["nombre"]))
    precio = (int(input(Texto.mensajesObras["precio"])))
    tipo = (input(Texto.mensajesObras["tipo"]))
    descripcion = (input(Texto.mensajesObras["descripcion"]))
    if (articulo.EditarArticulo(artista, nombre, precio, tipo, descripcion)):
        print(Texto.mensajesObras["editcorrecto"])
    else:
        print(Texto.mensajesObras["nopuedeedit"])


def MenuElimArticulo(artista):
    id = input(Texto.mensajesObras["id"])
    articulo = Articulo.dictArticulos[id]
    if articulo.EliminarArticulo(artista):
        print(Texto.mensajesObras["elim"])
    else:
        print(Texto.mensajesObras["nopuedeedit"])


def VerArticulosPublicados(artista):
    articulos = artista.getArticulos()
    for i in articulos:
        print(
            Texto.mensajesObras["nombre"] + " " + articulos[i].getNombre() + " " + Texto.mensajesObras["id"] + " " + i)


def BuscarArtista(artista):
    nombre = str(input(Texto.mensajesBuscador["1"]))
    resultados = Artista.BuscarArtistaNombre(nombre)
    for clave in resultados:
        print(Texto.mensajesBuscador["nombre"], resultados[clave].getNombres(), Texto.mensajesBuscador["sobrenombre"],
              resultados[clave].getSobrenombre(), Texto.mensajesBuscador["id"], clave)


def VerArticulosPublicadosArtista(artista):
    artista = Artista.dictArtistasID[str(input(Texto.mensajesBuscador["idb"]))]
    VerArticulosPublicados(artista)


def ComentarObra(artista):
    nombre = str(input(Texto.mensajesComentarios["buscarnombre"]))
    opciones = Articulo.BuscarArticulo(nombre)
    print(Texto.mensajesComentarios["encontrados"])
    for clave in opciones:
        print(Texto.mensajesObras["nombre"], opciones[clave].getNombre(), ",", Texto.mensajesObras["id"], clave)
    eleccion = str(input(Texto.mensajesComentarios["ingresarid"]))
    MenuAgregarComentario(artista, opciones[eleccion])


def VerComentariosObra(usuario):
    nombre = str(input(Texto.mensajesComentarios["buscarnombreV"]))
    opciones = Articulo.BuscarArticulo(nombre)
    print(Texto.mensajesComentarios["encontrados"])
    for clave in opciones:
        print(Texto.mensajesObras["nombre"], opciones[clave].getNombre(), Texto.mensajesObras["id"], clave)
    eleccion = str(input(Texto.mensajesComentarios["ingresaridV"]))
    comentarios = opciones[eleccion].getComentarios()
    for idcomentario in comentarios:
        nombreUsuario = comentarios[idcomentario].getUsuario().getNombres()
        descripcion = comentarios[idcomentario].getDescripcion()
        puntuacion = comentarios[idcomentario].getPuntuacion()
        print(Texto.mensajesComentarios["user"] + " " + nombreUsuario)
        print(Texto.mensajesComentarios["punt"] + " " + puntuacion)
        print(Texto.mensajesComentarios["desc"] + " " + descripcion)


def ComprarObra(artista):
    nombre = str(input(Texto.mensajesCompras["buscar"]))
    opciones = Articulo.BuscarArticulo(nombre)
    print(Texto.mensajesComentarios["encontrados"])
    for clave in opciones:
        if opciones[clave].getEstado:
            print(Texto.mensajesObras["nombre"], opciones[clave].getNombre(), Texto.mensajesObras["precio"],
                  opciones[clave].getPrecio(), Texto.mensajesObras["id"], clave)
    eleccion = str(input(Texto.mensajesCompras["ide"]))
    if (opciones[eleccion].ComprarArticulo(artista)):
        print(Texto.mensajesCompras["comprado"])
        print(Texto.mensajesCompras["saldo"], artista.getPresupuesto())
    else:
        print(Texto.mensajesCompras["error"])
        print(Texto.mensajesCompras["saldo"], artista.getPresupuesto())


def RecargarPresupuesto(artista):
    recarga = int(input(Texto.mensajesCompras["recarga"]))
    if recarga > 0:
        artista.RecargarPresupuesto(recarga)
        print(Texto.mensajesCompras["saldo"], artista.getPresupuesto())
    else:
        print(Texto.mensajesCompras["errorRecarga"])


def VerObrasCompradas(artista):
    obras = artista.getArticulosComprados()
    for clave in obras:
        print(
            Texto.mensajesObras["nombre"] + str(obras[clave].getNombre()) + ", " + Texto.mensajesObras["precio"] + str(
                obras[clave].getPrecio()))


def MenuReputacion(artista):
    MensajesReputacion()
    opcion = str(input())
    while (opcion != "n"):
        OpcionesMenuReputacion(opcion)
        MensajesReputacion()
        opcion = str(input())


def OpcionesMenuReputacion(opcion):
    opciones = {"1": RankingReputacion,
                "2": RankingPuntuacion}
    opciones[opcion]()


def RankingReputacion():
    artistas = Artista.OrdenarPorReputacion()
    rank = 1
    print(Texto.mensajesReputacion["rankr"])
    for artista in artistas:
        nombre = artista.getNombres() + " " + artista.getApellidos()
        reputacion = artista.getReputacion()
        sobrenombre = artista.getSobrenombre()
        print(Texto.mensajesReputacion["r"] + " " + str(rank) + " " +
              Texto.mensajesReputacion["rep"] + " " + str(reputacion) + " " +
              Texto.mensajesReputacion["nombres"] + " " + nombre + " " +
              Texto.mensajesReputacion["sobrenombre"] + " " + sobrenombre)
        rank += 1


def RankingPuntuacion():
    articulos = Articulo.OrdenarPorPuntuacion()
    rank = 1
    print(Texto.mensajesReputacion["rankp"])
    for articulo in articulos:
        nombre = articulo.getNombre()
        puntuacion = articulo.getPuntuacion()
        print(Texto.mensajesReputacion["r"] + " " + str(rank) + " " +
              Texto.mensajesReputacion["punt"] + " " + str(puntuacion) + " " +
              Texto.mensajesReputacion["nombres"] + " " + nombre)
        rank += 1


MenuInicial()
