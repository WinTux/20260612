from flask import Flask, render_template
import pandas as pd
import matplotlib

# Evita problemas en servidores sin interfaz gráfica
matplotlib.use("Agg")

import matplotlib.pyplot as plt

app = Flask(__name__)


def obtener_resumen():
    df = pd.read_csv("ventas.csv")

    df["total"] = df["cantidad"] * df["precio"]

    resumen = (
        df.groupby("producto")
        .agg(
            unidades_vendidas=("cantidad", "sum"),
            ingresos=("total", "sum")
        )
        .reset_index()
    )

    return resumen


def generar_grafico(resumen):
    plt.figure(figsize=(8, 4))
    plt.bar(
        resumen["producto"],
        resumen["ingresos"],
        color="steelblue"
    )
    plt.title("Ingresos por producto")
    plt.xlabel("Producto")
    plt.ylabel("Ingresos ($)")
    plt.tight_layout()
    plt.savefig("static/reporte_ingresos.png")
    plt.close()


@app.route("/")
def index():
    resumen = obtener_resumen()

    generar_grafico(resumen)

    producto_top = resumen.loc[
        resumen["unidades_vendidas"].idxmax()
    ]

    return render_template(
        "index.html",
        resumen=resumen.to_dict(orient="records"),
        producto_top=producto_top["producto"],
        unidades_top=producto_top["unidades_vendidas"]
    )


if __name__ == "__main__":
    app.run(debug=True)
