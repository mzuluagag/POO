<%-- 
    Document   : mostrarUsuarios
    Created on : 01-may-2017, 13:52:25
    Author     : Sergio
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@include file="header.jsp" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="css/styles.css">
        <link rel="stylesheet" type="text/css" href="css/bootstrap.css">
        <link rel="stylesheet" type="text/css" href="css/bootstrap-theme.css">
        <title>Desvararte-Usuarios</title>
    </head>
    <div class="main">
    <body>
        <form method="POST" action="./dataSession">
            <input type="submit" value="Actualizar">
        </form>
        <h3>Lista de usuarios</h3>
        <c:if test="${!empty Usuarios}">
               <table class="tg">
                   <tr>
                    <th width="120">ID</th>
                    <th width="120">Nombre</th>
                    <th width="120">Apellidos</th>
                    <th width="120">Sobrenombre</th>
                    <th width="120">E-mail</th>
                    <th width="120">Fecha de nacimiento</th>
                    <th width="120">Presupuesto</th>
                </tr>
                   <c:forEach items="${Usuarios}" var="user">
                           <tr>
                               <td width="120"><a href="./buscarUsuario?id=${user.getId()}">${user.getId()}</a></td>
                               <td width="120">${user.getNombres()}</td>
                               <td width="120">${user.getApellidos()}</td>
                        <td width="120">${user.getSobrenombre()}</td>
                               <td width="120">${user.getEmail()}</td>
                               <td width="120">${user.getFechaDeNacimiento()}</td>
                               <td width="120">${user.getPresupuesto()}</td>
                           </tr>
                    </c:forEach>
            </table>
        </c:if>
        <form action="./index.jsp">
            <input type="submit" value="Inicio" />
        </form>    
    </body>
    </div>
</html>
<%@include file="footer.jsp" %>