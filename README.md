# Simple API con Flask y SQLite3

Archivos:
- config_db.py: configuración de la base de datos y creación de tablas.
- producto.py: consultas a la base de datos.
- app.py: creación y configuración de la aplicación, creación de rutas.

Rutas:
1. GET      /productos
2. POST     /productos
4. PUT      /productos/<id>
5. DELETE   /productos/<id>
6. GET      /productos/<id>

Tabla producto:
- id: int
- descripcion: str
- precio: float
