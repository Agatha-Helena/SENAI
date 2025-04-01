# -*- coding: UTF-8 -*-

print("Digite o valor de um produto e do seu imposto e eu lhe darei o valor total dele.")

def somaImposto():

    custo = float(input("Digite o valor do produto antes do imposto: "))
    imposto = float(input("Digite o valor do imposto: "))

    taxaImposto = (custo * imposto) / 100

    T = custo + taxaImposto
    return T

print(f"O valor total é de {somaImposto()}.")
