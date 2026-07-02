# declaração de variáveis
nome = input("Informe o nome do aluno: ").title()
nota = float(input("Informe a nota o aluno: ").replace(",", "."))

# verifica se a nota é válida
if nota >= 0 and nota <= 10:
    if nota >=7:
        print(f"{nome} está aprovadoo.")
    elif nota := 5:
        print(f"{nome} está de recuperação.")
    else:
        print(f"{nome} está reprovado.")
else:
    print(f"Nota de {nome} inválida.")