import random
numero_secreto = random.randint(1, 100)
intentos = 0
fin_intentos = 12
print("Adivina el numero del 1 al 100")
print("Tienes 12 intentos")

while intentos < fin_intentos:
    try:
        numero = int(input("-> Numero: "))
        if numero < 1 or numero > 100:
            print("El numero no puede ser menor a 0 ni mayor a 100")
            continue
        if numero < numero_secreto:
                intentos += 1
                if intentos < 12:
                    print("El numero es mayor")
                    
        elif numero > numero_secreto:
                intentos += 1
                if intentos < 12:
                    print("El numero es menor")
            
        elif numero == numero_secreto:
            print(f"Correcto!!! adivinaste el numero secreto. \nTus intentos fueron: {intentos}")
            break
    except Exception:
        print("Error!!! Introduce un Numero entero")
else:
    print(f"Te has quedado sin intentos. \nSuerte para la proxima")
