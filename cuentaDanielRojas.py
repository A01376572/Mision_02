# Autor: Daniel Alfonso Rojas Chávez, A01376572
# Calcular el IVA, la propina, y el total a partir del subtotal de una cuenta de comida.

# Escribe tu programa después de esta línea.

costo = float (input("Teclea el costo de la comida: "))

propina = costo*0.13
IVA = costo*0.16
total = costo + propina + IVA

print ("Propina: $%.2f" % (propina))
print ("IVA: $%.2f" % (IVA))
print ("Total: $%.2f" % (total))

