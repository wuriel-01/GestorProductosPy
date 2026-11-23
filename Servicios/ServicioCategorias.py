from Datos.categoriaDAO import CategoriaDAO
class ServicioCategorias:
    def __init__(self):
        self.categoria_dao= CategoriaDAO()

    def obtener_todas(self):
        return self.categoria_dao.obtener_todas()

    def obtener_por_nombre(self, nombre):
        if not nombre:
            raise ValueError("nombre invalido")

        categoria_por_nombre=self.categoria_dao.obtener_por_nombre(nombre)

        if categoria_por_nombre is None:
            raise ValueError("no se encontro categoria con ese nombre")

        return categoria_por_nombre

    def obtener_por_id(self, id):
        if not id:
            raise ValueError("el ID es invalido")

        categoria_por_id= self.categoria_dao.obtener_por_id(id)

        if categoria_por_id is None:
            raise ValueError("no se encontro categoria con ese ID")

        return categoria_por_id