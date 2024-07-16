import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Dicionário de tradução de cores
traducao_cores = {
    'Red': 'Vermelho',
    'Orange': 'Laranja',
    'Yellow': 'Amarelo',
    'Green': 'Verde',
    'Blue': 'Azul',
    'Indigo': 'Índigo',
    'Violet': 'Violeta',
    'Black': 'Preto'
}

# Carregar os dados da planilha (substitua pelo seu caminho)
dados = pd.read_excel('C:\\Users\\jonhv\\OneDrive\\Documentos\\AnálisesUID\\Cópia de UID.xlsx')

# Selecionar apenas as colunas de componentes e cores características
componentes_cores = dados.iloc[:, 49:-2]  # Selecionar da coluna 50 até a penúltima coluna

# Criar uma matriz de contagem de cores por componente
matriz_cores_componentes = componentes_cores.groupby(dados['Caracteristc color']).mean()

# Renomear os índices da matriz de acordo com o dicionário de tradução
matriz_cores_componentes.rename(index=traducao_cores, inplace=True)

# Transpor a matriz para trocar as posições dos eixos
matriz_componentes_cores = matriz_cores_componentes.T

# Ordenar as colunas e índices de acordo com as listas de componentes
matriz_componentes_cores = matriz_componentes_cores.reindex(index=componentes_estruturais + componentes_navegacionais + componentes_entrada + componentes_informativos + outros_componentes,
                                                            columns=list(traducao_cores.values()))

# Ajustar o tamanho da figura
plt.figure(figsize=(18, 16))  # Ajustar o tamanho da figura para acomodar os rótulos

for i in [len(componentes_estruturais), len(componentes_estruturais) + len(componentes_navegacionais), 
          len(componentes_estruturais) + len(componentes_navegacionais) + len(componentes_entrada), 
          len(componentes_estruturais) + len(componentes_navegacionais) + len(componentes_entrada) + len(componentes_informativos)]:
    plt.axhline(i, color='green', linewidth=1.0)
    # plt.axvline(i, color='black', linewidth=0.5)

# Criar o mapa de calor para associar as cores e os componentes
ax = sns.heatmap(
    matriz_componentes_cores, 
    cmap='gist_heat_r', 
    annot=True,  # Adicionar anotações
    fmt=".2f", 
    annot_kws={"size": 9},  # Ajustar o tamanho das anotações
    cbar=True,
    linewidths=0.1,  # Adicionar linhas entre os quadrados para melhor visualização
    square=False  # Permitir que os quadrados sejam ajustados para caber na figura
)

# Ajustar a proporção dos quadrados para auto
ax.set_aspect('auto')

# Ajustar os rótulos dos eixos para melhorar a legibilidade
plt.setp(ax.get_yticklabels(), rotation=0, fontsize=10, fontstyle='italic')

# Ajustar os rótulos dos eixos para melhorar a legibilidade
plt.xticks(rotation=90)
plt.yticks(rotation=0)

# # Adicionar anotações para os grupos ao lado esquerdo das linhas
# plt.text(-1, len(componentes_estruturais) / 2, 'Structural C.', rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8, fontstyle='italic')
# plt.text(-1, len(componentes_estruturais) + len(componentes_navegacionais) / 2, 'Navigational C.', rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8, fontstyle='italic')
# plt.text(-1, len(componentes_estruturais) + len(componentes_navegacionais) + len(componentes_entrada) / 2, 'Input C.', rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8, fontstyle='italic')
# plt.text(-1, len(componentes_estruturais) + len(componentes_navegacionais) + len(componentes_entrada) + len(componentes_informativos) / 2, 'Informative C.', rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8, fontstyle='italic')
# plt.text(-1, len(componentes_estruturais) + len(componentes_navegacionais) + len(componentes_entrada) + len(componentes_informativos) + len(outros_componentes) / 2, 'Other C.', rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=8, fontstyle='italic')

# # Ajustar os limites do eixo x para acomodar o texto adicional
# plt.xlim(-2, len(ordem_componentes))

# Definir o título do mapa de calor
# ax.set_title('Occurrences of Components by Characteristic Colors')

# Salvar a figura em um arquivo PDF
plt.savefig("Associacao_Cores_Componentes_Valores.pdf", format='pdf', bbox_inches='tight')

# Exibir o mapa de calor
# plt.show()
