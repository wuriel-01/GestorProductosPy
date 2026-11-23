import customtkinter as ctk


class PantallaInicio:
    def __init__(self, contenedor):
        self.contenedor = contenedor

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = ctk.CTkLabel(
            self.contenedor,
            text="Bienvenido al Gestor de Inventario",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=40)

        descripcion = ctk.CTkLabel(
            self.contenedor,
            text="Administrá tus productos, movimientos y stock.",
            font=("Arial", 16)
        )
        descripcion.pack(pady=10)
