# Autor: Daniel Alfonso Rojas Chávez, A01376572
# Descripcion: Calcular la distancia entre dos puntos en un plano.

# Escribe tu programa después de esta línea.

x1 = float(input("Teclea la coordenada x del punto 1: "))
y1 = float(input("Teclea la coordenada y del punto 1: "))
x2 = float(input("Teclea la coordenada x del punto 2: "))
y2 = float(input("Teclea la coordenada y del punto 2: "))

distancia =((x2-x1)**2+(y2-y1)**2)**(1/2)

print ("La distancia entre el punto 1 y el punto 2 es %.3f" % (distancia))