# muebles.py

from enum import Enum

class Color(Enum):
    AZUL = "Azul"
    ROJO = "Rojo"
    VERDE = "Verde"
    AMARILLO = "Amarillo"
    # Puedes agregar más colores según sea necesario

class Mueble:
    def __init__(self, color, precio):
        self.color = color
        self.precio = precio

class Mesa(Mueble):
    pass

class Silla(Mueble):
    pass

class Lampara(Mueble):
    pass
