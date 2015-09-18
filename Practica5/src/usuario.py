import sys

class Usuario:
    
    def __init__(self,usr,ip):
        self.usr = usr
        self.ip = ip
        
    def getUsr(self):
        return str(self.usr)
    
    def getIp(self):
        return str(self.ip)        