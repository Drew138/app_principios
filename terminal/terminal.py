import requests
import os
from prettytable import PrettyTable
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
        self.controladorOrden.realizarOrden()



    def mostrarInformacionVendedor(self):
        table1 = PrettyTable()
        table1.field_names = ["nombre", "telefono","tipo" ,"establecimiento", "direccion"]
        table1.add_row([field for field in self.controladorProducto.getInformacionVendedor().values()])
        print("Informacion de vendedor asociado")
        print(table1)
        table2 = PrettyTable()
        if not self.controladorProducto.getProductos():
            print("No hay productos disponibles")
        table2.field_names = ["Nombre", "Marca", "Precio", "Disponibilidad"]
        for producto in self.controladorProducto.getProductos():
            table2.add_row([field for field in producto.values()])
        print("Informacion de productos ofrecidos por este vendedor")
        print(table2)

    def verificarDisponibilidadProducto(self, producto, cantidad):
        existeProducto = False
        hayDisponibilidad = False
        for prod in self.controladorProducto.getInformacionProductos():
            if prod["nombre"] == producto:
                existeProducto = True
            if existeProducto:
                hayDisponibilidad = cantidad <= prod["disponibilidad"]
                break
        if not existeProducto:
            print("El producto seleccionado no existe")
        if not hayDisponibilidad:
            print("No hay las cantidades suficientes para satisfacer la órden")
        return existeProducto and hayDisponibilidad

    def verVendedores(self):
        self.controladorUsuario.obtenerVendedores()
        self.mostrarVendedores()
        vendedor = input("Seleccione un vendedor (Nombre de Establecimiento): ")
        self.controladorProducto.setVendedor(vendedor)
        for vend in self.controladorUsuario.getInformacionVendedores():
                if vend["establecimiento"] == vendedor:
                    self.controladorProducto.setInformacionVendedor(vend)
                    break
        while not (self.controladorProducto.getVendedor() in self.controladorUsuario.vendedores):
            print("Vendedor inválido, seleccione de nuevo")
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
            accion = input("Desea agregar un nuevo producto a su órden (Si/No): ").capitalize()
            while accion == "Si":
                producto = input("Ingrese el producto que desea agregar: ")
                cantidad = input("Ingrese la cantidad que desea agregar de este producto: ")
                cantidad = int(cantidad)
                if not self.verificarDisponibilidadProducto(producto, cantidad):
                    continue
                else:
                    for prod in self.controladorProducto.getInformacionProductos():
                        if prod["nombre"] == producto:
                            nuevoProducto = {
                                "costo": (prod["precio"] * cantidad),
                                "cantidad": cantidad,
                                "completado": False,
                                "producto": prod["nombre"]
                            }
                            self.controladorOrden.agregarProducto(nuevoProducto)
                            break
                print(self.controladorOrden.orden)
                accion = input("Desea agregar un nuevo producto a su órden (Si/No): ").capitalize()


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
        self.controladorOrden.obtenerOrdenes()
        self.mostrarInformacionOrden()

    def mostrarInformacionComprador(self):
        table = PrettyTable()
        table.field_names = ["Marca", "Producto", "Precio", "Disponibilidad"]
        # TODO Mostrar información comprador
        print(table)

    def mostrarVendedores(self):
        table = PrettyTable()
        table.field_names = ["nombre", "telefono","tipo" ,"establecimiento", "direccion"]
        for vendedor in self.controladorUsuario.getInformacionVendedores():
            if vendedor:
                table.add_row([field for field in vendedor.values()])
        print(table)


    def mostrarDisponibilidadProducto(self):
        table = PrettyTable()
        table.field_names = ["Marca", "Producto", "Precio", "Disponibilidad"]
        # TODO Hacer solicitud de productos
        print(table)

    def mostrarInformacionOrden(self):
        table = PrettyTable()
        table.field_names = ["Comprador","Costos", "Cantidades", "Productos", "Vendedor"]
        for orden in self.controladorOrden.orden:
            if table:
                table.add_row([field for field in orden.values()])
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
            self.controladorProducto.registrarProducto()
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
            if self.controladorUsuario.autenticar() == "no":
                self.interfacesAbiertas = 0
        else:
            if self.controladorUsuario.crearCuenta() == "no":
                self.interfacesAbiertas = 0

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
