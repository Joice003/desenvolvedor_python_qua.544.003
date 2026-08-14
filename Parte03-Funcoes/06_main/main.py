# fazendo esse import não precisa escrever modulo para chamar a função, basta iniciar com m
import modulo as m


def main():
    m.limpar()

    nome = input("Informe o nome: ").strip().title()
    idade = int(input("Informe a idade: "))

    print(f"{nome} é {m.maioridade(idade)}")

# para proteger os dados
if __name__ == "__main__":
    main()