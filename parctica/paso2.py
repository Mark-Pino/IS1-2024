import random

def generar_numero_secreto(minimo, maximo):
    return random.randint(minimo, maximo)

def test_generar_numero_secreto():
    numero_secreto = generar_numero_secreto(1, 100)
    print(f"Número secreto generado: {numero_secreto}")  # Imprimir el número secreto generado
    assert 1 <= numero_secreto <= 100

# Ejecutar la prueba
test_generar_numero_secreto()
