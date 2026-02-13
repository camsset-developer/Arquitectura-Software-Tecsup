class CalcularTotal:

    def calcular_total(self, cantidad: int, precio: float) -> float:
        return cantidad * precio


class PagoService:

    def procesar_compra(self, total: float):
        print(f"Procesando compra por S/ {total}")


class ValidarCompra:

    def validar(self, total: float):
        if total > 80:
            print("Aplica descuento")
        else:
            print("No aplica descuento")


class AltaCohesion:

    def procesar_compra(self):
        calculadora = CalcularTotal()
        pago_service = PagoService()
        validador = ValidarCompra()

        total = calculadora.calcular_total(2, 50.0)
        pago_service.procesar_compra(total)
        validador.validar(total)


# Main
compra = AltaCohesion()
compra.procesar_compra()