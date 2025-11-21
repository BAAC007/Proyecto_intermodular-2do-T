#Importo la libreria flask, para crear webs
from flask import Flask, render_template
import json

#Creo una nueva aplicacion
app = Flask(__name__)

#Escucho en la ruta raiz
@app.route("/")
def inicio():

    return render_template("inicio.html")

@app.route("/sobremi")
def sobremi():

    return render_template("sobremi.html")
@app.route("/contacto")
def contacto():

    return render_template("contacto.html")

#Si este archivo no es una libreria y es el archivo principal
if __name__ == "__main__":
    app.run(debug=True)