
import customtkinter as ctk

from Vistas.MenuLateral import MenuLateral
from Vistas.Pantallas.PantallaInicio import PantallaInicio
from Vistas.Pantallas.PantallaProductos import PantallaProductos
from Vistas.Pantallas.FormCrearProducto import FormCrearProducto

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestor de Inventario")
        self.geometry("1100x700")
        self.minsize(900, 600)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menu_lateral = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )
        self.menu_lateral.grid(
            row=0,
            column=0,
            sticky="nsew"
        )
        self.menu_lateral.grid_propagate(False)

        self.contenido_principal = ctk.CTkFrame(
            self,
            corner_radius=0
        )
        self.contenido_principal.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.menu = MenuLateral(
            self.menu_lateral,
            self.mostrar_pantalla
        )

        self.pantalla_actual = None
        self.mostrar_pantalla("Inicio")

    def mostrar_pantalla(self, nombre):
        for widget in self.contenido_principal.winfo_children():
            widget.destroy()

        if nombre == "Inicio":
            self.pantalla_actual = PantallaInicio(
                self.contenido_principal
            )

        elif nombre== "Productos":
            self.pantalla_actual= PantallaProductos(
                self.contenido_principal
            )
        elif nombre== "+ Agregar producto":
            self.pantalla_actual=FormCrearProducto(
                self.contenido_principal
            )
        

