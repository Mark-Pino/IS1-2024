def adivinar(numero_secreto, suposicion):
    if suposicion > numero_secreto:
        return "Demasiado alto"
    elif suposicion < numero_secreto:
        return "Demasiado bajo"
    else:
        return "Has ganado!"