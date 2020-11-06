from .controlador import Controlador
import requests
import os
import json

class ControladorOrden(Controlador):

    def __init__(self):
        super(Controlador).__init__()
        self.vendedor = ""
        self.orden = []

    def seleccionarVendedor(self, vendedor):
        self.vendedor = vendedor
        self.productos = {}

    def agregarProducto(self, producto):
        self.orden.append(producto)

    def realizarOrden(self):
        url = ControladorOrden.host + "/orden/"
        for ords in orden:
            response = requests.post(
                url,
                headers={'Authorization': f'Bearer {Controlador.getJWT()}'}, data=ords)
            if reponse.status_code != 201:
                print("Error al enviar orden")

    def obtenerOrdenes(self):
        url = ControladorOrden.host + "/api/ordenes"
        response = requests.get(
            url,
            headers={'Authorization': f'Bearer {Controlador.getJWT()}'})
        response_dict = json.loads(response.text)
        self.orden = response_dict
