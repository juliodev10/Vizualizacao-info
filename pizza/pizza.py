import pandas as pd
import  matplotlib.pyplot as plt
# Carregar dados de um CSV
try:
    d = pd.read_csv('densidade.csv', encoding='utf-8')  
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome e o caminho do arquivo.")
    exit()
# Extrai dados para o gráfico
estados = d['Região']
densidade = d['Densidade']

# Cria o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(densidade, labels=estados, autopct='%1.1f%%', startangle=120)
plt.title('Distribuição da Densidade Demográfica por Estado')
plt.axis('equal')  # Deixa o gráfico redondo
plt.show()