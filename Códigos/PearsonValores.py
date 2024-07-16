import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados da planilha
dados = pd.read_excel("C:\\Users\\jonhv\\OneDrive\\Documentos\\AnálisesUID\\Cópia de UID.xlsx")

# Selecionar da coluna 50 até a penúltima coluna
component_columns = dados.iloc[:, 49:-2]

# # Substituir 'True' por 1 e 'False' por 0
# component_columns = component_columns.replace({True: 1, False: 0})

# Calcular a matriz de correlação de Pearson
correlacao_pearson = component_columns.corr(method='pearson')

# Listas de componentes por categoria
componentes_estruturais = [
    'Botton app bar', 'Card list', 'Carousel', 'Common button', 'Divider', 'Extended FAB', 
    'Floating Action Button', 'Grid layout', 'Icon button', 'Images', 'List', 'Text view', 'Top app bar'
]
componentes_navegacionais = [
    'Chip', 'Menu', 'Navigation bar', 'Navigation drawer', 'Navigation rail', 'Primary tab', 
    'Secondary tab', 'Segmented Buttons'
]
componentes_entrada = [
    'Bottom sheet', 'Checkbox', 'Date picker', 'Dial time picker', 'Input time picker ', 
    'Full-screen dialog', 'Radio button', 'Side sheet', 'Slider', 'Switch', 'Text field'
]
componentes_informativos = [
    'Badge', 'Circular progress indicator', 'Linear progress indicator', 'Pre-loading indicator', 
    'Snackbar', 'Sound Effects', 'Tool tip'
]
outros_componentes = [
    'Account required', 'Background music', 'Default night mode', 'Dialog', 'Landscape mode', 'Map View', 
    'Search', 'Social interaction', 'Videos', 'Web component'
]

# Ordem desejada dos componentes
ordem_componentes = (
    componentes_estruturais + componentes_navegacionais + 
    componentes_entrada + componentes_informativos + 
    outros_componentes
)

# Reorganizar a matriz de correlação de Pearson conforme a ordem dos componentes
correlacao_pearson = correlacao_pearson.reindex(index=ordem_componentes, columns=ordem_componentes)

# Ajustar o tamanho da figura
plt.figure(figsize=(18, 16))  # Ajustar o tamanho da figura para acomodar os rótulos

# Criar o mapa de calor da matriz de correlação de Pearson
heatmap = sns.heatmap(
    correlacao_pearson, 
    cmap='gist_heat_r', 
    annot=True,  # Adicionar anotações
    fmt=".2f",   # Formato dos valores
    annot_kws={"size": 4},  # Ajustar o tamanho das anotações
    #cbar_kws= {'location': 'top'},
    # xticklabels=True, 
    # yticklabels=True, 
    linewidths=0.1
)

# Adicionar linhas para destacar as categorias
for i in [len(componentes_estruturais), len(componentes_estruturais) + len(componentes_navegacionais), 
          len(componentes_estruturais) + len(componentes_navegacionais) + len(componentes_entrada), 
          len(componentes_estruturais) + len(componentes_navegacionais) + len(componentes_entrada) + len(componentes_informativos)]:
    plt.axhline(i, color='green', linewidth=0.8)
    plt.axvline(i, color='green', linewidth=0.8)

# Adicionar anotações para os grupos ao lado esquerdo das linhas
plt.text(-1, len(componentes_estruturais) / 2, 'Structural C.', rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8, fontstyle='italic')
plt.text(-1, len(componentes_estruturais) + len(componentes_navegacionais) / 2, 'Navigational C.', rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8, fontstyle='italic')
plt.text(-1, len(componentes_estruturais) + len(componentes_navegacionais) + len(componentes_entrada) / 2, 'Input C.', rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8, fontstyle='italic')
plt.text(-1, len(componentes_estruturais) + len(componentes_navegacionais) + len(componentes_entrada) + len(componentes_informativos) / 2, 'Informative C.', rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8, fontstyle='italic')
plt.text(-1, len(componentes_estruturais) + len(componentes_navegacionais) + len(componentes_entrada) + len(componentes_informativos) + len(outros_componentes) / 2, 'Other C.', rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8, fontstyle='italic')

# Ajustar os limites do eixo x para acomodar o texto adicional
plt.xlim(-2, len(ordem_componentes))

# Ajustar os rótulos dos eixos para melhorar a legibilidade
plt.xticks(rotation=90, fontstyle='italic')
plt.yticks(rotation=0, fontstyle='italic')

# Definir o título do mapa de calor
#heatmap.set_title('Pearson Correlation between Components')

# Salvar a figura em um arquivo PDF
plt.savefig("Correlacao_Pearson_Valores.pdf", format='pdf', bbox_inches='tight')

# # Mostrar o mapa de calor
# plt.show()
