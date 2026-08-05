paises = [
    "Brasil",
    "México",
    "Argentina",
    "Chile",
    "Brasil",
    "México",
    "Peru",
    "França",
    "Chile",
    "Italia",
    "Coreia",
    "China",
    "Brasil",
    "China",
    "Irã",
    "Brasil",
    "China",
    "Italia",
    "Brasil"
]

pais = input("Informe o país a ser pesquisado: ").strip().title()

# armazena a quantidade de ocorrências na lista
qtde = paises.count(pais)

print(f"{pais} foi encontrado {qtde} vezes na lista.")