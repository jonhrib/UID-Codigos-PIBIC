    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

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

    # Carregar os dados da planilha
    dados = pd.read_excel('C:\\Users\\jonhv\\OneDrive\\Documentos\\AnálisesUID\\Cópia de UID.xlsx')

    # Obter todas as cores únicas
    cores_unicas = dados['Caracteristc color'].unique()

    # Calcular a contagem de cada cor característica por categoria
    dados_tabela_cores = [['Category³', 'Caracteristc color', 'Contagem', 'Porcentagem']]
    cores_por_categoria = {}

    for categoria, dados_categoria in dados.groupby('Category³'):
        contagem_cores = dados_categoria['Caracteristc color'].value_counts().reindex(cores_unicas, fill_value=0)
        total_ocorrencias = contagem_cores.sum()
        porcentagens = (contagem_cores / total_ocorrencias) * 100

        for cor, contagem, porcentagem in zip(contagem_cores.index, contagem_cores.values, porcentagens.values):
            dados_tabela_cores.append([categoria, cor, contagem, porcentagem])

    # Converter os dados em um DataFrame
    df_cores = pd.DataFrame(dados_tabela_cores[1:], columns=dados_tabela_cores[0])

    # Criar uma matriz de contagem de cores por categoria
    matriz_cores = df_cores.pivot(index='Category³', columns='Caracteristc color', values='Porcentagem').fillna(0)

    # Renomear as colunas da matriz de acordo com o dicionário de tradução
    matriz_cores.rename(columns=traducao_cores, inplace=True)

    matriz_cores = matriz_cores.reindex(columns=list(traducao_cores.values()))

    plt.figure(figsize=(18, 10.5)) 

    # Ajustar os rótulos dos eixos para melhorar a legibilidade
    plt.yticks(rotation=0, fontstyle='italic')

    # sns.set(font_scale=1.2, rc={'axes.grid': False}) 

    # Criar o mapa de calor com anotações
    heatmap = sns.heatmap(
        matriz_cores, 
        cmap='gist_heat_r', 
        annot=True,  # Adicionar anotações
        fmt=".2f", 
        annot_kws={"size": 8},  # Ajustar o tamanho das anotações
        linewidths=0.1,
        square=False  # Permitir que os quadrados sejam ajustados para caber na figura
        )

    plt.gca().set_aspect('auto', 'box')

    # Ajustar os rótulos dos eixos para melhorar a legibilidade
    plt.xticks(rotation=90, fontstyle='italic')

    # Definir o título do mapa de calor
    heatmap.set_title('Occurrences of Characteristic Colors by Category')

    plt.setp(heatmap.get_yticklabels(), rotation=0, fontsize=10, fontstyle='italic')

    # Salvar a figura em um arquivo PDF
    plt.savefig("Ocorrencias_Cores_Categorias_Valores.pdf", format='pdf', bbox_inches='tight')

    # # Mostrar o mapa de calor
    # plt.show()
