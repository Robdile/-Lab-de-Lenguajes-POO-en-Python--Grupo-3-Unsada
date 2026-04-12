# =================================================================
# TP Laboratorio de Lenguajes - Cliente de Correo - Grupo 3
# UNSAdA - Sede Arrecifes
# =================================================================

class Contacto(object):
    def __init__(self, nombre, apellido, direccion_mail):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion_mail = direccion_mail

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.direccion_mail})"

class Cuenta(object):
    def __init__(self, nombre_usuario, direccion_mail, servidor_entrada, servidor_salida):
        self.nombre_usuario = nombre_usuario
        self.direccion_mail = direccion_mail
        self.servidor_entrada = servidor_entrada
        self.servidor_salida = servidor_salida

class Correo(object):
    def __init__(self, asunto, mensaje, remitente, destinatarios):
        self.asunto = asunto
        self.mensaje = mensaje
        self.remitente = remitente
        if isinstance(destinatarios, list):
            self.destinatarios = destinatarios
        else:
            self.destinatarios = [destinatarios]
        self.leido = False

    def marcar_como_leido(self):
        self.leido = True

class ClienteDeCorreo(object):
    def __init__(self, cuenta):
        self.cuenta = cuenta
        self.recibidos = []
        self.enviados = []
        self.agenda = []

    def agregar_contacto(self, unContacto):
        self.agenda.append(unContacto)

    def agregar_correo_recibido(self, unCorreo):
        self.recibidos.append(unCorreo)

    def enviar_correo(self, unCorreo):
        self.enviados.append(unCorreo)

    def cantidad_contactos(self):
        return len(self.agenda)

    def cantidad_correos_recibidos(self):
        return len(self.recibidos)

    def cantidad_correos_enviados(self):
        return len(self.enviados)

    def cantidad_correos(self):
        return len(self.recibidos) + len(self.enviados)

    def cantidad_correos_no_leidos(self):
        return len([m for m in self.recibidos if not m.leido])

# --- SCRIPT DE PRUEBA ---
if __name__ == "__main__":
    # Creamos la configuración inicial
    mi_cuenta = Cuenta("JuanG", "juan.dan@unsada.edu.ar", "pop.unsada.edu.ar", "smtp.unsada.edu.ar")
    cliente = ClienteDeCorreo(mi_cuenta)
    
    # Carga de un contacto
    c1 = Contacto("Eros", "Perez", "eros@email.com")
    cliente.agregar_contacto(c1)
    
    # Simulamos un correo recibido (no leído)
    m_recibido = Correo("Aviso", "Hola Juan, este es un mail de prueba.", "roberto@email.com", [mi_cuenta.direccion_mail])
    cliente.agregar_correo_recibido(m_recibido)
    
    # Informe por consola
    print(f"--- Sistema de Correo de {mi_cuenta.nombre_usuario} ---")
    print(f"Total de correos: {cliente.cantidad_correos()}")
    print(f"Correos sin leer: {cliente.cantidad_correos_no_leidos()}")