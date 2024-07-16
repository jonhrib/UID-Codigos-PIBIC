import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import combinations
from scipy.stats import chi2_contingency

# Carregar os dados da planilha
dados = pd.read_excel("C:\\Users\\jonhv\\OneDrive\\Documentos\\AnálisesUID\\Cópia de UID.xlsx")

# Selecionar da coluna 50 até a penúltima coluna
component_columns = dados.iloc[:, 49:-2]

# Inicializar um dicionário para armazenar os resultados do teste qui-quadrado
chi2_results = {}

# Calcular o teste qui-quadrado para cada par de componentes
for combo in combinations(component_columns.columns, 2):
    contingency_table = pd.crosstab(dados[combo[0]], dados[combo[1]])
    chi2, _, _, _ = chi2_contingency(contingency_table)
    chi2_results[combo] = chi2

# Criar DataFrame com os valores do qui-quadrado
chi2_df = pd.DataFrame(chi2_results.values(), index=pd.MultiIndex.from_tuples(chi2_results.keys()), columns=['Chi2'])

# Transformar os índices em colunas para facilitar a visualização
chi2_df.reset_index(inplace=True)
chi2_df.columns = ['Component1', 'Component2', 'Chi2']

# Pivotar o DataFrame para o formato adequado ao heatmap
chi2_pivot = chi2_df.pivot(index='Component1', columns='Component2', values='Chi2')

# Preencher valores NaN com 0 (ou algum valor apropriado)
chi2_pivot = chi2_pivot.fillna(0)

# Ajustar o tamanho da figura para garantir que todos os componentes sejam exibidos corretamente
plt.figure(figsize=(14, 12))
heatmap = sns.heatmap(chi2_pivot, cmap='gist_heat_r', annot=False, linewidths=0.1)
heatmap.set_title('Association between Components - Chi Square')

plt.xticks(fontstyle='italic')
plt.yticks(rotation=0, fontstyle='italic')

# plt.setp(heatmap.get_yticklabels(), rotation=0, fontsize=10, fontstyle='italic')
# plt.setp(heatmap.get_xticklabels(), rotation=0, fontsize=10, fontstyle='italic')

# Salvar a figura em um arquivo PDF
plt.savefig("QuiQuadrado.pdf", format='pdf', bbox_inches='tight')

# # Mostrar o mapa de calor
# plt.show()
