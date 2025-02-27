# realizaralgoritmo de suma y multiplicacion de dos numeros
 
num1=int(input("ingrese el primer numero :"))
num2=int(input("ingrese el segundo numero :"))

suma= num1+num2
multiplicacion= num1*num2

print(f"la suma de {num1} y {num2} es: {suma}")
print(f"la multiplicacion de {num1} y {num2} es:{multiplicacion}")


#realizar un algoritmo que devuelva los numeros pares entre 10 y 50 

pares = list(range(10, 51, 2))
print(pares)


#realizar un algorito que devuelva los 20 primeros numeros primeros y que devuelva como una lista

def primo(n):
    if n <2:
        return False 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = []
num = 2

while len(primos) <20:
    if primo(num):
        primos.append(num)
    num += 1
    
print(primos)         