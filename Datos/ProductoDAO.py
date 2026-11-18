import json
from Modelos.Producto import Producto
class ProductoDAO:
    def cargar_producto(self, producto):
        with open("Datos/productos.json", "r", encoding="utf-8") as archivo:
            datos= json.load(archivo)


        nuevo_producto={
            "id_producto": producto.id_producto,
            "nombre":producto.nombre,
            "precio":producto.precio,
            "stock":producto.stock,
            "descripcion":producto.descripcion,
            "categoria_id": producto.categoria_id,
            "codigoBarra": producto.codigoBarra

        } 

        datos.append(nuevo_producto)

        with open("Datos/productos.json", "w", encoding="utf-8") as archivo:
         json.dump(datos, archivo, indent=4, ensure_ascii=False) 


    def obtener_todos_productos(self):
       with open("Datos/productos.json", "r", encoding="utf-8") as archivo:
          datos= json.load(archivo)
          productos=[]

          for dato in datos:
             nuevo_producto = Producto(dato["id_producto"],
                                        dato["nombre"],
                                        dato["precio"],
                                        dato["stock"],
                                        dato["descripcion"],
                                        dato["categoria_id"],
                                        dato["codigoBarra"])
             productos.append(nuevo_producto)
          return productos

    def obtener_producto_id(self, id):
       with open("Datos/productos.json", "r", encoding="utf-8") as archivo:
                 datos= json.load(archivo)

                 for dato in datos:
                     if dato["id_producto"]==id:
                         producto_id=Producto(dato["id_producto"],
                                        dato["nombre"],
                                        dato["precio"],
                                        dato["stock"],
                                        dato["descripcion"],
                                        dato["categoria_id"],
                                        dato["codigoBarra"])
                         return producto_id
                 return None


    def obtener_producto_nombre(self, nombre):
              with open("Datos/productos.json", "r", encoding="utf-8") as archivo:
                        datos= json.load(archivo)
       
                        for dato in datos:
                            if dato["nombre"].lower()==nombre.lower():
                                producto_nombre=Producto(dato["id_producto"],
                                               dato["nombre"],
                                               dato["precio"],
                                               dato["stock"],
                                               dato["descripcion"],
                                               dato["categoria_id"],
                                               dato["codigoBarra"])
                                return producto_nombre
                        return None
    
    def actualizar_producto(self, producto):
        with open("Datos/productos.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        for indice, dato in enumerate(datos):
            if dato["id_producto"] == producto.id_producto:
                nuevo_producto = {
                "id_producto": producto.id_producto,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "stock": producto.stock,
                "descripcion": producto.descripcion,
                "categoria_id": producto.categoria_id,
                "codigoBarra": producto.codigoBarra
            }

            datos[indice] = nuevo_producto

            with open("Datos/productos.json", "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)

            return True

        return False

    def eliminar_producto(self, id):
           with open("Datos/productos.json", "r", encoding="utf-8") as archivo:
                                      datos= json.load(archivo)
                                      for dato in datos:
                                             if dato["id_producto"]==id:
                                                   datos.remove(dato)
                                                   with open("Datos/productos.json", "w", encoding="utf-8") as archivo:
                                                                   json.dump(datos, archivo, indent=4, ensure_ascii=False)
                                                   return True
                                      return False
                  
                                        
                                        