import requests
import os

class Terminal:
    def __init__(self):
        self.usuario = ""
        self.contraseña = ""
        self.jwt = ""
        self.vendedor = ""
        self.host = "http://127.0.0.1.8000"
        

    def autenticar(self):
       url = " "
       direccion = os.path.join(self.host,url) + "/"
       response = requests.post(self.host+)

    def enviarInformacion(self):
        pass

    def verVendedores(self):
        pass

    def verCompradores(self):
        pass

    def mostrarInformacionUsuario(self):
        pass

    def mostrarDisponibilidadProducto(self):
        pass

    def mostrarInformacionOrden(self):
        pass

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