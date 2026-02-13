class BajaCohesion:

    def procesar_compra(self):
        total = self.__calcular_total(2, 50.0)
        print(f"Procesando compra por S/ {total}")

        if total > 80:
            print("Aplica descuento")
        else:
            print("No aplica descuento")

    def __calcular_total(self, cantidad: int, precio: float) -> float:
        return cantidad * precio


# Main
compra = BajaCohesion()
compra.procesar_compra()