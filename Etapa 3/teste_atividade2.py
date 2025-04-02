from tabulate import tabulate
import random

def cria_dicionario_alunos_notas():
    dicionario_alunos = {
        "Rodrigo": [],
        "Renan": [],
        "Roberto": [],
        "Ana": [],
        "Claudia": [],
        "Maria": []
    }

    for aluno in dicionario_alunos.keys():
        dicionario_alunos[aluno] = [random.randint(1, 10) for _ in range(10)]

    return dicionario_alunos

def calcula_media_alunos(dicionario_alunos):
    medias = {}
    for aluno, notas in dicionario_alunos.items():
        medias[aluno] = sum(notas) / len(notas)
    return medias

def identifica_alunos_aprovados(medias):
    aprovados = {}
    for aluno, media in medias.items():
        aprovados[aluno] = "Aprovado" if media >= 7 else "Reprovado"
    return aprovados

def gerar_relatorio(dicionario_alunos):
    medias = calcula_media_alunos(dicionario_alunos)
    aprovados = identifica_alunos_aprovados(medias)

    tabela = []
    for aluno in dicionario_alunos.keys():
        tabela.append([aluno, f"{medias[aluno]:.2f}", aprovados[aluno]])

    return tabulate(tabela, headers=["Aluno", "Média", "Status"], tablefmt="grid")

# Testes com pytest
def test_cria_dicionario_alunos_notas():
    dicionario = cria_dicionario_alunos_notas()
    assert isinstance(dicionario, dict), "O retorno deve ser um dicionário"
    for aluno, notas in dicionario.items():
        assert len(notas) == 10, f"O aluno {aluno} deve ter 10 notas"
        assert all(1 <= nota <= 10 for nota in notas), f"Todas as notas de {aluno} devem estar entre 1 e 10"

def test_calcula_media_alunos():
    dicionario = {
        "Rodrigo": [5, 5, 5],
        "Renan": [10, 10, 10],
    }
    medias = calcula_media_alunos(dicionario)
    assert medias["Rodrigo"] == 5, "A média de Rodrigo deve ser 5.0"
    assert medias["Renan"] == 10, "A média de Renan deve ser 10.0"

def test_identifica_alunos_aprovados():
    medias = {"Rodrigo": 5, "Renan": 10}
    aprovados = identifica_alunos_aprovados(medias)
    assert aprovados["Rodrigo"] == "Reprovado", "Rodrigo deve ser Reprovado"
    assert aprovados["Renan"] == "Aprovado", "Renan deve ser Aprovado"

def test_gerar_relatorio():
    dicionario = {
        "Rodrigo": [5, 5, 5],
        "Renan": [10, 10, 10],
    }
    relatorio = gerar_relatorio(dicionario)
    assert "Rodrigo" in relatorio, "O relatório deve conter Rodrigo"
    assert "Renan" in relatorio, "O relatório deve conter Renan"
    assert "5" in relatorio, "O relatório deve conter a média 5.00"
    assert "10" in relatorio, "O relatório deve conter a média 10.00"
    assert "Reprovado" in relatorio, "O relatório deve conter o status Reprovado"
    assert "Aprovado" in relatorio, "O relatório deve conter o status Aprovado"