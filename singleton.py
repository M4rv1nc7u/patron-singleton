# ==========================================
# 1. SINGLETON (Instancia única)
# ==========================================
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("[Singleton] Creando nueva conexión a la base de datos...")
            cls._instance = super().__new__(cls)
        return cls._instance


# ==========================================
# 2. DTO (Data Transfer Object)
# ==========================================
class UsuarioDTO:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email


# ==========================================
# 3. STRATEGY (Cambio de algoritmo/comportamiento)
# ==========================================
class PagoEfectivo:
    def pagar(self, monto):
        print(f"[Strategy] Pagando ${monto} en efectivo.")

class PagoTarjeta:
    def pagar(self, monto):
        print(f"[Strategy] Pagando ${monto} con tarjeta de crédito.")

class CarritoCompras:
    def __init__(self, estrategia_pago):
        self.estrategia_pago = estrategia_pago

    def procesar(self, monto):
        self.estrategia_pago.pagar(monto)


# ==========================================
# 4. FACTORY (Creación de objetos)
# ==========================================
class NotificacionEmail:
    def enviar(self, msg): print(f"[Factory] Email enviado: {msg}")

class NotificacionSMS:
    def enviar(self, msg): print(f"[Factory] SMS enviado: {msg}")

class NotificacionFactory:
    @staticmethod
    def crear_notificador(tipo):
        if tipo == "email":
            return NotificacionEmail()
        elif tipo == "sms":
            return NotificacionSMS()


# ==========================================
# 5. FACADE (Fachada simplificada)
# ==========================================
class SubsystemAudio:
    def encender(self): print("[Facade] Audio encendido.")

class SubsystemVideo:
    def encender(self): print("[Facade] Video encendido.")

class HomeTheaterFacade:
    def __init__(self):
        self.audio = SubsystemAudio()
        self.video = SubsystemVideo()

    def ver_pelicula(self):
        print("[Facade] Iniciando modo cine...")
        self.audio.encender()
        self.video.encender()


# ==========================================
# DEMO Y EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    print("=== 1. DEMO SINGLETON ===")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print("¿Es la misma instancia?:", db1 is db2)

    print("\n=== 2. DEMO DTO ===")
    user = UsuarioDTO(1, "Marvin", "marvin@example.com")
    print(f"DTO Datos: ID={user.id}, Nombre={user.nombre}")

    print("\n=== 3. DEMO STRATEGY ===")
    carrito = CarritoCompras(PagoTarjeta())
    carrito.procesar(150)

    print("\n=== 4. DEMO FACTORY ===")
    notificador = NotificacionFactory.crear_notificador("email")
    notificador.enviar("Hola desde el Factory")

    print("\n=== 5. DEMO FACADE ===")
    cine = HomeTheaterFacade()
    cine.ver_pelicula()