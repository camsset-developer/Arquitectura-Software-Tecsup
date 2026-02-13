# ============================================================
# EJERCICIO 4: ISP - Interface Segregation Principle
# Los clientes no deben depender de interfaces que no usan
# ============================================================
from abc import ABC, abstractmethod
class Arrancable(ABC):
    @abstractmethod
    def arrancar(self): pass

    @abstractmethod
    def detener(self): pass


class Conducible(ABC):
    @abstractmethod
    def conducir(self): pass

class Volador(ABC):
    @abstractmethod
    def volar(self): pass


class Navegable(ABC):
    @abstractmethod
    def navegar(self): pass


# Cada vehículo implementa solo lo que necesita
class Automovil(Arrancable, Conducible):
    def arrancar(self): print("Auto arrancando...")
    def detener(self): print("Auto detenido.")
    def conducir(self): print("Conduciendo por la carretera.")


class Avion(Arrancable, Conducible, Volador):
    def arrancar(self): print("Avión arrancando motores...")
    def detener(self): print("Avión detenido.")
    def conducir(self): print("Avión rodando en pista.")
    def volar(self): print("Avión volando a 10,000m.")


class Barco(Arrancable, Navegable):
    def arrancar(self): print("Barco encendiendo motores...")
    def detener(self): print("Barco anclado.")
    def navegar(self): print("Barco navegando en el mar.")

# --- Uso ---
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("EJERCICIO 4: ISP")
    print("=" * 50)

    auto = Automovil()
    auto.arrancar()
    auto.conducir()
    auto.detener()

    avion = Avion()
    avion.arrancar()
    avion.volar()

    barco = Barco()
    barco.arrancar()
    barco.navegar()