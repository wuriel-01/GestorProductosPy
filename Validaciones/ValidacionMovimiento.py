def validar_cantidad(cantidad):
    try:
        cantidad_convertida = int(cantidad)
    except (ValueError, TypeError):
        raise ValueError("La cantidad debe ser un número entero")

    if str(cantidad).strip() != str(cantidad_convertida):
        raise ValueError("La cantidad no puede contener decimales")

    if cantidad_convertida <= 0:
        raise ValueError("La cantidad debe ser mayor que cero")

    return cantidad_convertida


def validar_ingreso(stock, cantidad):
    if int(stock) + int(cantidad) > 100000:
        limite_ingreso = 100000 - stock
        raise ValueError(f"El límite de ingreso es {limite_ingreso} unidades")

def validar_egreso(stock, cantidad):
    if int(cantidad)> int(stock):
        limite_egreso = stock
        raise ValueError(f"El límite de salida es {limite_egreso} unidades")


def validar_descripcion(descripcion):
    if not isinstance(descripcion, str):
        raise ValueError("La descripción debe ser texto")

    if len(descripcion.strip()) > 150:
        raise ValueError("La descripción no puede superar los 150 caracteres")