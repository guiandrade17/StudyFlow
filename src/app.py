from flask import Flask, render_template, request
from src.core import calcular_proxima_revisao, obter_frase
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "../templates"))

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    frase = None

    if request.method == "POST":
        dias = int(request.form["dias"])
        resultado = calcular_proxima_revisao(dias)
        frase = obter_frase()

    return render_template("index.html", resultado=resultado, frase=frase)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)