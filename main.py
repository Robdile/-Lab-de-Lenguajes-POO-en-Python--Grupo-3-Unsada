# TP Laboratorio de Lenguajes - Cliente de Correo - Grupo 3
 
class Contacto:
    def __init__(self, nombre : str, apellido : str, direccion_mail : str):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion_mail = direccion_mail

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.direccion_mail})"
    
class Correo:
    def __init__(self, remitente : str, destinatarios : list[Contacto], asunto : str, cuerpo : str):
        self.remitente = remitente
        self.destinatarios = destinatarios
        self.asunto = asunto
        self.cuerpo = cuerpo

class Cuenta:
    def __init__(self, nombre_usuario : str, direccion_mail : str, servidor_entrada : str, servidor_salida : str):
        self.nombre_usuario = nombre_usuario
        self.direccion_mail = direccion_mail
        self.servidor_entrada = servidor_entrada
        self.servidor_salida = servidor_salida

class ClienteDeCorreo:
    def __init__(self, cuenta):
        self.cuenta = cuenta