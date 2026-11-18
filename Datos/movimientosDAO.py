import json
from Modelos.Movimientos import Movimiento
from datetime import datetime
class MovimientosDAO:

    def cargar_movimiento(self, movimiento):
        with open("Datos/movimientos.json", "r", encoding="utf-8") as archivo:
            datos=json.load(archivo)


        nuevo_movimiento={
        "id":movimiento.id,
        "id_producto":movimiento.id_producto,
        "nombre_producto":movimiento.nombre_producto,
        "tipo":movimiento.tipo,
        "cantidad":movimiento.cantidad,
        "fecha": movimiento.fecha.strftime("%d/%m/%Y %H:%M:%S"),
        "descripcion":movimiento.descripcion,
        }

        datos.append(nuevo_movimiento)

        with open("Datos/movimientos.json", "w", encoding="utf-8") as archivo:
                 json.dump(datos, archivo, indent=4, ensure_ascii=False) 

    def obtener_todos(self):
         with open("Datos/movimientos.json", "r", encoding="utf-8") as archivo:
                     datos=json.load(archivo)
                     movimientos=[]
                     for dato in datos:
                           nuevo_movimiento=Movimiento(
                             dato["id"],
                             dato["id_producto"],
                             dato["nombre_producto"],
                             dato["tipo"],
                             dato["cantidad"],
                             datetime.strptime(dato["fecha"], "%d/%m/%Y %H:%M:%S"),
                             dato["descripcion"]    
                           )
                           movimientos.append(nuevo_movimiento)
                     return movimientos

    def obtener_por_id(self, id):
          with open("Datos/movimientos.json", "r", encoding="utf-8") as archivo:
                               datos=json.load(archivo)
                               for dato in datos:
                                       if(id==dato["id"]):
                                        movimiento_id= Movimiento(
                                            dato["id"],
                                            dato["id_producto"],
                                            dato["nombre_producto"],
                                            dato["tipo"],
                                            dato["cantidad"],
                                            datetime.strptime(dato["fecha"], "%d/%m/%Y %H:%M:%S"),
                                            dato["descripcion"]
                                        )
                                        return movimiento_id
                               return None

    def obtener_por_producto(self, id_producto):
                     with open("Datos/movimientos.json", "r", encoding="utf-8") as archivo:
                               datos=json.load(archivo)
                               movimientos_producto=[]
                               for dato in datos:
                                       if(id_producto==dato["id_producto"]):
                                        movimiento_producto_id= Movimiento(
                                            dato["id"],
                                            dato["id_producto"],
                                            dato["nombre_producto"],
                                            dato["tipo"],
                                            dato["cantidad"],
                                            datetime.strptime(dato["fecha"], "%d/%m/%Y %H:%M:%S"),
                                            dato["descripcion"]
                                        )
                                        movimientos_producto.append(movimiento_producto_id)
                                
                               return movimientos_producto


    def obtener_por_tipo(self, tipo):
                     with open("Datos/movimientos.json", "r", encoding="utf-8") as archivo:
                               datos=json.load(archivo)
                               movimientos_tipo=[]
                               for dato in datos:
                                       if(tipo==dato["tipo"]):
                                        movimiento_por_tipo= Movimiento(
                                            dato["id"],
                                            dato["id_producto"],
                                            dato["nombre_producto"],
                                            dato["tipo"],
                                            dato["cantidad"],
                                            datetime.strptime(dato["fecha"], "%d/%m/%Y %H:%M:%S"),
                                            dato["descripcion"]
                                        )
                                        movimientos_tipo.append(movimiento_por_tipo)
                                
                               return movimientos_tipo
                                               



     







# 