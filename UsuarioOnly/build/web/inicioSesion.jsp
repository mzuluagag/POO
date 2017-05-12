<%-- 
    Document   : inicioSesion
    Created on : 10-may-2017, 15:56:45
    Author     : ASUS
--%>
<%@include file="header.jsp" %>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <div class="container" align="center" STYLE= "background-color:#DAF7A6; margin-top: -2em" >
            <br>
            <div class="form" style="width:23%">
                <form method="POST" action="./login" >
                    E-mail: <input class="form-control" type="email" name="email" required><br> </br>
                    Identificación: <input class="form-control" type="password" name="id" required><br> </br>
                    <input class="btn btn-primary form-control" type="submit" value="Entrar" name="Confirmar">
                </form>
            </div>  
            <br>
        </div>
    </body>
    <%@include file="footer.jsp" %>
</html>
