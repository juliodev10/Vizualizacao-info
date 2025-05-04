import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Carregar dados
df = pd.read_csv("dados.csv")

# Calcular densidade demográfica
df["Densidade"] = df["População"] / df["Área_km2"]

# Ordenar para melhor visualização
df = df.sort_values(by="Densidade", ascending=False)

# Criar Treemap
plt.figure(figsize=(14, 8))
squarify.plot(
    sizes=df["Densidade"],
    label=[f"{estado}\n{dens:.0f} hab/km²" for estado, dens in zip(df["Estado"], df["Densidade"])],
    color=plt.cm.viridis(df["Densidade"] / max(df["Densidade"])),
    alpha=0.8
)

plt.title("Densidade Demográfica dos Estados Brasileiros (Treemap)", fontsize=18)
plt.axis("off")
plt.tight_layout()
plt.show()