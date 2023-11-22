def obtener_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingresa un número válido.")

def numeros_pares_entre(inicial, final):
    return [num for num in range(inicial, final + 1) if num % 2 == 0]

if __name__ == "__main__":
    try:
        numero_inicial = obtener_numero("Ingresa el número inicial: ")
        numero_final = obtener_numero("Ingresa el número final: ")

        if numero_inicial > numero_final:
            raise ValueError("El número inicial no puede ser mayor que el número final.")

        lista_pares = numeros_pares_entre(numero_inicial, numero_final)

        if lista_pares:
            print(f"Lista de números pares entre {numero_inicial} y {numero_final}:")
            print(lista_pares)
        else:
            print(f"No hay números pares entre {numero_inicial} y {numero_final}.")

    except Exception as e:
        print(f"Error: {e}")
