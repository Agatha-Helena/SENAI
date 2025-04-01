# -*- coding: UTF-8 -*-

print("Olá! Lhe informarei sua faixa etária de acordo com a sua idade.")

idade = int(input("Digite sua idade: "))

if idade <= 0:
    print("Digite uma idade válida.")
elif idade > 0 and idade < 2:
    print("Você é um bebê.")
elif idade >= 2 and idade < 12:
    print("Você é uma criança.")
elif idade >= 12 and idade < 23:
    print("Você é um adolescente.")
elif idade >= 23 and idade < 70:
    print("Você é um adulto.")
elif idade >= 70 and idade < 100:
    print("Você é idoso.")
else:
    print("Você provavelmente está morto.")
