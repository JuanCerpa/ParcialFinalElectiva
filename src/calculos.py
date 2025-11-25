def suma(a, b):
    """Retorna la suma de dos números."""
    return a + b


def division(a, b):
    """Retorna la división, maneja división por cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def resta(a, b):
    return a - b