class Producto:
    def __init__(self, id_producto, nombre, precio, stock, descripcion, categoria_id, codigoBarra):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.descripcion = descripcion
        self.categoria_id = categoria_id
        self.id_producto = id_producto
        self.codigoBarra = codigoBarra