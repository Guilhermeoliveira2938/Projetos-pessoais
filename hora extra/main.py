import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    sal_bruto = float(request.form["salario"])
    porcent_dia = int(request.form["porcentagem"])
    horas = float(request.form["horas"])

    val_hora = sal_bruto / 220

    if porcent_dia == 50:
        val_extra = val_hora * 1.5
    else:
        val_extra = val_hora * 2

    pagar = val_extra * horas

    return render_template("index.html",
        val_hora=round(val_hora, 2),
        val_extra=round(val_extra, 2),
        pagar=round(pagar, 2)
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))