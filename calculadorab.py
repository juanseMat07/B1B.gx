class Calculadorab:
	def __init__(self, x, y):
		self.x=x
		self.y=y
	
	def suma(self):
	    return self.x + self.y

	def resta(self):
	    return self.x - self.y

	def multiplicacion(self):
	    return self.x * self.y

	def division(self):
	    return self.x / self.y

x=input('Ingrese el numero: ')
y=input('Ingrese el numero: ')
r=Calculadorab(x,y)
	
print "1.Suma"
print "2.Resta"
print "3.Multiplicacion"
print "4.Division"
op=input('Seleccione la operacion a realizar: ')

if op==1:
	print "Resultado= ",(r.suma())
elif op==2:
	print "Resultado= ",(r.resta())
elif op==3:
	print "Resultado= ",(r.multiplicacion())
elif op==4:
	print "Resultado= ",(r.division())
else:
	print "Seleccion no valida"
