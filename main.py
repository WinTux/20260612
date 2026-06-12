import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv("ventas.csv")

# Crear columna de total vendido
df["total"] = df["cantidad"] * df["precio"]

print("=== DATOS DE VENTAS ===")
print(df)

# Agrupar por producto
resumen = (
    df.groupby("producto")
      .agg(
          unidades_vendidas=("cantidad", "sum"),
          ingresos=("total", "sum")
      )
      .reset_index()
)

print("\n=== RESUMEN ===")
print(resumen)

# Producto más vendido
mas_vendido = resumen.loc[
    resumen["unidades_vendidas"].idxmax()
]

print(
    f"\nProducto más vendido: "
    f"{mas_vendido['producto']} "
    f"({mas_vendido['unidades_vendidas']} unidades)"
)

# Gráfico
plt.figure(figsize=(8, 5))
plt.bar(
    resumen["producto"],
    resumen["ingresos"]
)
plt.title("Ingresos por producto")
plt.xlabel("Producto")
plt.ylabel("Ingresos ($)")
plt.tight_layout()
plt.savefig("reporte_ingresos.png")

print("\nGráfico generado: reporte_ingresos.png")
