from .controlador import Controlador


class ControladorProducto(Controlador):
    def __init__(self):
        super(Controlador).__init__()
        self.vendedor = None
        self.productos = []

    def setVendedor(self, vendedor):
        self.vendedor = vendedor

    def obtenerProductos(self):
        pass
