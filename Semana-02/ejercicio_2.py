# ============================================================
# EJERCICIO 2: OCP - Open/Closed Principle
# Abierto para extensión, cerrado para modificación
#Las entidades deben estar abiertas para extensión pero cerradas para modificación.
# ============================================================

from abc import ABC, abstractmethod


class Notificacion(ABC):
    """Interfaz base: no se modifica al agregar nuevos tipos."""
    @abstractmethod
    def enviar(self, mensaje: str):
        pass


class NotificacionSMS(Notificacion):
    def enviar(self, mensaje: str):
        print(f"[SMS] Enviando: {mensaje}")


class NotificacionEmail(Notificacion):
    def enviar(self, mensaje: str):
        print(f"[EMAIL] Enviando: {mensaje}")


# Nuevos tipos agregados SIN modificar la clase base
class NotificacionWhatsApp(Notificacion):
    def enviar(self, mensaje: str):
        print(f"[WHATSAPP] Enviando: {mensaje}")


class NotificacionPush(Notificacion):
    def enviar(self, mensaje: str):
        print(f"[PUSH] Enviando: {mensaje}")


class NotificadorServicio:
    """Orquesta el envío sin conocer el tipo concreto."""
    def __init__(self, canal: Notificacion):
        self.canal = canal

    def notificar(self, mensaje: str):
        self.canal.enviar(mensaje)

# --- Uso ---
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("EJERCICIO 2: OCP")
    print("=" * 50)

    canales = [
        NotificacionSMS(),
        NotificacionEmail(),
        NotificacionWhatsApp(),
        NotificacionPush(),
    ]

    for canal in canales:
        servicio = NotificadorServicio(canal)
        servicio.notificar("Tu análisis está listo.")