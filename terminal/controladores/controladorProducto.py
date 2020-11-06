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

    def setInformacionVendedor(self, informacionVendedor):
        self.informacionVendedor = informacionVendedor

    def obtenerProductos(self):
        url = ControladorProducto.host + f"/productos?vendedor={self.vendedor}",
        response = requests.get(
            url,
            headers={'Authorization': f'Bearer {Controlador.getJWT()}'})
        self.productos = [response.content] # TODO cambiar para remover vendedor asociado

    def getInformacionVendedor(self):
        return self.informacionVendedor

    def getProductos(self):
        return self.productos

    def registrarProducto(self, informacionUsuario):

        nombre = input("Ingrese el nombre de su producto: ")
        precio = input("Ingrese el precio del producto: ")
        marca = input("Ingrese la marca del producto: ")
        disponibilidad = input("Ingrese la cantidad de productos disponibles: ")
        try:
            assert type(nombre) is str
            assert type(precio) is int
            assert type(marca) is str
            assert type(disponibilidad) is int
        except Exception:
            self.registrarProducto()
        data = {
            "nombre":nombre, 
            "precio":precio, 
            "marca":marca, 
            "disponibilidad":disponibilidad,
            "vendedor": informacionUsuario 
            }
        headers = {"Authorization": f"Bearer {ControladorUsuario.getJWT()}"}
        url = ControladorProducto.host + "/productos/"
        response = request.post(url, headers=headers, data=data)
