
import customtkinter as ctk


class MenuLateral:
    def __init__(self, contenedor, cambiar_pantalla):
        self.contenedor = contenedor
        self.cambiar_pantalla = cambiar_pantalla

        self.crear_titulo()
        self.crear_botones()

    def crear_titulo(self):
        titulo = ctk.CTkLabel(
            self.contenedor,
            text="GESTOR INVENTARIO",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=30, padx=10)

    def crear_botones(self):
        opciones = ["Inicio", "Productos", "+ Agregar producto","Movimientos",]

        for opcion in opciones:
            boton = ctk.CTkButton(
                self.contenedor,
                text=opcion,
                height=40,
                corner_radius=8,
                command=lambda pantalla=opcion: self.cambiar_pantalla(pantalla)
            )
            boton.pack(fill="x", padx=15, pady=8)
