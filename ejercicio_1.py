# ============================================================
# EJERCICIO 1: SRP - Single Responsibility Principle
# Cada clase tiene UNA sola responsabilidad
#SRP — Libro solo guarda datos. Las responsabilidades de persistir, mostrar y enviar se separaron en LibroRepositorio, LibroConsola y LibroEmailService.
# ============================================================

class Libro:
    """Solo almacena los datos del libro."""
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor


class LibroRepositorio:
    """Responsable de persistir el libro en archivo."""
    def guardar_en_archivo(self, libro: Libro, ruta: str = "libros.txt"):
        with open(ruta, "a", encoding="utf-8") as f:
            f.write(f"{libro.titulo} - {libro.autor}\n")
        print(f"Libro guardado en '{ruta}'.")


class LibroConsola:
    """Responsable de mostrar el libro en consola."""
    def imprimir(self, libro: Libro):
        print(f"{libro.titulo} - {libro.autor}")


class LibroEmailService:
    """Responsable de enviar el libro por email."""
    def enviar(self, libro: Libro, destinatario: str):
        # Aquí iría la lógica real de envío
        print(f"Enviando '{libro.titulo}' a {destinatario}...")

# --- Uso ---
if __name__ == "__main__":
    print("=" * 50)
    print("EJERCICIO 1: SRP")
    print("=" * 50)

    libro = Libro("Clean Code", "Robert C. Martin")

    consola = LibroConsola()
    consola.imprimir(libro)

    repositorio = LibroRepositorio()
    repositorio.guardar_en_archivo(libro)

    email_service = LibroEmailService()
    email_service.enviar(libro, "camsset@example.com")
