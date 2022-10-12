import sqlite3
from sqlite3 import Error
from config_db import BD

bd = BD()

class Productos():
    def select(self):
        conexion = bd.conectar_bd()
        conexion.row_factory = sqlite3.Row
        sentencia_sql = "SELECT * FROM productos"
        try:
            cursor = conexion.cursor()
            cursor.execute(sentencia_sql)
            fila_producto = cursor.fetchall()
            productos = [ dict(fila) for fila in fila_producto ]
            return productos
        except Error as e:
            print(f"Error seleccionando todos los productos: {str(e)}.")
        finally:
            conexion.close()

    def select_by_id(self, id):
        conexion = bd.conectar_bd()
        sentencia_sql = f"SELECT * FROM productos WHERE id = {id}"
        conexion.row_factory = sqlite3.Row # convert row object to dictionary
        try:
            cursor = conexion.cursor()
            cursor.execute(sentencia_sql)
            producto = dict(cursor.fetchone())
            return producto
        except Error as e:
            print(f"Error seleccionando el producto: {str(e)}.")
        finally:
            conexion.close()

    def insert(self, producto):
        conexion = bd.conectar_bd()
        sentencia_sql = "INSERT INTO productos (descripcion, precio) VALUES (?, ?)"
        parametros = (producto["descripcion"], producto["precio"])
        try:
            cursor = conexion.cursor()
            cursor.execute(sentencia_sql, parametros)
            conexion.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error creando el producto: {str(e)}")
            return False
        finally:
            conexion.close()

    def update(self, id, producto):
        conexion = bd.conectar_bd()
        sentencia_sql = "UPDATE productos SET descripcion = ?, precio = ? WHERE id =?"
        parametros = (producto["descripcion"], producto["precio"], id)
        try:
            cursor = conexion.cursor()
            cursor.execute(sentencia_sql, parametros)
            conexion.commit()
            producto_actualizado = self.select_by_id(id)
            return producto_actualizado
        except Error as e:
            print(f"Error actualizando el producto: {str(e)}.")
            return False
        finally:
            conexion.close()


    def delete(self, id):
        conexion = bd.conectar_bd()
        sentencia_sql = f"DELETE from productos WHERE id = {id}"
        mensaje = {}
        try:
            cursor = conexion.cursor()
            cursor.execute(sentencia_sql)
            conexion.commit()
            mensaje["status"] = "Producto eliminado con éxito."
            return mensaje
        except Error as e:
            print(f"Error al eliminar el producto: {str(e)}.")
        finally:
            conexion.close()
