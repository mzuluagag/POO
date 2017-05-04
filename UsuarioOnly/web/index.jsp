<%-- 
    Document   : index
    Created on : 30-abr-2017, 17:38:37
    Author     : Sergio
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@include file="header.jsp" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        
        <link rel="stylesheet" type="text/css" href="css/bootstrap.css">
        <link rel="stylesheet" type="text/css" href="css/bootstrap-theme.css">
        <title>Desvararte</title>
    </head>
    <div class="container" ALIGN="center" STYLE= "background-color:#DAF7A6">
    <body>
        <br/>
        <form  action="./registerUsuario.jsp" >
            <button class="btn btn-block btn-lg btn-danger" type="submit" style='width:200px' >Registro</button><br/><br/>
        </form>
        <form  action="./buscarUsuario.jsp" >
            <input class="btn btn-block btn-lg btn-danger" type="submit" value="Buscar usuarios" style='width:200px' /><br/><br/>
        </form>
        <form  action="./mostrarUsuarios.jsp" >
            <input class="btn btn-block btn-lg btn-danger" type="submit" value="Mostrar usuarios" style='width:200px'/><br/><br/>
        </form> 
    </body>
    </div>
</html>
<%@include file="footer.jsp" %>