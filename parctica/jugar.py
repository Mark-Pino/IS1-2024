import random

# Paso 3: Escribir el código mínimo para que la prueba pase
def generar_numero_secreto(minimo, maximo):
    return random.randint(minimo, maximo)

# Paso 5: Desarrollar el código para que las pruebas pasen
def adivinar(numero_secreto, suposicion):
    if suposicion > numero_secreto:
        return "Demasiado alto"
    elif suposicion < numero_secreto:
        return "Demasiado bajo"
    else:
        return "Has ganado!"

# Paso 2: Escribir la primera prueba
def test_generar_numero_secreto():
    numero_secreto = generar_numero_secreto(1, 100)
    print(f"Número secreto generado: {numero_secreto}")
    assert 1 <= numero_secreto <= 100

# Paso 4: Escribir pruebas adicionales
def test_adivinar_demasiado_alto():
    numero_secreto = generar_numero_secreto(1, 100)
    respuesta = adivinar(numero_secreto, numero_secreto + 50)  # Asegurarse de que la suposición sea demasiado alta
    print(f"Adivinar demasiado alto: Suposición: {numero_secreto + 50}, Respuesta: {respuesta}")
    assert respuesta == "Demasiado alto"

def test_adivinar_demasiado_bajo():
    numero_secreto = generar_numero_secreto(1, 100)
    respuesta = adivinar(numero_secreto, numero_secreto - 50)  # Asegurarse de que la suposición sea demasiado baja
    print(f"Adivinar demasiado bajo: Suposición: {numero_secreto - 50}, Respuesta: {respuesta}")
    assert respuesta == "Demasiado bajo"

def test_adivinar_correcto():
    numero_secreto = generar_numero_secreto(1, 100)
    respuesta = adivinar(numero_secreto, numero_secreto)
    print(f"Adivinar correcto: Suposición: {numero_secreto}, Respuesta: {respuesta}")
    assert respuesta == "Has ganado!"

# Función para jugar interactivamente
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

# Ejecutar todas las pruebas y el juego interactivo
if __name__ == "__main__":
    # Ejecutar pruebas
    test_generar_numero_secreto()
    test_adivinar_demasiado_alto()
    test_adivinar_demasiado_bajo()
    test_adivinar_correcto()
    
    # Jugar interactivamente
    jugar()
