import cherrypy
from banco1 import Banco
class Visualizar(object):
    def __init__(self):
        self.ver = Banco()
        self.ver.crear_cajero(5000,"Bochica")
        self.ver.lista_cajeros
        super
    
    # accedo a la carpeta views, archivo index.html
    @cherrypy.expose
    def index(self):
        return open('views/index.html')
       
    @cherrypy.expose
    def crear_cajero(self):
        print("crear cajero")
        return open('views/crear.html')

    @cherrypy.expose
    def cajero_nuevo(self, valor, nombre):
        self.ver.crear_cajero(valor,nombre)
        return "Se ha creado un nuevo cajero"

    @cherrypy.expose
    def listar_cajeros(self):
        return open('views/lista.html')
    
    @cherrypy.expose
    def listar(self):
        lista = ""
        for cajero in self.ver.lista_cajeros:
            lista += cajero.nombre 
        return lista 

if __name__== "__main__":
    cherrypy.quickstart(Visualizar())