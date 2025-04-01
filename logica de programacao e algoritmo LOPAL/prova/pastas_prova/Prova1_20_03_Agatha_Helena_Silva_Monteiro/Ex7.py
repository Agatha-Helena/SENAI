# -*- coding: UTF-8 -*-

print("Oi, nesse programa irei lhe pedir três lados de um triângulo e eu irei lhe dizer se ele é ou não é equilátero.")

def triangulo_equilatero():
    if n1 != n2:
        return "não formam um triângulo equilátero."
    elif n2 != n3:
        return "não formam um triângulo equilátero."
    elif n1 != n3:
        return "não formam um triângulo equilátero."
    elif n1 == n2 and n1 == n3 and n2 == n3:
        return "formam um triângulo equilátero."
    else:
        return "Erro."

n1 = float(input("Digite o valor do primeiro lado: "))
n2 = float(input("Digite o valor do segundo lado: "))
n3 = float(input("Digite o valor do terceiro lado: "))

print(f"Os números {n1:.2f}, {n2:.2f} e {n3:.2f} {triangulo_equilatero()}")
