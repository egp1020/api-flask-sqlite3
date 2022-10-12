from flask import Flask, render_template, jsonify, request
from productos import Productos
from config_db import BD



app = Flask(__name__)
bd = BD()
p = Productos()


@app.route("/")
@app.route("/index")
def index_views():
    return render_template("index.html")

@app.route("/productos/")
def get_productos():
    productos = p.select()
    return jsonify(productos)

@app.route("/productos/", methods=["POST"])
def post_producto():
    datos_producto = request.get_json()
    resultado = p.insert(datos_producto)
    return jsonify(resultado)

@app.route("/productos/<id>/", methods=["PUT"])
def put_producto(id):
    datos_producto = request.get_json()
    resultado = p.update(id, datos_producto)
    return jsonify(resultado)

@app.route("/productos/<id>/", methods=["DELETE"])
def delete_producto(id):
    resultado = p.delete(id)
    return jsonify(resultado)

@app.route("/productos/<id>/", methods=["GET"])
def get_by_id_producto(id):
    producto = p.select_by_id(id)
    return jsonify(producto)


if __name__ == "__main__":
    bd.crear_tabla()
    app.run(debug = True)

