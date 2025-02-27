#Ejercicio 1: desarrollar un algoritmo que te permita ingresar 5 numeros y luego ordenarlos de menor a moyor.
nums=sorted(int(input(f"Numeros{i+1}: "))for i in range (5))
print(nums)


#Ejercicio 2: desarrolla un algoritmo en numpy que permita la multiplicacion de listas de 5 elementos.
import numpy as np

a = np.array([int(input(f"Ingrese el número {i+1}: ")) for i in range(5)])
b = np.array([int(input(f"Ingrese el número {i+1}: ")) for i in range(5)])

resultado = a * b

print(f"La respuesta de:{resultado}")


#Ejercicio 3: desarrolla un algoritmo que permita la multiplicacion de listas de 5 elementos sin numpy
a=[int(input(f"ingresge el numero {i+1} para A: "))for i in range(5)]
b=[int(input(f"ingresge el numero {i+1} para A: "))for i in range(5)]

resultado=[a[i]*b[i]for i in range(5)]

print(f"el resultado es: {resultado}")