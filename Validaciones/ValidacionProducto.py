def validar_nombre(nombre):
    nombre_producto=nombre.strip()

    if nombre_producto == "":
        raise ValueError( "El nombre no puede estar vacío")

    elif len(nombre_producto) > 20:
        raise ValueError("El nombre no puede contener más de 20 caracteres")

    elif len(nombre_producto) < 3:
       raise ValueError ("El nombre debe tener al menos 3 caracteres")



def validar_precio (precio):
    try:
        precio = float(precio)
    except ValueError:
        raise ValueError("El precio debe ser numérico")
    

    if precio < 0:
       raise ValueError("El precio debe ser mayor que cero")
       

    elif precio > 10000000:
        raise ValueError( "El precio no puede superar los $10.000.000")
        


def validar_stock (stock):
    try:
        stock= int(stock)
    except ValueError:
            raise ValueError( "El stock debe ser numérico")
            

    if stock < 0 :
        raise ValueError( "El stock debe ser mayor/igual que cero")
       

    elif stock > 100000:
        raise ValueError( "El stock no puede superar las 100.000 unidades")
        




def validar_codigoBarra(codigoBarra):
    if codigoBarra == "":
        raise ValueError( "El código de barras no puede estar vacío")
        

    elif not codigoBarra.isdigit():
        raise ValueError("El código de barras debe contener solamente números")
        

    elif len(codigoBarra) != 13:
        raise ValueError( "El código de barras debe contener 13 dígitos")


def validar_descripcion(descripcion):
    if descripcion is None:
        raise ValueError("La descripción no es válida")

    if len(descripcion.strip()) > 300:
        raise ValueError("La descripción no puede superar los 300 caracteres")       


def validar_categoria(categoria_id):
    if categoria_id is None or categoria_id == "":
        raise ValueError("Debe seleccionar una categoría")
        