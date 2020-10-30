import requests
import os
import prettytable
import getpass


class Terminal:
    def __init__(self):
        self.usuario = ""
        self.contraseña = ""
        self.refresh = ""
        self.jwt = ""
        self.informacionUsuario = {}
        self.vendedor = ""
        self.host = "http://127.0.0.1.8000"
        self.interfacesAbiertas = 1

    def setContraseña(self, contraseña):
        self.contraseña = contraseña

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setJWT(self, jwt):
        self.jwt = jwt

    def setRefresh(self, refresh):
        self.refresh = refresh

    def setInformacionUsuario(self, informacionUsuario):
        self.informacionUsuario = informacionUsuario

    def crearCuenta(self):
        username = input("Nombre de usuario: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        segundaContraseña = getpass.getpass("Ingrese su contraseña de nuevo: ")
        while contraseña != segundaContraseña:
            print("Las contraseñas no coinciden, intente de nuevo")
            contraseña = getpass.getpass("Ingrese su contraseña: ")
            segundaContraseña = getpass.getpass(
                "Ingrese su contraseña de nuevo: ")
        telefono = input("Ingrese su telefono: ")
        direccion = input("Ingrese su direccion: ")
        tipo = input("Ingrese su tipo de usuario (Comprador/Vendedor): ")
        while tipo != "Comprador" and tipo != "Vendedor":
            tipo = input("Ingrese su tipo de usuario (Comprador/Vendedor): ")
        direccion = os.path.join(self.host, 'api/auth/register/')
        user = {"username": username,
                "password": contraseña,
                "telefono": telefono,
                "direccion": direccion,
                "tipo": tipo, }
        if tipo == "Vendedor":
            establecimiento = input("Ingrese el nombre de su establecimiento")
            user["establecimiento"] = establecimiento
        response = requests.post(direccion, user)
        if response.status_code == 201:
            print(response.reason)
            accion = input("Desea volver a intentarlo (Si/No): ")
            while accion != 'Si' and accion != 'No':
                print("Accion invalida, Intente de nuevo")
                accion = input("Desea volver a intentarlo (Si/No): ")
            if accion == "Si":
                self.crearCuenta()
            else:
                self.terminar()

    def autenticar(self):
        usuario = input("Ingrese su usuario: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        self.setUsuario(usuario)
        self.setContraseña(contraseña)
        credenciales = {"username": self.usuario, "password": self.contraseña}
        url = "api/auth/login/"
        direccion = os.path.join(self.host, url)
        response = requests.post(direccion, credenciales)
        self.setJWT(response['access'])
        self.setRefresh(response['refresh'])
        self.setInformacionUsuario(response['user'])

    def refrescarJWT(self):
        url = 'api/auth/refresh'
        direccion = os.path.join(self.host, url)
        headers = {"Authorization": f"Bearer {self.refresh}"}
        response = requests.post(direccion, headers=headers)
        self.setJWT(response['access'])
        self.setRefresh(response['refresh'])

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

    def verificarEstadoOrden(self):
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
            self.autenticar()
        else:
            self.crearCuenta()
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
