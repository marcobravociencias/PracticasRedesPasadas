
class fichero:

	def __init__(self,usr,pas):
		self.usr = usr
		self.pas = pas

	def codifica(self,password):
		lista = list(password)		
		asci = [ord(a) for a in lista]
		asci = [num+5 for num in asci]
		return ''.join(chr(i) for i in asci)

	def arreglo(self,linea):
		x = linea.split()
		contra = x.pop()
		x.pop()#:
		x.pop()#Password
		usuario = x.pop()
		lista = list()		
		lista.append(contra)
		lista.append(usuario)
		return lista

	def login(self):
		f = open('input.txt','r')
		line = f.readline()
		while line!='':
			lista = self.arreglo(line) #Contrasena Usuario
			if self.usr==lista.pop():
				if self.codifica(self.pas)==lista.pop():
					return True
				else:
					return False
			line = f.readline()										
		f.seek(0) #Regresamos Apuntador
		f.close()
		return False

	def busca(self):
		f = open("input.txt")
		line = f.readline()
		while line!="":
			lista = self.arreglo(line) #contra Usuario
			if self.usr==lista.pop(): #Concidio con el Usuario		
				return False
			line = f.readline()
		self.agrega()
		f.seek(0)
		f.close()
		return True

	def agrega(self):
		f = open('input.txt','a')
		password = self.pas
		linea = '\nusername : '+self.usr+' password : '+self.codifica(password)
		f.write(linea)

	