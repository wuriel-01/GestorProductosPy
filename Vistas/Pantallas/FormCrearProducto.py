import uuid
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from Servicios.ServicioProductos import ServicioProductos
from Servicios.ServicioCategorias import ServicioCategorias
from Modelos.Producto import Producto

class FormCrearProducto:
    def __init__(self, contenedor):
        self.contenedor= contenedor
        self.servicios_productos=ServicioProductos()
        self.servicios_categorias=ServicioCategorias()
        self.categorias=self.servicios_categorias.obtener_todas()
        self.crear_interfaz()


    def crear_interfaz(self):
        self.crear_encabezado()
        self.crear_formulario()

    def crear_encabezado(self):
        titulo = ctk.CTkLabel(
            self.contenedor,
            text="Gestión de Productos",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=40)

        encabezado= ctk.CTkLabel(
            self.contenedor,
            text="Ingresa nuevos Productos a tu inventario",
            font=("Arial", 12 )
        )
        encabezado.pack(pady=40)
    def crear_formulario(self):
        self.label_nombre = ctk.CTkLabel(
            self.contenedor,
            text="Nombre",
            font=("Arial", 12, "bold")
        )
        self.label_nombre.pack(pady=(10, 5))

        self.txt_nombre = ctk.CTkEntry(
            self.contenedor,
            placeholder_text="Ingrese el nombre"
        )
        self.txt_nombre.pack(pady=5)

        self.label_precio = ctk.CTkLabel(
            self.contenedor,
            text="Precio",
            font=("Arial", 12, "bold")
        )
        self.label_precio.pack(pady=(10, 5))

        self.txt_precio = ctk.CTkEntry(
            self.contenedor,
            placeholder_text="Ingrese el precio"
        )
        self.txt_precio.pack(pady=5)

        self.label_stock = ctk.CTkLabel(
            self.contenedor,
            text="Stock",
            font=("Arial", 12, "bold")
        )
        self.label_stock.pack(pady=(10, 5))

        self.txt_stock = ctk.CTkEntry(
            self.contenedor,
            placeholder_text="Ingrese las unidades del producto"
        )
        self.txt_stock.pack(pady=5)

        self.label_descripcion = ctk.CTkLabel(
            self.contenedor,
            text="Descripcion",
            font=("Arial", 12, "bold")
        )
        self.label_descripcion.pack(pady=(10, 5))

        self.txt_descripcion = ctk.CTkEntry(
            self.contenedor,
            placeholder_text="Ingrese la descripcion del producto"
        )
        self.txt_descripcion.pack(pady=5)

        self.label_categoria = ctk.CTkLabel(
            self.contenedor,
            text="Categoría",
            font=("Arial", 12, "bold")
        )
        self.label_categoria.pack(pady=(10, 5))
        nombres_categorias = [
        categoria.nombre for categoria in self.categorias
        ]

        self.txt_categoria = ctk.CTkOptionMenu(
            self.contenedor,
            values=nombres_categorias
        )
        self.txt_categoria.pack(pady=5)

        self.label_codigoBarra = ctk.CTkLabel(
            self.contenedor,
            text="Código de barras",
            font=("Arial", 12, "bold")
        )
        self.label_codigoBarra.pack(pady=(10, 5))

        self.txt_codigoBarra = ctk.CTkEntry(
            self.contenedor,
            placeholder_text="Ingrese el código de barras"
        )
        self.txt_codigoBarra.pack(pady=5)

        self.boton_guardar = ctk.CTkButton(
            self.contenedor,
            text="Guardar cambios",
            command=self.guardar_cambios
            )
        self.boton_guardar.pack(pady=20)

    def borrar_campos(self):
     self.txt_nombre.delete(0, "end")
     self.txt_precio.delete(0, "end")
     self.txt_stock.delete(0, "end")
     self.txt_descripcion.delete(0, "end")
     self.txt_categoria.set("Almacén")
     self.txt_codigoBarra.delete(0, "end")



    def guardar_cambios(self):
        id_producto=str(uuid.uuid4())
        nombre=self.txt_nombre.get()
        precio=self.txt_precio.get()
        stock=self.txt_stock.get()
        descripcion=self.txt_descripcion.get()
        categoria_nombre = self.txt_categoria.get()
        codigoBarra=self.txt_codigoBarra.get()

        categoria_id=self.servicios_categorias.obtener_por_nombre(categoria_nombre)

        try:
          producto= Producto(id_producto, nombre, precio, stock, descripcion, categoria_id.id, codigoBarra)
          self.servicios_productos.crear_producto(producto)
          messagebox.showinfo("Exito", "Producto cargado correctamente")
          self.borrar_campos()
          return
        except ValueError as error: 
             messagebox.showerror("Error", str(error))
             return
                


                



        
