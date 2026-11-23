from Datos.ProductoDAO import ProductoDAO
from Datos.categoriaDAO import CategoriaDAO
import uuid
from Validaciones.ValidacionProducto import validar_nombre, validar_categoria, validar_codigoBarra, validar_precio, validar_stock
class ServicioProductos:
  def __init__(self):
     self.producto_dao=ProductoDAO()
     self.categoria_dao = CategoriaDAO()

  def obtener_todos(self):
     return self.producto_dao.obtener_todos_productos()

  def obtener_por_id(self, id):
    if not id:
        raise ValueError("El ID del producto no es válido")

    producto = self.producto_dao.obtener_producto_id(id)

    if producto is None:
        raise ValueError("No se encontró el producto")

    return producto

  def obtener_por_nombre(self, nombre):
     if not nombre:
        raise ValueError("El nombre del producto es invalido")
     producto= self.producto_dao.obtener_producto_nombre(nombre)

     if producto is None:
        raise ValueError("No se encontró el producto")

     return producto

  def crear_producto(self, producto):
        validar_nombre(producto.nombre)
        validar_stock(producto.stock)
        validar_precio(producto.precio)
        validar_categoria(producto.categoria_id)
        validar_codigoBarra(producto.codigoBarra)
        
        categoria = self.categoria_dao.obtener_por_id(producto.categoria_id)

        if categoria is None:
            raise ValueError("La categoría seleccionada no existe")
  
        producto_existente=self.producto_dao.obtener_producto_codigoBarra(producto.codigoBarra)
        if producto_existente is not None:
           raise ValueError("producto ya existente con ese codigo de barra")

        
        self.producto_dao.cargar_producto(producto)

        return producto

  def eliminar_producto(self,id):
     producto_encontrado=self.producto_dao.obtener_producto_id(id)

     if producto_encontrado is None:
      raise ValueError("Producto no encontrado")

     return self.producto_dao.eliminar_producto(id)

  def actualizar_producto(self, producto):
    if not producto.id_producto:
        raise ValueError("ID inválido, no se puede actualizar el producto")

    producto_encontrado = self.producto_dao.obtener_producto_id(producto.id_producto)

    if producto_encontrado is None:
        raise ValueError("No existe el producto que desea actualizar")

    validar_nombre(producto.nombre)
    validar_precio(producto.precio)
    validar_categoria(producto.categoria_id)
    validar_stock(producto_encontrado.stock)
    validar_codigoBarra(producto.codigoBarra)

    categoria = self.categoria_dao.obtener_por_id(producto.categoria_id)

    if categoria is None:
        raise ValueError("La categoría seleccionada no existe")

    producto_existente = self.producto_dao.obtener_producto_codigoBarra(producto.codigoBarra)

    if producto_existente is not None and producto_existente.id_producto != producto.id_producto:
        raise ValueError("Ya existe otro producto con ese código de barras")

    producto.stock = producto_encontrado.stock

    actualizado = self.producto_dao.actualizar_producto(producto)

    if not actualizado:
        raise ValueError("No se pudo actualizar el producto")

    return producto

     
     





# crear_producto()	Validar y registrar un producto.
# obtener_todos()	Consultar todos los productos.
# obtener_por_id()	Buscar un producto por ID.
# obtener_por_nombre()	Buscar por nombre.
# actualizar_producto()	Validar y actualizar un producto.
# eliminar_producto()