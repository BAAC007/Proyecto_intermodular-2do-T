from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return "hola"

if __name__ == "__main__":
    app.run(debug=True)