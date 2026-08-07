# A chave, neste caso, é nome, idade, email e cpf

usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789-12"
}

# usuário informa a chave que ele deseja alterar (obs.: lower é para tornar as letras minusculas ainda q o usuário escreva em maiuscula pq a variavel está em minusculo)
chave = input("Informe a chave que deseja alterar: ").strip().lower()

if chave in usuario:

    # Exibe o dicionário com novo valor da chave escolhida
    usuario[chave] = input(f"Informe o novo valor para a {chave} ").strip()

    # Exibe o dicionário com novo valor da chave escolhida
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")

else:
    print("Chave não encontrada")