import pandas as pd
import os
from atividade1 import (
    gerar_dados_csv,
    salvar_csv,
    carregar_dados_to_df,
    calcular_valor_total,
    filtrar_produtos_vl_maior_500,
    salvar_resultado_csv
)

def test_gerar_dados_csv():
    dados = gerar_dados_csv(5)  # Gera 5 linhas de dados
    assert len(dados) == 5, "O número de linhas gerado deve ser igual ao solicitado"
    for linha in dados:
        assert len(linha) == 3, "Cada linha deve conter 3 colunas: produto, quantidade e preço unitário"
        assert isinstance(linha[0], str), "O primeiro elemento (produto) deve ser uma string"
        assert isinstance(linha[1], int), "O segundo elemento (quantidade) deve ser um inteiro"
        assert isinstance(linha[2], float), "O terceiro elemento (preço unitário) deve ser um float"

def test_salvar_e_carregar_csv():
    dados = [["Banana", 2, 10.5], ["Melancia", 3, 15.0]]
    nome_arquivo = "teste_vendas.csv"
    salvar_csv(nome_arquivo, dados)
    assert os.path.exists(nome_arquivo), "O arquivo CSV deve ser criado"

    df = carregar_dados_to_df(nome_arquivo)
    assert not df.empty, "O DataFrame carregado não deve estar vazio"
    assert list(df.columns) == ["produto", "quantidade", "preco_unitario"], "As colunas do DataFrame devem estar corretas"
    os.remove(nome_arquivo)  # Limpa o arquivo de teste

def test_calcular_valor_total():
    dados = {"produto": ["Banana", "Melancia"], "quantidade": [2, 3], "preco_unitario": [10.5, 15.0]}
    df = pd.DataFrame(dados)
    calcular_valor_total(df)
    assert "valor_total" in df.columns, "A coluna 'valor_total' deve ser adicionada ao DataFrame"
    assert df.loc[0, "valor_total"] == 21.0, "O valor total para a primeira linha está incorreto"
    assert df.loc[1, "valor_total"] == 45.0, "O valor total para a segunda linha está incorreto"

def test_filtrar_produtos_vl_maior_500():
    dados = {
        "produto": ["Banana", "Melancia", "Abacaxi"],
        "quantidade": [10, 30, 2],
        "preco_unitario": [50.0, 20.0, 300.0],
        "valor_total": [500.0, 600.0, 600.0]
    }
    df = pd.DataFrame(dados)
    filtro = filtrar_produtos_vl_maior_500(df)
    assert len(filtro) == 2, "Deve haver 2 produtos com valor total maior que 500"
    assert filtro.iloc[0]["produto"] == "Melancia", "O primeiro produto filtrado deve ser Melancia"
    assert filtro.iloc[1]["produto"] == "Abacaxi", "O segundo produto filtrado deve ser Abacaxi"

def test_salvar_resultado_csv():
    dados = {"produto": ["Banana", "Melancia"], "quantidade": [2, 3], "preco_unitario": [10.5, 15.0], "valor_total": [21.0, 45.0]}
    df = pd.DataFrame(dados)
    nome_arquivo_saida = "teste_vendas_resultado.csv"
    salvar_resultado_csv(df, nome_arquivo_saida)
    assert os.path.exists(nome_arquivo_saida), "O arquivo de resultado deve ser criado"
    df_carregado = pd.read_csv(nome_arquivo_saida, delimiter=';')
    assert not df_carregado.empty, "O arquivo de saída não deve estar vazio"
    os.remove(nome_arquivo_saida)  # Limpa o arquivo de teste