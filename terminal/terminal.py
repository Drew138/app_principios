import requests
import os
import prettytable
import getpass
from controladores.controladorUsuario import ControladorUsuario
from controladores.controladorProducto import ControladorProducto
from controladores.controladorOrden import ControladorOrden


class Terminal:
    def __init__(self):
        self.controladorUsuario = ControladorUsuario()
        self.controladorProducto = ControladorProducto()
        self.controladorOrden = ControladorOrden()
        self.interfacesAbiertas = 1

    def realizarOrden(self):
        pass

    def mostrarInformacionVendedor(self):
        table1.fieldnames = ["nombre", "telefono", "direccion", "establecimiento"]
        table1.add_row([field for field in self.controladorProducto.getInformacionVendedor().values()])
        print(table1)
        table2 = prettytable()
        table2.fieldnames = ["Marca", "Producto", "Precio", "Disponibilidad"]
        for producto in self.controladorProducto.getProductos():
            table.add_row(producto)
        print(table2)

    def verificarDisponibilidadProducto(self):
        pass

    def verVendedores(self):
        self.controladorUsuario.obtenerVendedores()
        print(ControladorUsuario.vendedores)
        vendedor = input("Seleccione un vendedor: ")
        self.controladorProducto.setVendedor(vendedor)
        while not (self.controladorProducto.getVendedor() in self.controladorUsuario.vendedores):
            print("Vendedor inválido, seleccione de nuevo")
            print(ControladorUsuario.vendedores)
            vendedor = input("Seleccione un vendedor: ")
            self.controladorProducto.setVendedor(vendedor)
            for vend in self.controladorUsuario.getInformacionVendedores():
                if vend["establecimiento"] == vendedor:
                    self.controladorProducto.setInformacionVendedor(vend)
        accion = input(
            "Desea ver los productos ofrecidos por este Vendedor (Si/No): ").capitalize()
        if accion == "Si":
            self.controladorProducto.obtenerProductos()
            self.mostrarInformacionVendedor()
            accion = input("Desea agregar un nuevo producto a su órden(Si/No): ").capitalize()
            while accion == "Si":
                producto = input("Ingrese el producto que desea agregar")
                cantidad = input("Ingrese la cantidad que desea agregar de este producto")
                # TODO agregar actuador para verificar cantidades
                accion = input("Desea agregar un nuevo producto a su órden(Si/No): ").capitalize()


    def seleccionarAccionComprador(self):
        accion = input(
            "Desea ver vendedores, realizar una órden o salir (Vendedores/Orden/Salir): ").capitalize()
        acciones = {"Vendedores", "Orden", "Salir"}
        while not (accion in acciones):
            print("Accion invalida, vuelva a intentar")
            accion = input(
                "Desea ver vendedores, realizar una órden o salir (Vendedores/Orden/Salir): ").capitalize()
        if accion == 'Vendedores':
            self.verVendedores()
        elif accion == "Orden":
            self.realizarOrden()
        else:
            self.interfacesAbiertas = 0


    def verOrdenes(self):
        self.controladorOrden.verOrdenes()

    def mostrarInformacionComprador(self):
        table = prettytable()
        table.fieldnames = ["Marca", "Producto", "Precio", "Disponibilidad"]
        # TODO Mostrar información comprador
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
            "Desea ver sus órdenes, registrar productos, o salir (Ordenes/Registrar/Salir): ").capitalize()

        acciones = {"Registrar", "Ordenes", "Salir"}
        while not (accion in acciones):
            print("Acción inválida, vuelva a intentar")
            accion = input(
                "Desea ver sus órdenes, registrar productos, o salir (Ordenes/Registrar/Salir): ").capitalize()
        if accion == 'Ordenes':
            self.verOrdenes()
        elif accion == "Registrar":
            self.controladorPoductos.registrarProducto(self.controladorUsuario.getInformacionUsuario())
        else:
            self.interfacesAbiertas = 0

    def verificarInformacionUsuario(self):
        pass

    

    def comenzar(self):
        accion = input(
            "Desea ingresar o registrarse (Ingresar/Registrarse): ")
        accion = accion.capitalize()
        while accion != "Ingresar" and accion != "Registrarse":
            print("Acción inválida, intenta de nuevo")
            accion = input(
                "Desea ingresar o registrarse (Ingresar/Registrarse): ").capitalize()
        if accion == "Ingresar":
            self.controladorUsuario.autenticar()
        else:
            self.controladorUsuario.crearCuenta()

    def correr(self):
        self.comenzar()
        while self.interfacesAbiertas:
            if self.controladorUsuario.getInformacionUsuario()["tipo"] == 'comprador':
                self.seleccionarAccionComprador()
            elif self.controladorUsuario.getInformacionUsuario()["tipo"] == 'vendedor':
                self.seleccionarAccionVendedor()
        print("Se ha cerrado la aplicación")


def main():
    terminal = Terminal()
    terminal.correr()


if __name__ == "__main__":
    main()
