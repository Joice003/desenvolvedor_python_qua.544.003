# TODO: atividade 01
"""
Crie um programa que receba o nome, peso e altura do usuário e informe na tela o seu IMC o seu dignóstico com base no valor do IMC.
"""

from bisect import bisect
import os

os.system("cls" if os.name == "nt" else "clear")

try:
    nome = input("Informe o nome: ").strip()
    altura = float(input("Informe a altura em metros: ").replace(",", "."))
    peso = float(input("Informe o seu peso: ").replace(",", "."))

    os.system("cls" if os.name == "nt" else "clear")

    while True:
        print("1 - Calcurar IMC")
        print("2 - Encerrar programa")

        opcao = int(input("Informe a opção desejada: ").strip())

        match opcao:
            case 1:
                imc = peso/(altura**2)

                limites = [18.5, 25.0, 30.0, 35.0, 40.0]

                categorias = [
                    "Abaixo do peso",
                    "Peso normal",
                    "Sobrepeso",
                    "Obesidade Grau I",
                    "Obesidade Grau II",
                    "Obesidade Grau II"
                ]

                indice = bisect(limites, imc)
                print(f"IMC: {imc: .2f}")
                print(categorias[indice])
            case 2:
                print("Programa encerrado!")
                break
            case _:
                print("Opção inválida!")
                continue

except Exception as error:
    print(f"Erro: {error}")