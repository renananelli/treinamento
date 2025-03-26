from tabulate import tabulate

def buscar_dados_api():
    usuarios = [
        {"id": 1, "nome": "Rodrigo", "idade": 25},
        {"id": 2, "nome": "Renan", "idade": 17},
        {"id": 3, "nome": "Roberto", "idade": 20},
        {"id": 4, "nome": "Ana", "idade": 15},
        {"id": 5, "nome": "Claudia", "idade": 22},
        {"id": 6, "nome": "Maria", "idade": 19}
    ]
    return usuarios

def filtrar_maiores_de_idade(usuarios):
    maiores_idade = [usuario for usuario in usuarios if usuario["idade"] >= 18]    
    print("\nmaiores de idade")
    print(tabulate(maiores_idade, headers="keys", tablefmt="grid"))

def ordenar_por_idade(usuarios):
    usuarios_ordenados = sorted(usuarios, key=lambda x: x["idade"])
    print("\nusuarios ordenados")
    print(tabulate(usuarios_ordenados, headers="keys", tablefmt="grid"))

def gerar_relatorio_usuarios(usuarios):
    relatorio = []
    for usuario in usuarios:
        status = "Maior de idade" if usuario["idade"] >= 18 else "Menor de idade"
        relatorio.append({"id": usuario["id"], "nome": usuario["nome"], "idade": usuario["idade"], "status": status})
    
    print("\nRelatorio de Usuarios:")    
    print(tabulate(relatorio, headers="keys", tablefmt="grid"))

def main():

    usuarios = buscar_dados_api()
    filtrar_maiores_de_idade(usuarios)
    ordenar_por_idade(usuarios)
    gerar_relatorio_usuarios(usuarios)


if __name__ == "__main__":
    main()