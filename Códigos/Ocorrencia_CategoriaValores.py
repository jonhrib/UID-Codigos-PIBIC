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

# Carregar os dados da planilha
dados = pd.read_excel('C:\\Users\\jonhv\\OneDrive\\Documentos\\AnálisesUID\\Cópia de UID.xlsx')

# Selecionar apenas as colunas de componentes na ordem desejada
componentes_selecionados = dados[ordem_componentes]

# Calcular a frequência de cada componente em cada categoria
frequencia_por_categoria = componentes_selecionados.groupby(dados['Category³']).mean()

# Ajustar o tamanho da figura
plt.figure(figsize=(18, 16))  # Ajustar o tamanho da figura para que não fique muito grande

for i in [len(componentes_estruturais), len(componentes_estruturais) + len(componentes_navegacionais), 
          len(componentes_estruturais) + len(componentes_navegacionais) + len(componentes_entrada), 
          len(componentes_estruturais) + len(componentes_navegacionais) + len(componentes_entrada) + len(componentes_informativos)]:
    plt.axhline(i, color='green', linewidth=1.0)
    # plt.axvline(i, color='black', linewidth=0.5)

# Criar o mapa de calor
heatmap = sns.heatmap(
    frequencia_por_categoria.T,  # Transpor os dados para colocar categorias na parte superior
    cmap='gist_heat_r', 
    annot=True,  # Adicionar anotações
    fmt=".2f", 
    annot_kws={"size": 8},  # Ajustar o tamanho das anotações
    linewidths=0.1,
    square=False
)

# Ajustar a proporção dos quadrados para auto
heatmap.set_aspect('auto')

# Ajustar a proporção dos quadrados
# heatmap.set_aspect(aspect=0.5)  # Ajustar a proporção dos quadrados

# Definir o título do mapa de calor
# heatmap.set_title('Frequency of Components by Category')

# Colocar os rótulos dos componentes acima do mapa de calor
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False, labeltop=True)

# Ajustar os rótulos dos eixos para melhorar a legibilidade
plt.xticks(rotation=90, fontstyle='italic')
plt.yticks(rotation=0, fontstyle='italic')

# Salvar a figura em um arquivo PDF com tamanho ajustado ao conteúdo
plt.savefig("Ocorrencias_Componentes_Categorias_Valores.pdf", format='pdf', bbox_inches='tight')
