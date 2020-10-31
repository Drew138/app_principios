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

    def enviarInformacion(self):
        pass

    def verVendedores(self):
        pass

    def verCompradores(self):
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

    def verificarInformacionUsurio(self):
        pass

    def verificarDisponibilidadProducto(self):
        pass

    def realizarOrden(self):
        pass

    def terminar(self):
        self.interfacesAbiertas -= 1

    def comenzar(self):
        accion = input("Desea ingresar o registrarse (Ingresar/Registrarse): ")
        while accion != "Ingresar" and accion != "Registrarse":
            print("Accion invalida, intenta de nuevo")
            accion = input(
                "Desea ingresar o registrarse (Ingresar/Registrarse): ")
        if accion == "Ingresar":
            self.usuario.autenticar()
        else:
            self.usuarios.crearCuenta()
        while self.interfacesAbiertas:
            if self.informacionUsuario['tipo'] == 'Comprador':
                pass
            elif self.informacionUsuario['tipo'] == 'Vendedor':
                pass
        print("Se ha cerrado la aplicacion")


def main():
    terminal = Terminal()
    terminal.comenzar()


if __name__ == "__main__":
    main()
