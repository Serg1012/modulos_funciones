# main.py

from Actividad4 import Silla, Color

def main():
    try:
        silla_azul = Silla(color=Color.AZUL, precio=9.95)
        silla_roja = Silla(color=Color.ROJO, precio=9.95)

        print(f"Silla azul - Color: {silla_azul.color.value}, Precio: ${silla_azul.precio}")
        print(f"Silla roja - Color: {silla_roja.color.value}, Precio: ${silla_roja.precio}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
