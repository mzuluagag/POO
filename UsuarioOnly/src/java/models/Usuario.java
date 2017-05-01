/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package models;

/**
 *
 * @author Sergio
 */
public class Usuario {
    private String nombres;
    private String apellidos;
    private String sobrenombre;
    private String email;
    private String id;
    private String fechaDeNacimiento;
    private int presupuesto;
    
    
    public Usuario(){
        
    }
    public Usuario(String nombres, String apellidos, String sobrenombre, String email, String id, String fechaDeNacimiento){
        this.nombres = nombres;
        this.apellidos = apellidos;
        this.sobrenombre = sobrenombre;
        this.email = email;
        this.id = id;
        this.fechaDeNacimiento = fechaDeNacimiento;
        this.presupuesto = 0;
        
    }
    public String getId(){
        return this.id;
    }
    public String getNombres(){
        return this.nombres;
    }
    public String getApellidos(){
        return this.apellidos;
    }
    public String getSobrenombre(){
        return this.sobrenombre;
    }
    public String getEmail(){
        return this.email;
    }
    public String getFechaDeNacimiento(){
        return this.fechaDeNacimiento;
    }
    public int getPresupuesto(){
        return this.presupuesto;
    }
}
