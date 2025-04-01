# -*- coding: UTF-8 -*-

print("Olá, usuário. Esse programa irá fazer cálculos a partir de algumas perguntas e lhe mostrar o valor final de um produto com juros compostos.")

def vfjc():
    VF = VI * (1 + i) * n
    return VF

VI = float(input("Digite o valor inicial do produto: "))
i = float(input("Digite (em forma decimal) a taxa de juros por período: "))
n = int(input("Digite o número de períodos: "))

print(f"O valor final do produto com juros compostos é de R${vfjc():.2f}.")
