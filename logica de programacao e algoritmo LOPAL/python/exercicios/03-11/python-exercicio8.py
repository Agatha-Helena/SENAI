# -*- coding: UTF-8 -*-

print("Me informe sua idade e eu lhe informarei sua classe eleitoral.")

def eleitoral():
    idade = int(input("Digite a sua idade: "))
    if idade < 16:
        return "Não-eleitor."
    elif idade > 18 and idade < 65:
        return "Eleitor obrigatório."
    elif idade >= 16 and idade <= 18 or idade >= 65:
        return "Eleitor facultativo."

print(eleitoral())
