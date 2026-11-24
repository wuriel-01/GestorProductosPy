from Datos.movimientosDAO import MovimientosDAO
from Datos.ProductoDAO import ProductoDAO
from Validaciones.ValidacionMovimiento import (
    validar_cantidad,
    validar_egreso,
    validar_ingreso,
    validar_descripcion
)
import uuid
from datetime import datetime
class ServicioMovimientos:
    def __init__(self):
        self.movimientos_dao=MovimientosDAO()
        self.productos_dao=ProductoDAO()

    def obtener_todos(self):
        return self.movimientos_dao.obtener_todos()

    def obtener_por_id(self, id):
        if not id:
            raise ValueError("Id invalido")

        movimiento_por_id=self.movimientos_dao.obtener_por_id(id)

        if movimiento_por_id is None:
            raise ValueError("no existe movimiento con ese ID")

        return movimiento_por_id

    def obtener_por_producto(self, id_producto):
        if not id_producto:
             raise ValueError("Id invalido")
        
        movimiento_por_producto=self.movimientos_dao.obtener_por_producto(id_producto)
        if not movimiento_por_producto:
             raise ValueError("no existe movimiento con ese producto")
       
        return movimiento_por_producto 

    def obtener_pot_tipo(self, tipo):
        if not tipo:
            raise ValueError("tipo invalido")

        movimiento_por_tipo=self.movimientos_dao.obtener_por_tipo(tipo)

        if not movimiento_por_tipo :
            raise ValueError("no se encontro movimiento con ese tipo")

        return movimiento_por_tipo

    def registrar_entrada(self, movimiento):
        producto_por_id=self.productos_dao.obtener_producto_id(movimiento.id_producto)

        if producto_por_id is None:
            raise ValueError("no existe producto seleccionado")
        
        cantidad_convertidad=validar_cantidad(movimiento.cantidad)
        validar_ingreso(producto_por_id.stock, cantidad_convertidad )
        validar_descripcion(movimiento.descripcion)
        
        producto_por_id.stock+=cantidad_convertidad
        producto_actualizado= self.productos_dao.actualizar_producto(producto_por_id)

        if not producto_actualizado:
            raise ValueError("no se pudo actualizar el producto")

        movimiento.id = str(uuid.uuid4())
        movimiento.tipo = "Entrada"
        movimiento.cantidad = cantidad_convertidad
        movimiento.nombre_producto = producto_por_id.nombre
        movimiento.fecha = datetime.now()

        self.movimientos_dao.cargar_movimiento(movimiento)

        return movimiento


    def registrar_salida(self, movimiento):
        
        producto = self.productos_dao.obtener_producto_id(movimiento.id_producto)

        if producto is None:
            raise ValueError("No existe el producto seleccionado")
        
        cantidad_convertidad = validar_cantidad(movimiento.cantidad)
        validar_egreso(producto.stock, cantidad_convertidad)
        validar_descripcion(movimiento.descripcion)

        producto.stock -= cantidad_convertidad
        producto_actualizado = self.productos_dao.actualizar_producto(producto)

        if not producto_actualizado:
            raise ValueError("No se pudo actualizar el producto")

        movimiento.id = str(uuid.uuid4())
        movimiento.tipo = "Salida"
        movimiento.cantidad = cantidad_convertidad
        movimiento.nombre_producto = producto.nombre
        movimiento.fecha = datetime.now()
        

        self.movimientos_dao.cargar_movimiento(movimiento)

        return movimiento
        


        
        




        

        