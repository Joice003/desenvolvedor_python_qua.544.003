nomes = [
    "Ana",
    "Caio",
    "Maria",
    "Pedro",
    "Jane",
    "Silas",
    "Enzo",
    "Maia",
    "Hugo",
    "Heitor",
    "Jose",
    "João",
    "Mel"
]

nome = input("Informe o nome a ser deletado: ").strip().title()

if nome in nomes:
    indice = nomes.index(nome)

    # apaga item da lista
    del(nomes[indice])

    #exibe a nova lista sem o item deletado
    for nome in nomes:
        print(nome)

else:
    print("Nome não encontrado.")