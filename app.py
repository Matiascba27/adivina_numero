import random

def crear_juego():
    """Genera un nuevo juego y devuelve el estado inicial."""
    
    return random.randint(1, 100) # Genera un número aleatorio entre 1 y 100 como el número a adivinar


def adivinar(numero, estado):
    """

    Compara el número adivinado por el usuario con el número a adivinar (estado) y devuelve un 
    mensaje indicando si el número es mayor, menor o correcto.

    """
    
    if numero < estado:
        return "el numero es mayor"
    elif numero > estado:
        return "el numero es menor"
    else:
        return "¡Felicidades! Has adivinado el número."
