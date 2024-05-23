from generar_numero_secreto import generar_numero_secreto
from adivinar import adivinar

def jugar():
    numero_secreto = generar_numero_secreto(1, 100)
    intentos = 0
    max_intentos = 10

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 100.")
    print(f"Tienes {max_intentos} intentos para adivinarlo.")

    while intentos < max_intentos:
        suposicion = int(input("Introduce tu suposición: "))
        respuesta = adivinar(numero_secreto, suposicion)
        print(respuesta)
        
        if respuesta == "Has ganado!":
            break
        intentos += 1

    if intentos == max_intentos:
        print(f"Lo siento, has alcanzado el número máximo de intentos. El número era {numero_secreto}.")

if __name__ == "__main__":
    jugar()
