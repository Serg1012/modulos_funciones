def suma_numeros():
    numeros = []
    while True:
        try:
            entrada = input("Introduce un número (o 'q' para salir): ")
            if entrada.lower() == 'q':
                break
            numero = float(entrada)
            numeros.append(numero)
            if len(numeros) == 5:
                break
        except ValueError:
            print("Error: Introduce un número válido.")

    suma = sum(numeros)
    return suma

resultado = suma_numeros()
print(f"La suma de los números introducidos es: {resultado}")
