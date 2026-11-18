import json
from Modelos.Categoria import Categoria

class CategoriaDAO:

    def obtener_todas(self):
        with open("Datos/categorias.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            categorias=[]

            for dato in datos:
                nueva_categoria= Categoria(dato["id"], dato["nombre"])
                categorias.append(nueva_categoria)

            return categorias

    def obtener_por_nombre(self, nombre):
         with open("Datos/categorias.json", "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)

                    for dato in datos:
                         if dato["nombre"].lower()== nombre.lower():
                              categoria_por_nombre= Categoria(dato["id"], dato["nombre"])
                              return categoria_por_nombre
                    return None
    def obtener_por_id(self, id):
         with open("Datos/categorias.json", "r", encoding="utf-8") as archivo:
                    datos=json.load(archivo)

                    for dato in datos:
                          if dato["id"]==id:
                                categoria_por_id= Categoria(dato["id"], dato["nombre"])
                                return categoria_por_id
                    return None