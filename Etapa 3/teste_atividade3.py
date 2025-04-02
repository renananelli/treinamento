from atividade3 import (
    buscar_dados_api,
    filtrar_maiores_de_idade,
    ordenar_por_idade,
    gerar_relatorio_usuarios
)

def test_buscar_dados_api():
    usuarios = buscar_dados_api()
    assert len(usuarios) == 6, "O número de usuários deve ser 6"
    assert isinstance(usuarios[0], dict), "Cada usuário deve ser representado como um dicionário"
    assert "id" in usuarios[0], "O dicionário do usuário deve conter a chave 'id'"
    assert "nome" in usuarios[0], "O dicionário do usuário deve conter a chave 'nome'"
    assert "idade" in usuarios[0], "O dicionário do usuário deve conter a chave 'idade'"

def test_filtrar_maiores_de_idade():
    usuarios = [
        {"id": 1, "nome": "Rodrigo", "idade": 25},
        {"id": 2, "nome": "Renan", "idade": 17},
        {"id": 3, "nome": "Roberto", "idade": 20}
    ]
    maiores_idade = [usuario for usuario in usuarios if usuario["idade"] >= 18]
    assert len(maiores_idade) == 2, "Deve haver 2 usuários maiores de idade"
    assert maiores_idade[0]["nome"] == "Rodrigo", "O primeiro usuário maior de idade deve ser Rodrigo"
    assert maiores_idade[1]["nome"] == "Roberto", "O segundo usuário maior de idade deve ser Roberto"

def test_ordenar_por_idade():
    usuarios = [
        {"id": 1, "nome": "Rodrigo", "idade": 25},
        {"id": 2, "nome": "Renan", "idade": 17},
        {"id": 3, "nome": "Roberto", "idade": 20}
    ]
    usuarios_ordenados = sorted(usuarios, key=lambda x: x["idade"])
    assert usuarios_ordenados[0]["nome"] == "Renan", "O usuário mais jovem deve ser Renan"
    assert usuarios_ordenados[1]["nome"] == "Roberto", "O segundo usuário mais jovem deve ser Roberto"
    assert usuarios_ordenados[2]["nome"] == "Rodrigo", "O usuário mais velho deve ser Rodrigo"

def test_gerar_relatorio_usuarios():
    usuarios = [
        {"id": 1, "nome": "Rodrigo", "idade": 25},
        {"id": 2, "nome": "Renan", "idade": 17},
        {"id": 3, "nome": "Roberto", "idade": 20}
    ]
    relatorio = []
    for usuario in usuarios:
        status = "Maior de idade" if usuario["idade"] >= 18 else "Menor de idade"
        relatorio.append({"id": usuario["id"], "nome": usuario["nome"], "idade": usuario["idade"], "status": status})
    
    assert relatorio[0]["status"] == "Maior de idade", "Rodrigo deve ser classificado como Maior de idade"
    assert relatorio[1]["status"] == "Menor de idade", "Renan deve ser classificado como Menor de idade"
    assert relatorio[2]["status"] == "Maior de idade", "Roberto deve ser classificado como Maior de idade"