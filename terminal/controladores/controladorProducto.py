from .controlador import Controlador
import requests
import os


class ControladorProducto(Controlador):
    def __init__(self):
        super(Controlador).__init__()
        self.vendedor = None
        self.informacionVendedor = None
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
        self.productos = [response.content] # TODO ver bien como recibe productos
        self.informacionVendedor = None # TODO cambiar a inf vendedor

    def getInformacionVendedor(self):
        return self.informacionVendedor

    def getProductos(self):
        return self.productos
