# TP Laboratorio de Lenguajes - Cliente de Correo - Grupo 3
 
class Contacto:
    def __init__(self, nombre, apellido, direccion_mail):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion_mail = direccion_mail

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.direccion_mail})"
    
class Correo:
    def __init__(self, asunto, mensaje, remitente, destinatarios):
        self.asunto = asunto
        self.mensaje = mensaje
        self.remitente = remitente
        # Roberto sugirió asegurar que destinatarios sea siempre una lista
        if isinstance(destinatarios, list):
            self.destinatarios = destinatarios
        else:
            self.destinatarios = [destinatarios]
        
        # Por defecto, un correo nuevo no está leído 
        self.leido = False

    def marcar_como_leido(self):
        """Cambia el estado del correo a leído."""
        self.leido = True

    def __str__(self):
        estado = "Leído" if self.leido else "No leído"
        return f"Asunto: {self.asunto} | De: {self.remitente} | Estado: {estado}"

class Cuenta:
    def __init__(self, nombre_usuario, direccion_mail, servidor_entrada, servidor_salida):
        self.nombre_usuario = nombre_usuario
        self.direccion_mail = direccion_mail
        self.servidor_entrada = servidor_entrada
        self.servidor_salida = servidor_salida

class ClienteDeCorreo:
    def __init__(self, cuenta):
        # El cliente administra una sola cuenta [cite: 325]
        self.cuenta = cuenta
        # Carpetas para organizar mensajes [cite: 326]
        self.recibidos = []
        self.enviados = []
        # Agenda de contactos [cite: 325]
        self.agenda = []

    # --- Métodos Operativos ---
    def agregar_contacto(self, unContacto):
        """Simula incorporar un nuevo contacto a la agenda[cite: 344]."""
        self.agenda.append(unContacto)

    def agregar_correo_recibido(self, unCorreo):
        """Simula la recepción de un correo en la carpeta de recibidos[cite: 339, 340]."""
        self.recibidos.append(unCorreo)

    def enviar_correo(self, unCorreo):
        """Simula el envío de un correo agregándolo a "enviados"[cite: 342, 343]."""
        self.enviados.append(unCorreo)

    # --- Métodos de Conteo (Reportes) ---
    def cantidad_contactos(self):
        """Retorna la cantidad total de contactos[cite: 338]."""
        return len(self.agenda)

    def cantidad_correos_recibidos(self):
        """Retorna la cantidad total de correos recibidos[cite: 335]."""
        return len(self.recibidos)

    def cantidad_correos_enviados(self):
        """Retorna la cantidad total de correos enviados[cite: 336]."""
        return len(self.enviados)

    def cantidad_correos(self):
        """Retorna la cantidad total (recibidos + enviados)[cite: 334]."""
        return len(self.recibidos) + len(self.enviados)

    def cantidad_correos_no_leidos(self):
        """Retorna el total de correos no leídos de la carpeta recibidos[cite: 337]."""
        contador = 0
        for correo in self.recibidos:
            if not correo.leido:
                contador += 1
        return contador