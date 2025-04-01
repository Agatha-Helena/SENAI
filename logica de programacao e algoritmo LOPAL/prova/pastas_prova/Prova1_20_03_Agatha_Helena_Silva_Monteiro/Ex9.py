# -*- coding: UTF-8 -*-

print("Olá, usuário. Irei pedir o comprimento dos três lados de um triângulo e eu irei informar se ele é escaleno.")

def tesc():
    if n1 != n2 and n1 != n3 and n2 != n3:
        return "formam um triângulo escaleno."
    else:
        return "não formam um triângulo escaleno."

n1 = float(input("Digite o valor do primeiro lado: "))
n2 = float(input("Digite o valor do segundo lado: "))
n3 = float(input("Digite o valor do terceiro lado: "))

print(f"Os números {n1:.2f}, {n2:.2f} e {n3:.2f} {tesc()}")
