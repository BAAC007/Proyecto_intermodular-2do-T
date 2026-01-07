from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def cv():
    with open("datos.json", encoding="utf-8") as f:
        data = json.load(f)
    return render_template("curriculum.html", **data)

if __name__ == "__main__":
    app.run(debug=True)