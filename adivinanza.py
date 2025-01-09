import random


def juego_adivinanza():
    # generar un numero del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adininanza de numero")
    print("Debes adivinar un numero entre el 1 al 100")
    print("¡Intenta adivinarlo!")

    while not adivinado:
        # SOlicitar un numero del 1 al 100
        adivinanza = input("introduzca un numero del 1 al 100:")

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Lo estamos pasando de texto a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicitaciones has ganado! El número {adivinanza} es el secreto y lo has logrado en {intentos} intentos. "
                )

        else:
            print("Por favor introdusca un numero valido")

juego_adivinanza()
