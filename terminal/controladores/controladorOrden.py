from .controlador import Controlador
import requests


class ControladorOrden(Controlador):

    def __init__(self):
        super(Controlador).__init__()
        self.vendedor = ""
        self.productos = {}

    def seleccionarVendedor(self, vendedor):
        self.vendedor = vendedor
        self.productos = {}

    def agregarProducto(self, producto, cantidad):
        pass

    def realizarOrden(self):
        pass

    def verEstadoOrden(self):
        pass

    def verOrdenes(self):
        pass
