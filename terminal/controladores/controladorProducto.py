from .controlador import Controlador
import requests
import os


class ControladorProducto(Controlador):
    def __init__(self):
        super(Controlador).__init__()
        self.vendedor = None
        self.productos = []

    def setVendedor(self, vendedor):
        self.vendedor = vendedor

    def getVendedor(self):
        return self.vendedor

    def obtenerProductos(self):
        url = os.path.join(
            self.host,
            f"productos?vendedor={self.vendedor}",
        )
        response = requests.get(
            url,
            headers={'Authorization': f'Bearer {Controlador.getJWT()}'})
        self.productos = [response.content]
