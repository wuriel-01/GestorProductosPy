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


def validar_tipo(tipo):
    tipos_validos = ["entrada", "salida"]

    if not isinstance(tipo, str) or tipo.strip().lower() not in tipos_validos:
        raise ValueError("El tipo de movimiento debe ser Entrada o Salida")


def validar_descripcion(descripcion):
    if not isinstance(descripcion, str):
        raise ValueError("La descripción debe ser texto")

    if len(descripcion.strip()) > 150:
        raise ValueError("La descripción no puede superar los 150 caracteres")