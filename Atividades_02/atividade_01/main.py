import json
import os

os.system("cls" if os.name == "nt" else "clear")

ARQUIVO = "alunos.json"

# Verifica se o arquivo JSON já existe
if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        alunos = json.load(arquivo)
else:
    alunos = []

while True:
    print("\n--- CADASTRO DE ALUNO ---")

    nome = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a primeira nota: ").replace(",","."))
    nota2 = float(input("Digite a segunda nota: ").replace(",","."))
    nota3 = float(input("Digite a terceira nota: ").replace(",","."))

    # Calcula a média
    media = (nota1 + nota2 + nota3) / 3

    # Verifica a situação do aluno
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    # Cria o cadastro do aluno
    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": round(media, 2),
        "situacao": situacao
    }

    # Adiciona o aluno à lista
    alunos.append(aluno)

    # Salva os dados no arquivo JSON
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)

    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Status: {situacao}")

    # Pergunta se deseja cadastrar outro aluno
    continuar = input("\nDeseja cadastrar outro aluno? (s/n): ").lower()

    if continuar != "s":
        break

print("\nDados salvos com sucesso no arquivo alunos.json!")
print("Programa encerrado.")





# TODO: atividade 03
# Crie um programa que receba o nome de um aluno e 3 notas.
# O programa deve calcular a média do aluno e informar se o aluno está aprovado (média mínima = 7) ou reprovado.
# O programa deve gravar esses dados em um JSON.
# Ao final, o usuário deverá escolher se deseja inserir as notas de outro aluno, que deverão ser gravadas no mesmo arquivo JSON.