import sys
from usuario import Usuario
class ServidorCentral:
    
    def __init__(self):
        self.usuarios = list()
        
    def ping(self):
        return True
    
    def setUsuario(self,usr,ip):
        usr = Usuario(usr,ip)
        self.usuarios.append(usr)

    def getAll(self):
        cat = ''
        for m in self.usuarios:
           cat = cat +'\n'+m.getUsr()+'-'+m.getIp()+','
        return cat
       