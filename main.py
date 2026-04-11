# TP Laboratorio de Lenguajes - Cliente de Correo - Grupo 3
 
class Contacto:
    def __init__(self, nombre, apellido, direccion_mail):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion_mail = direccion_mail

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.direccion_mail})"
    
class Correo:
    pass

class Cuenta:
    def __init__(self, nombre_usuario, direccion_mail, servidor_entrada, servidor_salida):
        self.nombre_usuario = nombre_usuario
        self.direccion_mail = direccion_mail
        self.servidor_entrada = servidor_entrada
        self.servidor_salida = servidor_salida

class ClienteDeCorreo:
    def __init__(self, cuenta):
        self.cuenta = cuenta