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
    
    # criando as notas para os alunos
    for aluno in dicionario_alunos.keys():
        dicionario_alunos[aluno] = [random.randint(1, 10) for _ in range(10)]
    
    for aluno, notas in dicionario_alunos.items():
        print(f"Aluno: {aluno}, Notas: {notas}")
    return dicionario_alunos

def calcula_media_alunos(dicionario_alunos):
    medias = {}
    for aluno, notas in dicionario_alunos.items():
        medias[aluno] = sum(notas) / len(notas)
    print(medias)
    return medias

def identifica_alunos_aprovados(medias):
    aprovados = {}
    for aluno, media in medias.items():
        aprovados[aluno] = "Aprovado" if media >= 7 else "Reprovado"
    print(aprovados)
    return aprovados

def gerar_relatorio(dicionario_alunos):
    medias = calcula_media_alunos(dicionario_alunos)
    aprovados = identifica_alunos_aprovados(medias)

    tabela = []
    for aluno in dicionario_alunos.keys():
        tabela.append([aluno, f"{medias[aluno]:.2f}", aprovados[aluno]])

    print("\nRelatorio de Alunos:")
    print(tabulate(tabela, headers=["Aluno", "Média", "Status"], tablefmt="grid"))

def main():

    dicionario_alunos = cria_dicionario_alunos_notas()
    gerar_relatorio(dicionario_alunos)

if __name__ == "__main__":
    main()