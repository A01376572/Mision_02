# Autor: Daniel Alfonso Rojas Chávez, A01376572
# Descripcion: Calcular distancias y tiempos de recorridos en coche a partir de la velocidad.

# Escribe tu programa después de esta línea.
velocidad = int(input("Teclea la velocidad del auto:"))

distancia1 = float(velocidad*6)
distancia2 = float(velocidad*3.5)
tiempo = float(485/velocidad)

print ("En 6 horas recorre %.1f" % (distancia1),"km")
print ("En 3.5 horas recorre %.1f" % (distancia2),"km")
print ("Tiempo para recorrer 485km: %.1f" % (tiempo), "hrs")