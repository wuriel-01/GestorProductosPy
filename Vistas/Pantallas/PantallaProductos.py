
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from Servicios.ServicioProductos import ServicioProductos
from Servicios.ServicioCategorias import ServicioCategorias
from Vistas.Pantallas.FormEditarProducto import FormEditarProducto

class PantallaProductos:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        self.servicios_productos= ServicioProductos()
        self.servicios_categorias=ServicioCategorias()
        self.crear_interfaz()


    def crear_interfaz(self):
        self.crear_encabezado()
        self.crear_herramientas()
        self.crear_tabla()

    def crear_encabezado(self):
        titulo = ctk.CTkLabel(
            self.contenedor,
            text="Gestión de Productos",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=40)

        encabezado= ctk.CTkLabel(
            self.contenedor,
            text="Administra los productos de tu inventario",
            font=("Arial", 12 )
        )
        encabezado.pack(pady=40)

    def crear_herramientas(self):
        self.buscador=ctk.CTkEntry(
            self.contenedor,
            placeholder_text="Buscar Producto",
        )

        self.boton_editar = ctk.CTkButton(
            self.contenedor,
            text="Editar producto",
            command=self.editar_producto
    )
        self.boton_eliminar = ctk.CTkButton(
            self.contenedor,
            text="Eliminar producto",
            command=self.eliminar_producto
    )
        self.boton_editar.pack()
        self.boton_eliminar.pack()
        self.buscador.pack()
        self.buscador.bind("<KeyRelease>", self.buscar_producto)
        

    def cargar_productos(self):
         for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

         productos=self.servicios_productos.obtener_todos()
         for producto in productos:
            categoria=self.servicios_categorias.obtener_por_id(producto.categoria_id)
            self.tabla_productos.insert(
                "",
                tk.END,
                iid=producto.id_producto,
                values=(
                    producto.nombre,
                    producto.precio,
                    producto.stock,
                    categoria.nombre,
                    producto.descripcion,
                    producto.codigoBarra,
                    "disponible"
                 
                )
            )

    def buscar_producto(self, evento):
        busqueda = self.buscador.get().strip()

        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        productos=self.servicios_productos.obtener_todos()

        for producto in productos:
           if   (
                busqueda == ""
                or busqueda in producto.nombre.lower()
                or busqueda in producto.codigoBarra.lower()
                ):

                categoria=self.servicios_categorias.obtener_por_id(producto.categoria_id)
                self.tabla_productos.insert(
                    "",
                    "end",
                    iid=producto.id_producto,
                    values=(
                        producto.nombre,
                        producto.precio,
                        producto.stock,
                        categoria.nombre,
                        producto.descripcion,
                        producto.codigoBarra,
                        "disponible"
                    )
                )

    def crear_tabla(self):
        self.tabla_productos=ttk.Treeview(
        self.contenedor,
        columns=("Nombre", "Precio", "Stock", "Categoria","Descripcion", "Codigo de Barra", "Estado"),
        show="headings"
    )
        self.tabla_productos.heading("Nombre", text="Nombre")
        self.tabla_productos.heading("Precio", text="Precio")
        self.tabla_productos.heading("Stock", text="Stock")
        self.tabla_productos.heading("Categoria", text="Categoria")
        self.tabla_productos.heading("Descripcion", text="Descripcion")
        self.tabla_productos.heading("Codigo de Barra", text="Codigo de Barra")
        self.tabla_productos.heading("Estado", text="Estado")
    
        self.tabla_productos.column("Nombre", width=140, anchor="w")
        self.tabla_productos.column("Precio", width=70, anchor="center")
        self.tabla_productos.column("Stock", width=60, anchor="center")
        self.tabla_productos.column("Categoria", width=110, anchor="center")
        self.tabla_productos.column("Descripcion", width=110, anchor="center")
        self.tabla_productos.column("Codigo de Barra", width=130, anchor="center")
        self.tabla_productos.column("Estado", width=90, anchor="center")
        scrollbar = ttk.Scrollbar(
            self.contenedor,
            orient="vertical",
            command=self.tabla_productos.yview
        )
        self.cargar_productos()

        self.tabla_productos.configure(yscrollcommand=scrollbar.set)

        self.tabla_productos.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


    def editar_producto(self):
        seleccion = self.tabla_productos.selection()

        if not seleccion:
            return

        id_producto = seleccion[0]

        producto = self.servicios_productos.obtener_por_id(id_producto)

        FormEditarProducto(
            producto,
            self.contenedor.winfo_toplevel(),
            self.cargar_productos
        )

    def eliminar_producto(self):
        seleccion= self.tabla_productos.selection()
        if not seleccion:
         messagebox.showerror(
            "Error",
            "Seleccione un producto",
            parent=self.contenedor
        )
         return
         
        id_producto=seleccion[0]
        self.servicios_productos.eliminar_producto(id_producto)
        self.cargar_productos()

        messagebox.showinfo("Exito", "producto eliminado correctamente")
        return 

        






    
