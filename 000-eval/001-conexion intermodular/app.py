from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  nombre = "Bryan"
  edad = 19
  return f"<h1>Bienvenido {nombre}</h1><p>Edad: {edad} años</p>"
  
if __name__ == "__main__":
  aplicacion.run(debug=True)
