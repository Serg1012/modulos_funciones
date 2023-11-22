from datetime import datetime

def calcular_subtotal(unidades, precio):
    try:
        unidades = int(unidades)
        precio = float(precio)
        subtotal = unidades * precio
        return subtotal
    except ValueError:
        print("Error: Introduce valores numéricos válidos.")
        return None

def calcular_descuento(subtotal):
    today = datetime.today().day
    if today < 15:
        descuento = 0.05 * subtotal
        return descuento
    else:
        return 0

def calcular_total(subtotal, descuento):
    total = subtotal - descuento
    return total

def main():
    try:
        unidades = input("Introduce la cantidad de unidades: ")
        precio = input("Introduce el precio por unidad: ")

        subtotal = calcular_subtotal(unidades, precio)
        if subtotal is not None:
            descuento = calcular_descuento(subtotal)
            total = calcular_total(subtotal, descuento)

            print(f"\nSubtotal: {subtotal:.2f}")
            print(f"Descuento aplicado: {descuento:.2f}")
            print(f"Total a pagar: {total:.2f}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
