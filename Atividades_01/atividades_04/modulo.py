import os
import math

# Limpa o terminal
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Calcula a potência
def potencia():
    numero = float(input("Digite o número: "))
    expoente = float(input("Digite o expoente: "))

    resultado = numero ** expoente

    print(f"Resultado: {resultado}")


# Calcula a raiz quadrada
def raiz_quadrada():
    numero = float(input("Digite um número: "))

    if numero < 0:
        print("Não é possível calcular a raiz quadrada de um número negativo.")
    else:
        resultado = math.sqrt(numero)
        print(f"Resultado: {resultado}")


# Calcula o volume de um paralelepípedo
def volume_paralelepipedo():
    comprimento = float(input("Digite o comprimento: "))
    largura = float(input("Digite a largura: "))
    altura = float(input("Digite a altura: "))

    volume = comprimento * largura * altura

    print(f"Volume: {volume}")


# Calcula o volume de um cilindro
def volume_cilindro():
    raio = float(input("Digite o raio: "))
    altura = float(input("Digite a altura: "))

    volume = math.pi * (raio ** 2) * altura

    print(f"Volume: {volume:.2f}")