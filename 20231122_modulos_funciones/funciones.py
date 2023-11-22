#capítulo 10 - página 204

def sumar(i,j):
    return i+j
suma_anonima=lambda i,j:i+j
print(f"el total de la suma anonima con lambda es {suma_anonima}")
def sumar_default(i,j,k=15):
    return i+j+k

def sumar_variable(*args):
    total=0
    for i in args:
        total+=1
    return total

suma=sumar(4,5)
print(f"el total de la suma es {suma}")

suma2=sumar_default(4,5)
print(f"el total de la suma con argumentos default es {suma2}")

suma3=sumar_variable(5,9,4,7)
print(f"La suma total de una función con argumentos variable es {suma3}")

def factorial(n):
    if n==1:
        return n
    elif n<=0:
        print("No hay factorial para 0 o menor que 0")
    else:
        return n+factorial(n-1)

resultado_factorial=factorial(3)
print(f"el resultado es {factorial()}")