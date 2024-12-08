# Importar bibliotecas necessárias
import matplotlib.pyplot as plt

# Dados fictícios simulando a situação pandêmica
semanas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
casos_doenca = [20, 480, 400, 700, 100, 1000, 500, 300, 150, 25]  # Casos subindo inicialmente e depois caindo
# pessoas_vacinadas = [0,  20, 100, 80, 400, 0, 500, 700, 900, 950]  # Vacinação aumentando
campanha_rua = [0,  0, 0, 50, 320, 20, 700, 900, 1000, 950]  # Campanha de rua
campanha_rede = [0,  100, 100, 200, 0, 600, 0, 250, 100, 150]  # Campanha Redes

# Visualização da situação pandêmica
plt.figure(figsize=(12, 6))

# Plotar os dados
plt.plot(semanas, casos_doenca, marker='o', label='Casos da Doença', color='red', linewidth=2)
# plt.plot(semanas, pessoas_vacinadas, marker='s', label='Pessoas Vacinadas', color='green', linewidth=2)
# plt.plot(semanas, campanha_rua, marker='D', label='Campanha de Rua', color='blue', linewidth=2)
plt.plot(semanas, campanha_rede, marker='^', label='Campanha Online', color='orange', linewidth=2)

# Configurações do gráfico
plt.title('Eficácia das Campanhas na Situação Pandêmica', fontsize=16, fontweight='bold')
plt.xlabel('Semanas', fontsize=14)
plt.ylabel('Número de Pessoas', fontsize=14)
plt.xticks(semanas)
plt.legend(title='Legenda', title_fontsize='13', fontsize='12')
plt.grid(alpha=0.5)
plt.tight_layout()  # Ajustar o layout
plt.show()
