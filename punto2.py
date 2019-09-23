import numpy
import math

x=0.4
y=1.3
x1=numpy.array([0.4])
y1=numpy.array([1.3])

z1=x+y
z2=x1+y1

h1=numpy.cos(x)
h2=numpy.cos(x1)

g1=numpy.exp(1j*2*math.pi*x)
g2=numpy.exp(1j*2*math.pi*x1)

print "Resultados operaciones con enteros: "  ,z1
print "                                    "  ,h1
print "                                    "  ,g1
print "Resultados operaciones con vectores: " ,z2
print "                                    "  ,h2
print "                                    "  ,g2

