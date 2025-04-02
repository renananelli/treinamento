import pandas as pd
import csv
import random
import os

def gerar_dados_csv(num_linhas):
    dados = []
    for _ in range(num_linhas):
        produto = random.choice(['Pera', 'Banana', 'Laranja', 'Abacaxi', 'Melancia', 'Morango', 'Azeitona'])
        quantidade = random.randint(1, 4)  
        preco_unitario = round(random.uniform(10.0, 1000.0), 2)  
        dados.append([produto, quantidade, preco_unitario])
    return dados

def salvar_csv(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        arquivo = csv.writer(arquivo_csv, delimiter=';')
        arquivo.writerow(['produto', 'quantidade', 'preco_unitario']) 
        arquivo.writerows(dados)  

def carregar_dados_to_df(nome_arquivo):
        df = pd.read_csv(nome_arquivo, delimiter=';')
        print(df)
        return(df)

def calcular_valor_total(df):
    df['valor_total'] = df['quantidade'] * df['preco_unitario']
    print(df)

def filtrar_produtos_vl_maior_500(df):
    filtro = df[df['valor_total'] > 500]
    print(filtro)
    return filtro

def salvar_resultado_csv(df, nome_arquivo_saida):
    df.to_csv(nome_arquivo_saida, index=False, sep=';', encoding='utf-8')
    print(f"Resultado salvo em {nome_arquivo_saida}.")

def main():
    dados = gerar_dados_csv(7)
    arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vendas.csv')

    salvar_csv(arquivo, dados)
    print("Arquivo 'vendas.csv' criado com sucesso!")
    
    df_criado = carregar_dados_to_df(arquivo)
    print(calcular_valor_total(df_criado))
    df_filtrado = filtrar_produtos_vl_maior_500(df_criado)
    
    arquivo_novo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vendas_resultado.csv')
    salvar_resultado_csv(df_filtrado, arquivo_novo)
    
if __name__ == "__main__":
    main()










# # Uso das funções
# nome_arquivo_entrada = "vendas.csv"  # Substitua pelo nome do seu arquivo de entrada
# nome_arquivo_saida = "vendas_filtradas.csv"  # Substitua pelo nome do arquivo de saída

# dados = carregar_dados(nome_arquivo_entrada)

# if dados is not None:
#     dados = calcular_valor_total(dados)
#     produtos_filtrados = filtrar_produtos(dados)
#     salvar_resultado(produtos_filtrados, nome_arquivo_saida)