#Importo la libreria flask, para crear webs
from flask import Flask, render_template

#Creo una nueva aplicacion
app = Flask(__name__)

#Escucho en la ruta raiz
@app.route("/")
def inicio():
    # Mi nombre es la variable que esta en python
    mi_nombre = "Bryan Avila"
    # Nombre es la variable que lanzo a la plantilla
    return render_template("variable.html", nombre = mi_nombre)

#Si este archivo no es una libreria y es el archivo principal
if __name__ == "__main__":
    app.run(debug=True)