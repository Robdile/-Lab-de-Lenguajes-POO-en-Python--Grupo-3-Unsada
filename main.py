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

def mostrar_menu_principal():
    print("\n" + "="*40)
    print("      SISTEMA DE CORREO UNSADA")
    print("="*40)
    print("1. Configurar Cuenta Única")
    print("2. Gestionar Agenda (Agregar Contacto)")
    print("3. Redactar y Enviar Correo")
    print("4. Simular Recepción de Correo")
    print("5. Bandeja de Salida (Ver Enviados)")
    print("6. Bandeja de Entrada (Ver Recibidos)")
    print("7. REPORTES / FUNCIONALIDADES")
    print("0. Salir")
    print("="*40)
    return input("Seleccione una opción: ")

def main():
    cliente = None 
    
    while True:
        opcion = mostrar_menu_principal()
        
        if not opcion.isdigit():
            print("\n>>> ERROR: Ingrese un número del 0 al 7.")
            continue

        if opcion == "1":
            if cliente is not None:
                print(f"\nAVISO: Ya existe la cuenta <{cliente.cuenta.direccion_mail}>.")
            else:
                user = input("Usuario: ")
                mail = ""
                while "@" not in mail:
                    mail = input("Email: ")
                    if "@" not in mail: print("Email inválido, intente de nuevo.")
                srv_in = input("Servidor Entrada: ")
                srv_out = input("Servidor Salida: ")
                cliente = ClienteDeCorreo(Cuenta(user, mail, srv_in, srv_out))
                print(">>> Cuenta configurada correctamente.")


        elif opcion == "2":
            if cliente:
                print("\n-- Nuevo Contacto --")
                m = input("Email: ")
                if "@" not in m:
                    print("Error: El mail debe contener '@'.")
                elif any(c.direccion_mail == m for c in cliente.contactos):
                    print(f"Error: El email {m} ya existe en la agenda.")
                else:
                    nom = input("Nombre: ")
                    ape = input("Apellido: ")
                    cliente.agregar_contacto(Contacto(nom, ape, m))
                    print(f"Contacto {nom} {ape} guardado.")
            else:
                print("\nDebe configurar la cuenta primero.")

        
        elif opcion == "3":
            if cliente:
                asunto = input("Asunto: ")
                msg = input("Mensaje: ")
                dest = input("Destinatario (Email): ")
                correo_nuevo = Correo(asunto, msg, cliente.cuenta.direccion_mail, [dest])
                cliente.enviar_correo(correo_nuevo)
                print(">>> Mensaje enviado.")
            else:
                print("\nConfigure la cuenta primero.")

        elif opcion == "4":
            if cliente:
                mail_in = Correo("Consulta TP", "Hola, te envío los modelos corregidos.", "juan@unsada.edu.ar", [cliente.cuenta.direccion_mail])
                cliente.agregar_correo_recibido(mail_in)
                print("\nSimulación: Nuevo correo en Recibidos.")
            else:
                print("\nConfigure la cuenta primero.")


        elif opcion == "6":
            if cliente:
                print("\n--- BANDEJA DE ENTRADA ---")
                if not cliente.correos_recibidos:
                    print("Sin mensajes.")
                else:
                    for i, mail in enumerate(cliente.correos_recibidos):
                        est = "Leído" if mail.esta_leido else "NUEVO"
                        print(f"{i+1}. [{est}] De: {mail.remitente} | Asunto: {mail.asunto}")
                        mail.marcar_como_leido()
            else:
                print("\nConfigure la cuenta primero.")

        elif opcion == "7":
            if cliente:
                print("\n" + "-"*35)
                print("      REPORTE DE ESTADO")
                print("-"*35)
                print(f"Total correos:    {cliente.cantidad_correos()}")
                print(f"Recibidos:       {cliente.cantidad_correos_recibidos()}")
                print(f"Enviados:        {cliente.cantidad_correos_enviados()}")
                print(f"Sin leer:        {cliente.cantidad_correos_no_leidos()}")
                print(f"Total contactos: {cliente.cantidad_contactos()}")
                print("-"*35)
            else:
                print("\nConfigure la cuenta primero para ver reportes.")
