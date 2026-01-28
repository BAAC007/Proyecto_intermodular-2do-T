from flask import Flask, render_template

app = Flask(__name__)

mis_frutas = ["peras","manzanas","platanos","fresas"]

@app.route("/")
def lista():
    return render_template("lista.html", frutas = mis_frutas)

if __name__ == "__main__":
    app.run(debug=True)