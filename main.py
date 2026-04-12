# TP Laboratorio de Lenguajes - Cliente de Correo - Grupo 3
 
class Contacto:
    def __init__(self, nombre: str, apellido: str, direccion_mail: str):
        self.nombre = nombre
        self.apellido = apellido
        # Validación de Roberto: El mail debe ser válido para crearse
        if "@" in direccion_mail:
            self.direccion_mail = direccion_mail
        else:
            self.direccion_mail = "Email Invalido"

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.direccion_mail})"
    
class Correo:
    def __init__(self, asunto: str, cuerpo: str, remitente: str, destinatarios: list):
        self.asunto = asunto
        self.cuerpo = cuerpo
        self.remitente = remitente
        # Aseguramos que destinatarios sea siempre una lista
        self.destinatarios = destinatarios if isinstance(destinatarios, list) else [destinatarios]
        self.esta_leido = False

    def marcar_como_leido(self):
        self.esta_leido = True

class Cuenta:
    def __init__(self, nombre_usuario : str, direccion_mail : str, servidor_entrada : str, servidor_salida : str):
        self.nombre_usuario = nombre_usuario
        self.direccion_mail = direccion_mail
        self.servidor_entrada = servidor_entrada
        self.servidor_salida = servidor_salida

class ClienteDeCorreo:
    def __init__(self, cuenta):
        self.cuenta = cuenta
