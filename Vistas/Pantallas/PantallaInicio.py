
import customtkinter as ctk
from tkinter import ttk, messagebox
from datetime import datetime

from Servicios.ServicioProductos import ServicioProductos
from Servicios.ServicioMovimientos import ServicioMovimientos


class PantallaInicio:

    def __init__(self, contenedor):
        self.contenedor = contenedor

        self.servicios_productos = ServicioProductos()
        self.servicios_movimientos = ServicioMovimientos()

        self.crear_interfaz()
        self.actualizar_datos()

    def crear_interfaz(self):
        self.frame_principal = ctk.CTkFrame(
            self.contenedor,
            fg_color="transparent"
        )
        self.frame_principal.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        self.crear_encabezado()
        self.crear_tarjetas()
        self.crear_actividad()
        self.crear_ultimos_movimientos()

    def crear_encabezado(self):
        encabezado = ctk.CTkFrame(
            self.frame_principal,
            fg_color="transparent"
        )
        encabezado.pack(fill="x", pady=(0, 25))

        titulo = ctk.CTkLabel(
            encabezado,
            text="Panel principal",
            font=("Arial", 26, "bold")
        )
        titulo.pack(anchor="w")

        subtitulo = ctk.CTkLabel(
            encabezado,
            text="Resumen general del inventario",
            font=("Arial", 13),
            text_color="gray"
        )
        subtitulo.pack(anchor="w", pady=(5, 0))

    def crear_tarjetas(self):
        contenedor_tarjetas = ctk.CTkFrame(
            self.frame_principal,
            fg_color="transparent"
        )
        contenedor_tarjetas.pack(fill="x", pady=(0, 20))

        for columna in range(2):
            contenedor_tarjetas.grid_columnconfigure(
                columna,
                weight=1
            )

        tarjetas = [
            ("productos", "Productos", "#3B82F6"),
            ("unidades", "Unidades", "#3B82F6"),
            ("stock_bajo", "Stock bajo", "#EAB308"),
            ("sin_stock", "Sin stock", "#EF4444")
        ]

        self.etiquetas_tarjetas = {}

        for indice, (clave, titulo, color) in enumerate(tarjetas):
            fila = indice // 2
            columna = indice % 2

            tarjeta = ctk.CTkFrame(
                contenedor_tarjetas,
                corner_radius=12,
                fg_color=("#F0F0F0", "#242424")
            )
            tarjeta.grid(
                row=fila,
                column=columna,
                sticky="nsew",
                padx=7,
                pady=7
            )

            etiqueta_titulo = ctk.CTkLabel(
                tarjeta,
                text=titulo,
                font=("Arial", 13),
                text_color="gray"
            )
            etiqueta_titulo.pack(
                anchor="w",
                padx=18,
                pady=(15, 5)
            )

            etiqueta_valor = ctk.CTkLabel(
                tarjeta,
                text="0",
                font=("Arial", 28, "bold"),
                text_color=color
            )
            etiqueta_valor.pack(
                anchor="w",
                padx=18,
                pady=(0, 15)
            )

            self.etiquetas_tarjetas[clave] = etiqueta_valor

    def crear_actividad(self):
        actividad = ctk.CTkFrame(
            self.frame_principal,
            corner_radius=12,
            fg_color=("#F0F0F0", "#242424")
        )
        actividad.pack(fill="x", pady=(0, 20))

        titulo = ctk.CTkLabel(
            actividad,
            text="Actividad del inventario",
            font=("Arial", 17, "bold")
        )
        titulo.pack(anchor="w", padx=18, pady=(15, 12))

        datos = [
            ("entradas", "Unidades ingresadas", "#22C55E"),
            ("salidas", "Unidades salidas", "#EF4444")
        ]

        self.etiquetas_actividad = {}

        for clave, nombre, color in datos:
            fila = ctk.CTkFrame(
                actividad,
                fg_color="transparent"
            )
            fila.pack(fill="x", padx=18, pady=5)

            ctk.CTkLabel(
                fila,
                text=nombre,
                font=("Arial", 13)
            ).pack(side="left")

            etiqueta_cantidad = ctk.CTkLabel(
                fila,
                text="0",
                font=("Arial", 13, "bold"),
                text_color=color
            )
            etiqueta_cantidad.pack(side="right")

            self.etiquetas_actividad[clave] = etiqueta_cantidad

        ctk.CTkFrame(
            actividad,
            height=10,
            fg_color="transparent"
        ).pack()

    def crear_ultimos_movimientos(self):
        movimientos = ctk.CTkFrame(
            self.frame_principal,
            corner_radius=12,
            fg_color=("#F0F0F0", "#242424")
        )
        movimientos.pack(fill="both", expand=True)

        titulo = ctk.CTkLabel(
            movimientos,
            text="Últimos movimientos",
            font=("Arial", 17, "bold")
        )
        titulo.pack(anchor="w", padx=18, pady=15)

        estilo = ttk.Style()
        estilo.configure(
            "Dashboard.Treeview",
            rowheight=35,
            font=("Arial", 11)
        )
        estilo.configure(
            "Dashboard.Treeview.Heading",
            font=("Arial", 11, "bold")
        )

        self.tabla_movimientos = ttk.Treeview(
            movimientos,
            columns=("producto", "tipo", "cantidad", "fecha"),
            show="headings",
            style="Dashboard.Treeview",
            height=5
        )

        self.tabla_movimientos.heading(
            "producto",
            text="Producto"
        )
        self.tabla_movimientos.heading(
            "tipo",
            text="Tipo"
        )
        self.tabla_movimientos.heading(
            "cantidad",
            text="Cantidad"
        )
        self.tabla_movimientos.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla_movimientos.column(
            "producto",
            anchor="w",
            width=200
        )
        self.tabla_movimientos.column(
            "tipo",
            anchor="center",
            width=120
        )
        self.tabla_movimientos.column(
            "cantidad",
            anchor="center",
            width=120
        )
        self.tabla_movimientos.column(
            "fecha",
            anchor="center",
            width=150
        )

        self.tabla_movimientos.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

    def convertir_fecha(self, fecha):
        if isinstance(fecha, datetime):
            return fecha

        try:
            return datetime.strptime(
                fecha,
                "%d/%m/%Y %H:%M"
            )
        except (ValueError, TypeError):
            return datetime.min

    def actualizar_datos(self):
        try:
            productos = self.servicios_productos.obtener_todos()
            movimientos = self.servicios_movimientos.obtener_todos()

         

            total_productos = len(productos)

            total_unidades = sum(
                int(producto.stock)
                for producto in productos
            )

            stock_bajo = sum(
                1 for producto in productos
                if 1 <= int(producto.stock) <= 5
            )

            sin_stock = sum(
                1 for producto in productos
                if int(producto.stock) == 0
            )

            self.etiquetas_tarjetas["productos"].configure(
                text=str(total_productos)
            )

            self.etiquetas_tarjetas["unidades"].configure(
                text=str(total_unidades)
            )

            self.etiquetas_tarjetas["stock_bajo"].configure(
                text=str(stock_bajo)
            )

            self.etiquetas_tarjetas["sin_stock"].configure(
                text=str(sin_stock)
            )

           

            total_entradas = sum(
                int(movimiento.cantidad)
                for movimiento in movimientos
                if movimiento.tipo.strip().lower() == "entrada"
            )

            total_salidas = sum(
                int(movimiento.cantidad)
                for movimiento in movimientos
                if movimiento.tipo.strip().lower() == "salida"
            )

            self.etiquetas_actividad["entradas"].configure(
                text=str(total_entradas)
            )

            self.etiquetas_actividad["salidas"].configure(
                text=str(total_salidas)
            )

          

            self.cargar_ultimos_movimientos(movimientos)

        except Exception as error:
            messagebox.showerror(
                "Error al cargar el panel",
                str(error),
                parent=self.contenedor
            )

    def cargar_ultimos_movimientos(self, movimientos):

        for item in self.tabla_movimientos.get_children():
            self.tabla_movimientos.delete(item)

        movimientos_ordenados = sorted(
            movimientos,
            key=lambda movimiento: self.convertir_fecha(
                movimiento.fecha
            ),
            reverse=True
        )

        ultimos_movimientos = movimientos_ordenados[:5]

        for movimiento in ultimos_movimientos:

            tipo = movimiento.tipo.strip().lower()
            cantidad = int(movimiento.cantidad)

            if tipo == "entrada":
                cantidad_mostrar = f"+{cantidad}"
            else:
                cantidad_mostrar = f"-{cantidad}"

            self.tabla_movimientos.insert(
                "",
                "end",
                iid=movimiento.id,
                values=(
                    movimiento.nombre_producto,
                    movimiento.tipo,
                    cantidad_mostrar,
                    movimiento.fecha.strftime("%d/%m/%Y %H:%M")
                    if isinstance(movimiento.fecha, datetime)
                    else movimiento.fecha
                )
            )
