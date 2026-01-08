from flask import Flask, render_template
import mysql.connector as mysql

# Conexión a la base de datos
def get_db_connection():
    return mysql.connect(
        host='localhost',
        user='tiendaPatos',
        password='tiendaPatos*123$',
        database='tienda_patitos'
    )

app = Flask(__name__)

@app.route("/")
def inicio():

    return render_template("inicio.html")

@app.route("/productos")
def productos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vw_productos_pato")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("productos.html", productos=productos)
    
@app.route("/pedidos")
def pedidos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vw_pedidos_con_clientes")
    pedidos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("pedidos.html", pedidos=pedidos)

@app.route("/pedido/<int:id_pedido>")
def detalle_pedido(id_pedido):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vw_lineas_pedido_detalle WHERE id_pedido = %s", (id_pedido,))
    lineas = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("detalle_pedido.html", lineas=lineas, id_pedido=id_pedido)

if __name__ == "__main__":
    app.run(debug=True)