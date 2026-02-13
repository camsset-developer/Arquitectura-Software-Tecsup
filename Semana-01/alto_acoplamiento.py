class PagoConTarjeta:

    def pagar(self):
        print("Se realizó la compra con tarjeta")


class CompraService:

    def __init__(self):
        self.pago = PagoConTarjeta()  # Dependencia concreta fija

    def realizar_compra(self):
        self.pago.pagar()
        print("Se realizó la compra")


# Main
compra = CompraService()
compra.realizar_compra()