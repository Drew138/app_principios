import requests
import os
import prettytable
import getpass

class Terminal:
    def __init__(self):
        self.usuario = ""
        self.contraseña = ""
        self.jwt = ""
        self.vendedor = ""
        self.host = "http://127.0.0.1.8000"
        
    def setContraseña(self, contaseña):
        self.contraseña = contraseña

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setJWT(self, jwt):
        self.jwt = jwt

    def autenticar(self):
        usuario = input("Ingrese su usuario: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        self.setUsuario(usuario)
        self.setContraseña(contraseña)
        credenciales = {"username": self.usuario, "password": self.contraseña}
        url = " "
        direccion = os.path.join(self.host,url) + "/"
        response = requests.post(direccion, credenciales) 

    def enviarInformacion(self):
        pass

    def verVendedores(self):
        pass

    def verCompradores(self):
        pass

    def mostrarInformacionComprador(self):
        table = prettytable()
        table.fieldnames= ["Marca", "Producto", "Precio", "Disponibilidad"]
        # TODO Mostrar información comprador 
        print(table)

    def mostrarInformacionVendedor(self):
        table = prettytable()
        table.fieldnames= ["Marca", "Producto", "Precio", "Disponibilidad"]
        # TODO Mostrar información vendedor 
        print(table)


    def mostrarDisponibilidadProducto(self):
        table = prettytable()
        table.fieldnames= ["Marca", "Producto", "Precio", "Disponibilidad"]
        # TODO Hacer solicitud de productos
        print(table)
        

    def mostrarInformacionOrden(self):
        table = prettytable()
        table.fieldnames= ["Productos", "Cantidades", "Costos"]
        # TODO Mostrar información de órden
        print(table)

    def verificarInformacionUsurio(self):
        pass

    def verificarDisponibilidadProducto(self):
        pass

    def realizarOrden(self):
        pass

    def verificarEstadoOrden(self):
        pass

    def terminal(self):
        pass





def main():
    terminal = Terminal()
    terminal.comenzar()
 

if __name__ == "__main__":
    main()