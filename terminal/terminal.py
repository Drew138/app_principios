import requests
import os
import prettytable
import getpass
from .controladores.controladorUsuario import ControladorUsuario
from .controladores.controladorProducto import ControladorProducto
from .controladores.controladorOrden import ControladorOrden


class Terminal:
    def __init__(self):
        self.controladorUsuario = ControladorUsuario()
        self.controladorProducto = ControladorProducto(self.controladorUsuario)
        self.controladorOrden = ControladorOrden(self.controladorProducto)
        self.interfacesAbiertas = 1

    def realizarOrden(self):
        pass

    def verVendedores(self):
        self.controladorUsuario.obtenerVendedores()
        print(ControladorUsuario.vendedores)
        vendedor = input("Seleccione un vendedor: ")
        self.controladorProducto.setVendedor(vendedor)
        while self.controladorProducto.getVendedor() not in self.controladorUsuario.vendedores:
            print("Vendedor invalido, seleccione de nuevo")
            print(ControladorUsuario.vendedores)
            self.controladorProducto.setVendedor(vendedor)
        accion = input(
            "Desea ver los productos ofrecidos por este Vendedor (Si/No): ").capitalize()
        if accion == "Si":
            self.controladorProducto.obtenerProductos()
            self.mostrarInformacionVendedor()

    def seleccionarAccionComprador(self):
        accion = input(
            "Desea ver vendedores, realizar su orden o salir (Vendedores/Orden/Salir): ").capitalize()
        while (accion != 'Vendedores') or (accion != 'Orden') or (accion != 'Salir'):
            print("Accion invalida, vuelva a intentar")
            accion = input(
                "Desea ver vendedores, realizar su orden o salir (Vendedores/Orden/Salir): ").capitalize()
        if accion == 'Vendedores':
            self.verVendedores()
        elif accion == "Orden":
            self.realizarOrden()
        else:
            self.interfacesAbiertas = 0

    def verOrdenes(self):
        pass

    def mostrarInformacionComprador(self):
        table = prettytable()
        table.fieldnames = ["Marca", "Producto", "Precio", "Disponibilidad"]
        # TODO Mostrar información comprador
        print(table)

    def mostrarInformacionVendedor(self):
        table = prettytable()
        table.fieldnames = ["Marca", "Producto", "Precio", "Disponibilidad"]
        # TODO Mostrar información vendedor
        print(table)

    def mostrarDisponibilidadProducto(self):
        table = prettytable()
        table.fieldnames = ["Marca", "Producto", "Precio", "Disponibilidad"]
        # TODO Hacer solicitud de productos
        print(table)

    def mostrarInformacionOrden(self):
        table = prettytable()
        table.fieldnames = ["Productos", "Cantidades", "Costos"]
        # TODO Mostrar información de órden
        print(table)

    def seleccionarAccionVendedor(self):
        accion = input(
            "Desea ver sus ordenes, o salir (Ordenes/Salir): ").capitalize()
        while (accion != 'Orden') or (accion != 'Salir'):
            print("Accion invalida, vuelva a intentar")
            accion = input(
                "Desea ver sus ordenes, o salir (Ordenes/Salir): ").capitalize()
        if accion == 'Ordenes':
            self.verOrdenes()
        else:
            self.interfacesAbiertas = 0

    def verificarInformacionUsurio(self):
        pass

    def verificarDisponibilidadProducto(self):
        pass

    def comenzar(self):
        accion = input(
            "Desea ingresar o registrarse (Ingresar/Registrarse): ").capitalize()
        while accion != "Ingresar" and accion != "Registrarse":
            print("Accion invalida, intenta de nuevo")
            accion = input(
                "Desea ingresar o registrarse (Ingresar/Registrarse): ").capitalize()
        if accion == "Ingresar":
            self.controladorUsuario.autenticar()
        else:
            self.controladorUsuario.crearCuenta()

    def correr(self):
        self.comenzar()
        while self.interfacesAbiertas:
            if self.informacionUsuario['tipo'] == 'Comprador':
                self.seleccionarAccionComprador()
            elif self.informacionUsuario['tipo'] == 'Vendedor':
                self.seleccionarAccionVendedor()
        print("Se ha cerrado la aplicacion")


def main():
    terminal = Terminal()
    terminal.correr()


if __name__ == "__main__":
    main()
