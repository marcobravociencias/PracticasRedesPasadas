from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from usuario import Usuario 
import sys


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class funcionesServidorGeneral():
    def __init__(self):
        self.usuarios = list()
        self.ipEntrante = 'NO'
    
#Ponemos la ip del usuario que quiere conectarse.
    def setMiIp(self,ipEntrante): 
        self.ipEntrante = ipEntrante
    def getTuIp(self):
        return self.ipEntrante        

    def setUsuario(self,usr,ip):
        usr = Usuario(usr,ip)
        self.usuarios.append(usr)
    
    def removeUsuario(self,ip1):
        for m in self.usuarios[:]:
           if(ip1==m.getIp()):
                self.usuarios.remove(m)

    def getAll(self):
        cat = ''
        for m in self.usuarios:
           cat = cat +'\n'+m.getUsr()+'-'+m.getIp()+','
        return cat        


#Obtenemos la ip donde vamos a iniciar el servidor
ip = str(sys.argv[1])
#Elegimos un puerto por defecto
puerto = 8001

server = SimpleXMLRPCServer((ip, puerto),requestHandler=RequestHandler,allow_none=True)
server.register_introspection_functions()
server.register_instance(funcionesServidorGeneral())
try:
    print 'Escuchando en '+ip+ ' En el puerto '+str(puerto)
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'         
