# ============================================================
# EJERCICIO 5: DIP - Dependency Inversion Principle
# Depender de abstracciones, no de implementaciones concretas
# ============================================================
from abc import ABC, abstractmethod
class GeneradorReporte(ABC):
    """Abstracción de la que depende ReporteService."""
    @abstractmethod
    def crear(self, contenido: str):
        pass


class PDFGenerator(GeneradorReporte):
    def crear(self, contenido: str):
        print(f"[PDF] Generando reporte: {contenido}")


class ExcelGenerator(GeneradorReporte):
    def crear(self, contenido: str):
        print(f"[EXCEL] Generando reporte: {contenido}")


class WordGenerator(GeneradorReporte):
    def crear(self, contenido: str):
        print(f"[WORD] Generando reporte: {contenido}")

class ReporteService:
    """
    Depende de la abstracción GeneradorReporte,
    no de ninguna implementación concreta.
    El generador se inyecta desde fuera (Dependency Injection).
    """
    def __init__(self, generador: GeneradorReporte):
        self.generador = generador

    def generar(self, contenido: str):
        self.generador.crear(contenido)

# --- Uso ---
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("EJERCICIO 5: DIP")
    print("=" * 50)

    contenido = "Resultados análisis ICP-MS - Febrero 2026"

    for generador in [PDFGenerator(), ExcelGenerator(), WordGenerator()]:
        servicio = ReporteService(generador)
        servicio.generar(contenido)