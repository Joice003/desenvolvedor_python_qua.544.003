# declaração de variáveis
nome = input("informe seu nome: ")
telefone = input("Informe seu telefone: ")

# saída de dados
print("olá ", nome, ", e meu telefone é", telefone, ".")
print("olá " + nome + ", e meu telefone é " + telefone + ".")
print("olá {}, e meu telefone é {}.".format(nome, telefone))
print(f"Olá {nome}, e meu telefone é {telefone}.")