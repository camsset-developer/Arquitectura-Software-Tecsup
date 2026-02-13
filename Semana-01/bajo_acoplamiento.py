from abc import ABC, abstractmethod


class MetodoPago(ABC):  # Equivalente a la interface de Java

    @abstractmethod
    def pagar(self):
        pass


class PagoTarjeta(MetodoPago):

    def pagar(self):
        print("Se realizó la compra con tarjeta")


class CompraService:

    def __init__(self, metodo_pago: MetodoPago):  # Inyección de dependencia
        self.metodo_pago = metodo_pago

    def realizar_compra(self):
        self.metodo_pago.pagar()
        print("Compra realizada")


# Main
pago = PagoTarjeta()
compra = CompraService(pago)
compra.realizar_compra()