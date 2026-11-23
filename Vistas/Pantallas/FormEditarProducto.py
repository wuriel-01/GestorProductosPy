
import customtkinter as ctk
from tkinter import messagebox
from Servicios.ServicioProductos import ServicioProductos
from Servicios.ServicioCategorias import ServicioCategorias


class FormEditarProducto:
    def __init__(self, producto, ventana_principal, al_guardar):
        self.ventana = ctk.CTkToplevel(ventana_principal)
        self.producto = producto
        self.al_guardar = al_guardar

        self.servicio_categorias = ServicioCategorias()
        self.servicio_productos = ServicioProductos()

        self.ventana.title("Editar producto")
        self.ventana.geometry("500x700")
        self.ventana.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):
        self.crear_encabezado()
        self.formulario_edicion()

    def crear_encabezado(self):
        titulo = ctk.CTkLabel(
            self.ventana,
            text="Editar Producto",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=(25, 10))

        encabezado = ctk.CTkLabel(
            self.ventana,
            text="Edita el producto seleccionado",
            font=("Arial", 12)
        )
        encabezado.pack(pady=(0, 15))

    def formulario_edicion(self):

        self.label_nombre = ctk.CTkLabel(
            self.ventana,
            text="Nombre",
            font=("Arial", 12, "bold")
        )
        self.label_nombre.pack(pady=(10, 5))

        self.txt_nombre = ctk.CTkEntry(
            self.ventana,
            placeholder_text="Ingrese el nombre"
        )
        self.txt_nombre.pack(pady=5)
        self.txt_nombre.insert(0, self.producto.nombre)

        self.label_descripcion = ctk.CTkLabel(
            self.ventana,
            text="Descripción",
            font=("Arial", 12, "bold")
        )
        self.label_descripcion.pack(pady=(10, 5))

        self.txt_descripcion = ctk.CTkEntry(
            self.ventana,
            placeholder_text="Ingrese la descripción"
        )
        self.txt_descripcion.pack(pady=5)
        self.txt_descripcion.insert(0, self.producto.descripcion)

        self.label_precio = ctk.CTkLabel(
            self.ventana,
            text="Precio",
            font=("Arial", 12, "bold")
        )
        self.label_precio.pack(pady=(10, 5))

        self.txt_precio = ctk.CTkEntry(
            self.ventana,
            placeholder_text="Ingrese el precio"
        )
        self.txt_precio.pack(pady=5)
        self.txt_precio.insert(0, str(self.producto.precio))

        self.label_categoria = ctk.CTkLabel(
            self.ventana,
            text="Categoría",
            font=("Arial", 12, "bold")
        )
        self.label_categoria.pack(pady=(10, 5))

        categorias = self.servicio_categorias.obtener_todas()
        nombres_categorias = [
            categoria.nombre for categoria in categorias
        ]

        self.txt_categoria = ctk.CTkOptionMenu(
            self.ventana,
            values=nombres_categorias
        )
        self.txt_categoria.pack(pady=5)

        categoria_actual = self.servicio_categorias.obtener_por_id(
            self.producto.categoria_id
        )

        if categoria_actual is not None:
            self.txt_categoria.set(categoria_actual.nombre)

        self.label_codigoBarra = ctk.CTkLabel(
            self.ventana,
            text="Código de barras",
            font=("Arial", 12, "bold")
        )
        self.label_codigoBarra.pack(pady=(10, 5))

        self.txt_codigoBarra = ctk.CTkEntry(
            self.ventana,
            placeholder_text="Ingrese el código de barras"
        )
        self.txt_codigoBarra.pack(pady=5)
        self.txt_codigoBarra.insert(0, self.producto.codigoBarra)

        self.boton_guardar = ctk.CTkButton(
            self.ventana,
            text="Guardar cambios",
            command=self.guardar_cambios
            )
        self.boton_guardar.pack(pady=20)

        self.boton_cancelar = ctk.CTkButton(
                    self.ventana,
                    text="Cancelar",
                    command=self.ventana.destroy
                    )
        self.boton_cancelar.pack(pady=20)


    def guardar_cambios(self):
        nombre = self.txt_nombre.get()
        descripcion = self.txt_descripcion.get()
        precio = self.txt_precio.get()
        categoria_nombre = self.txt_categoria.get()
        codigo_barra = self.txt_codigoBarra.get()

        try:
            categoria = self.servicio_categorias.obtener_por_nombre(
            categoria_nombre
            )

            if categoria is None:
                raise ValueError("La categoría seleccionada no existe")

            self.producto.nombre = nombre
            self.producto.descripcion = descripcion
            self.producto.precio = precio
            self.producto.categoria_id = categoria.id
            self.producto.codigoBarra = codigo_barra

            self.servicio_productos.actualizar_producto(self.producto)

            self.al_guardar()
            self.ventana.destroy()

        except ValueError as error:
            messagebox.showerror("Error al actualizar", str(error))
