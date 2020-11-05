import requests
import getpass
import os
from .controlador import Controlador


class ControladorUsuario(Controlador):

    def __init__(self):
        super(Controlador).__init__()
        self.usuario = ""
        self.contraseña = ""
        self.informacionUsuario = {}
        self.vendedores = []

    def setContraseña(self, contraseña):
        self.contraseña = contraseña

    def setUsuario(self, usuario):
        self.usuario = usuario

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
        if response.status_code != 201:
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
        Controlador.setJWT(response['access'])
        Controlador.setRefresh(response['refresh'])
        self.setInformacionUsuario(response['user'])

    def refrescarJWT(self):
        url = 'api/auth/refresh'
        direccion = os.path.join(self.host, url)
        headers = {"Authorization": f"Bearer {Controlador.getRefresh()}"}
        response = requests.post(direccion, headers=headers)
        Controlador.setJWT(response['access'])
        Controlador.setRefresh(response['refresh'])

    def obtenerVendedores(self):
        url = os.path.join(
            self.host,
            f"usuarios",
        )
        response = requests.get(
            url,
            headers={'Authorization': f'Bearer {Controlador.getJWT()}'})
        self.vendedores = [response.content]
