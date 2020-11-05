from .controlador import Controlador
import requests
import os


class ControladorOrden(Controlador):

    def __init__(self):
        super(Controlador).__init__()
        self.vendedor = ""
        self.orden = {}

    def seleccionarVendedor(self, vendedor):
        self.vendedor = vendedor
        self.productos = {}

    def agregarProducto(self, producto, cantidad):
        self.productos[producto] = cantidad

    def realizarOrden(self):
        url = os.path.join(
            self.host,
            f"orden/",
        )
        response = requests.post(
            url,
            headers={'Authorization': f'Bearer {Controlador.getJWT()}'})
        response.content

    def verOrdenes(self):
        url = os.path.join(
            self.host,
            f"orden/",
        )
        response = requests.get(
            url,
            headers={'Authorization': f'Bearer {Controlador.getJWT()}'})
        self.orden = [response.content]
