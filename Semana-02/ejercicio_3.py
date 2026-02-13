# ============================================================
# EJERCICIO 3: LSP - Liskov Substitution Principle
# Las subclases deben poder reemplazar a su clase base
#  Los objetos de una superclase deben poder ser reemplazados por objetos de sus subclases sin afectar el funcionamiento del programa.
# ============================================================
from abc import ABC, abstractmethod

class Ave(ABC):
    """Clase base para todas las aves."""
    @abstractmethod
    def describir(self) -> str:
        pass


class AveVoladora(Ave):
    """Aves que pueden volar."""
    def volar(self):
        print(f"{self.describir()} está volando...")


class AveNoVoladora(Ave):
    """Aves que no vuelan pero pueden nadar u otras acciones."""
    def nadar(self):
        print(f"{self.describir()} está nadando...")


class Aguila(AveVoladora):
    def describir(self) -> str:
        return "Águila"

class Paloma(AveVoladora):
    def describir(self) -> str:
        return "Paloma"


class Pinguino(AveNoVoladora):
    """Pinguino NO hereda volar() — viola LSP si lo fuerza."""
    def describir(self) -> str:
        return "Pingüino"
    

# --- Uso ---
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("EJERCICIO 3: LSP")
    print("=" * 50)

    aves_voladoras: list[AveVoladora] = [Aguila(), Paloma()]
    for ave in aves_voladoras:
        ave.volar()  # Siempre funciona — LSP respetado

    pinguino = Pinguino()
    pinguino.nadar()  # Comportamiento apropiado para su tipo

