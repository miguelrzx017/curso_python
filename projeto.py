import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta

def gera_dados_ficticios(num_registros = 600):
    """
    Gera um DataFrame do pandas com dados de vendas ficticios.
    """
    print(f"\nIniciando a geração de {num_registros} registros de vendas ficticias...")

    produtos = {
        'Stratocaster': {'categoria': 'guitarras', 'preco': 11500.00},
        'Les Paul': {'categoria': 'guitarras', 'preco': 12000.00},
        'SG': {'categoria': 'guitarras', 'preco': 11500.00}
    }

    lista_produtos = list(produtos.keys())

    cidades_estados = {
        'São Paulo': 'SP',
        'Rio de Janeiro': 'RJ'  
    }

    lista_cidades = list(cidades_estados.keys())

    dados_vendas = []

    data_inicial = datetime(2026, 1, 1)

    for i in range(num_registros):
        produto_nome = random.choice(lista_produtos)
        cidade = random.choice(lista_cidades)
        quantidade = np.random.randint(1, 8)
        data_pedido = data_inicial + timedelta(days = int(i/S), hours = random.randint(0, 23))

        if produto_nome in ['Stratocaster', 'Les Paul']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome]['preco']

        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitário': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'Id_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })

        print("Geração de dados concluída.\n")
    return pd.DataFrame(dados_vendas)

    df_vendas = gera_dados_ficticios(500)
    type(df_vendas)
    df_vendas.shape
    df_vendas.head()
    df_vendas.info()
    df_vendas.describe()
    df_vendas.dtypes
