usuario = {
    'nome': "Fulano de Tal",
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789-12"
}

# usuário informa a chave que ele deseja alterar (obs.: lower é para tornar as letras minusculas ainda q o usuário escreva em maiuscula pq a variavel está em minusculo)
chave = input("Informe o nome da chave: ").strip().lower()

# TODO: verifica se a chave existe