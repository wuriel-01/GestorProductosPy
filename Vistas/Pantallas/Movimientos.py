from Servicios.ServicioMovimientos import ServicioMovimientos
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from Servicios.ServicioProductos import ServicioProductos
from Servicios.ServicioCategorias import ServicioCategorias
from Vistas.Pantallas.FormCrearMovimiento import FormCrearMovimiento

class Movimientos:
    def __init__(self, contenedor):
       self.contenedor=contenedor
       self.servicio_movimientos=ServicioMovimientos()
       self.servicio_productos=ServicioProductos()
       self.crear_interfaz()

    def crear_interfaz(self):
        self.crear_encabezado()
        self.crear_tabla()
        self.crear_herramientas()
        
    def crear_encabezado(self):
        titulo = ctk.CTkLabel(
            self.contenedor,
            text="Gestión de Movimientos",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=40)

        encabezado= ctk.CTkLabel(
            self.contenedor,
            text="Administra los movimientos de tus productos",
            font=("Arial", 12 )
        )
        encabezado.pack(pady=40)

    def nuevo_movimiento(self):
            FormCrearMovimiento(
            self.contenedor.winfo_toplevel(),
            self.cargar_movimientos,
        )

    
    def crear_herramientas(self):
        self.buscador=ctk.CTkEntry(
            self.contenedor,
            placeholder_text="Buscar Movimiento",
        )

        self.boton_nuevo_momiento = ctk.CTkButton(
            self.contenedor,
            text="+ Nuevo Movimiento",
            command=self.nuevo_movimiento
    )

        self.boton_nuevo_momiento.pack()
        self.buscador.pack()
        self.buscador.bind("<KeyRelease>", self.buscar_producto)

    def buscar_producto(self, evento):
        busqueda = self.buscador.get().strip()
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        movimientos=self.servicio_movimientos.obtener_todos()

        for movimiento in movimientos:
           if   (
                busqueda == ""
                or busqueda in movimiento.nombre_producto.lower()
                ):
                self.tabla_productos.insert(
                    "",
                    "end",
                    iid=movimiento.id,
                    values=(
                    movimiento.fecha,
                    movimiento.nombre_producto,
                    movimiento.tipo,
                    movimiento.cantidad,
                    movimiento.descripcion,  
                    )
                )

    def cargar_movimientos(self):
         for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

         movimientos=self.servicio_movimientos.obtener_todos()

         for movimiento in movimientos:
           
             
             self.tabla_productos.insert(
                "",
                tk.END,
                iid=movimiento.id,
                values=(
                    movimiento.fecha,
                    movimiento.nombre_producto,
                    movimiento.tipo,
                    movimiento.cantidad,
                    movimiento.descripcion,                
             )
             )

    def crear_tabla(self):
        self.tabla_productos=ttk.Treeview(
        self.contenedor,
        columns=("Fecha", "Producto", "Tipo", "Cantidad","Descripcion"),
        show="headings"
    )
        self.tabla_productos.heading("Fecha", text="Fecha")
        self.tabla_productos.heading("Producto", text="Producto")
        self.tabla_productos.heading("Tipo", text="Tipo")
        self.tabla_productos.heading("Cantidad", text="Cantidad")
        self.tabla_productos.heading("Descripcion", text="Descripcion")

    
        self.tabla_productos.column("Fecha", width=140, anchor="w")
        self.tabla_productos.column("Producto", width=70, anchor="center")
        self.tabla_productos.column("Tipo", width=60, anchor="center")
        self.tabla_productos.column("Cantidad", width=110, anchor="center")
        self.tabla_productos.column("Descripcion", width=110, anchor="center")

        scrollbar = ttk.Scrollbar(
            self.contenedor,
            orient="vertical",
            command=self.tabla_productos.yview
        )
        self.cargar_movimientos()

        self.tabla_productos.configure(yscrollcommand=scrollbar.set)

        self.tabla_productos.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
