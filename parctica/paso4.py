from paso2 import generar_numero_secreto
from paso5 import adivinar

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

if __name__ == "__main__":
    test_adivinar_demasiado_alto()
    test_adivinar_demasiado_bajo()
    test_adivinar_correcto()
