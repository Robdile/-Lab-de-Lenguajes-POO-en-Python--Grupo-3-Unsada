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
    def __init__(self, nombre_usuario: str, direccion_mail: str, servidor_entrada: str, servidor_salida: str):
        self.nombre_usuario = nombre_usuario
        self.direccion_mail = direccion_mail
        self.servidor_entrada = servidor_entrada
        self.servidor_salida = servidor_salida

class ClienteDeCorreo:
    def __init__(self, cuenta):
        self.cuenta = cuenta
        self.contactos = []
        self.correos_recibidos = []
        self.correos_enviados = []

    # Métodos de conteo requeridos por la consigna
    def cantidad_contactos(self):
        return len(self.contactos)

    def cantidad_correos_recibidos(self):
        return len(self.correos_recibidos)

    def cantidad_correos_enviados(self):
        return len(self.correos_enviados)

    def cantidad_correos(self):
        return len(self.correos_recibidos) + len(self.correos_enviados)

    def cantidad_correos_no_leidos(self):
        return len([m for m in self.correos_recibidos if not m.esta_leido])
    # Métodos operativos
    def agregar_contacto(self, unContacto):
        self.contactos.append(unContacto)

    def agregar_correo_recibido(self, unCorreo):
        self.correos_recibidos.append(unCorreo)

    def enviar_correo(self, unCorreo):
        self.correos_enviados.append(unCorreo)


class ClienteDeCorreo:
    def __init__(self, cuenta):
        self.cuenta = cuenta
