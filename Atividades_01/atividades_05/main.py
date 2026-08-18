# TODO: atividade 05
# usando recursividade, crie um programa onde o usuário informa um número interio e o programa calcula a sequência de Fibonacci até o número informado.
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def fibonacci(a, b, limite):
    if a > limite:
        return

    print(a, end=" ")

    fibonacci(b, a + b, limite)


numero = int(input("Digite um número inteiro: "))

print("Sequência de Fibonacci até", numero, ":")
fibonacci(0, 1, numero)