# Autor: Daniel Alfonso Rojas Chávez, A01376572
# Descripcion: Calcular el porcentaje de estudiantes hombres y mujeres en una clase.

# Escribe tu programa después de esta línea.

m = int(input("Teclea el total de mujeres en la clase: "))
h = int(input("Teclea el total de hombres en la clase: "))

total = m+h
mujeres = m/total*100
hombres = h/total*100

print ("Total de alumnos: %d" % (total))
print ("Porcentaje de mujeres: %d%%" % (mujeres))
print ("Porcentaje de hombres: %d%%" % (hombres))

