# TODO: atividade 04
# Utilizando o conceito de módulo, crie um módulo com funções que façam as seguintes ações:
# - limpa o terminal.
# - Calcula a potência de um número informado pelo usuário elevado
# a outro número informado pelo usuário.
# - Calcula a raíz quadrada de um número informado pelo usuário.
# - Calcula o volume de um recipiente paralelepípidico.
# - Calcula o volume de um recipeinte cilindrico.
# - Em seguida, faça um programa que o usuário escolha executar uma dessas funções ou sair do programa.

import modulo

while True:
    print("\n===== MENU =====")
    print("1 - Limpar terminal")
    print("2 - Calcular potência")
    print("3 - Calcular raiz quadrada")
    print("4 - Calcular volume do paralelepípedo")
    print("5 - Calcular volume do cilindro")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        modulo.limpar_terminal()

    elif opcao == "2":
        modulo.potencia()

    elif opcao == "3":
        modulo.raiz_quadrada()

    elif opcao == "4":
        modulo.volume_paralelepipedo()

    elif opcao == "5":
        modulo.volume_cilindro()

    elif opcao == "6":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")

    input("\nPressione ENTER para continuar...")
    modulo.limpar_terminal()