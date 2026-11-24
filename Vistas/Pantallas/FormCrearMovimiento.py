import customtkinter as ctk
import uuid
from tkinter import messagebox
from Servicios.ServicioProductos import ServicioProductos
from Servicios.ServicioMovimientos import ServicioMovimientos
from Modelos.Movimientos import Movimiento
from datetime import datetime

class FormCrearMovimiento:
    def __init__(self, ventana_principal, al_guardar):
        self.ventana = ctk.CTkToplevel(ventana_principal)
        self.ventana.transient(ventana_principal)
        self.ventana.grab_set()
        self.ventana.focus_force()
        self.al_guardar = al_guardar
        self.servicio_productos=ServicioProductos()
        self.servicio_movimientos=ServicioMovimientos()
        self.todos_productos=self.servicio_productos.obtener_todos()


        self.ventana.title("Editar producto")
        self.ventana.geometry("500x700")
        self.ventana.resizable(False, False)
        self.crear_interfaz()

    def crear_interfaz(self):
        self.crear_encabezado()
        self.crear_formulario()

    def crear_encabezado(self):
        titulo = ctk.CTkLabel(
            self.ventana,
            text="Gestión de Movimientos",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=40)

        encabezado= ctk.CTkLabel(
            self.ventana,
            text="Registra un nuevo Movimiento",
            font=("Arial", 12 )
        )
        encabezado.pack(pady=40)

    def crear_formulario(self):
        self.label_producto = ctk.CTkLabel(
            self.ventana,
            text="Producto",
            font=("Arial", 12, "bold")
        )
        self.label_producto.pack(pady=(10, 5))

        
        nombres_productos = [
            producto.nombre for producto in self.todos_productos
        ]

        self.txt_producto = ctk.CTkOptionMenu(
            self.ventana,
            values=nombres_productos
        )
        self.txt_producto.pack(pady=5)

        self.label_tipos = ctk.CTkLabel(
            self.ventana,
            text="Ingreso/Salida",
            font=("Arial", 12, "bold")
        )
        self.label_tipos.pack(pady=(10, 5))

        
        tipos = [
            "Ingreso",
            "Salida"
        ]

        self.txt_tipos = ctk.CTkOptionMenu(
            self.ventana,
            values=tipos
        )
        self.txt_tipos.pack(pady=5)

        self.label_cantidad = ctk.CTkLabel(
            self.ventana,
            text="Cantidad",
            font=("Arial", 12, "bold")
        )
        self.label_cantidad.pack(pady=(10, 5))

        self.txt_cantidad = ctk.CTkEntry(
            self.ventana,
            placeholder_text="Ingrese la cantidad"
        )
        self.txt_cantidad.pack(pady=5)

        self.label_descripcion = ctk.CTkLabel(
            self.ventana,
            text="Descripcion",
            font=("Arial", 12, "bold")
        )
        self.label_descripcion.pack(pady=(10, 5))

        self.txt_descripcion = ctk.CTkEntry(
            self.ventana,
            placeholder_text="Ingrese la descripcion del movimiento"
        )
        self.txt_descripcion.pack(pady=5)

        self.boton_guardar = ctk.CTkButton(
            self.ventana,
            text="Confirmar",
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
        id=str(uuid.uuid4())
        nombre_producto=self.txt_producto.get()
        tipo=self.txt_tipos.get()
        cantidad=self.txt_cantidad.get()
        descripcion=self.txt_descripcion.get()


        id_producto=self.servicio_productos.obtener_por_nombre(nombre_producto)
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

        

        try:
          movimiento= Movimiento(id, id_producto.id_producto, nombre_producto , tipo, cantidad, fecha, descripcion)
          if tipo=="Ingreso":
           self.servicio_movimientos.registrar_entrada(movimiento)
          else:
            self.servicio_movimientos.registrar_salida(movimiento)
          messagebox.showinfo("Exito", "Movimiento guardado", parent=self.ventana)
          self.al_guardar()
          self.ventana.destroy()
          return
        except ValueError as error: 
             messagebox.showerror("Error al registrar movimiento", str(error), parent=self.ventana)
             return



