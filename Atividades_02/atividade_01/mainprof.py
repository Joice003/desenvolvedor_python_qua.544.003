import os
import json

alunos = []

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - Informa dados")
    print("2 - Sair do programa")
    opcao = input("Informe a opção: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            aluno = {}
            notas = [0,0,0]

            aluno['nome'] = input("Informe o nome do aluno: ").strip().title()
            for i in range(len(notas)):
                notas[i] = float(input(f"Informe a {i+1}ª nota: ").replace(",","."))
            aluno['notas'] = notas
            aluno['média'] = sum(notas)/len(notas)
        case "2":
            pass
        case _:
            print("Opçao inválida.")
            continue