import os
import math

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# != significa diferente, no caso a é diferente de 0
def equacao_segundo_grau(a, b, c):
    if a != 0:
        # b**2 significa b ao quadrado
        delta = (b**2)-4*a*c
        if delta > 0:
            x1 = (-b+math.sqrt(delta))/(2*a)
            x2 = (-b-math.sqrt(delta))/(2*a)
            # gera mais de um valor, não pode ser usado com return
            yield x1
            yield x2
        elif delta == 0:
            x = -b/(2*a)
            yield x
        else:
            yield "Não existem raízes reais."
    else:
        yield "A equação não é do 2º grau."