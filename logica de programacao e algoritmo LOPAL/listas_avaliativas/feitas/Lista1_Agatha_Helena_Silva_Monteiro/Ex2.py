#-*- coding: UTF-8 -*-

print("Digite um número e, dependendo do número, informarei a raiz quadrada ou o quadrado do número.")

import math

num = int(input("Qual número você escolheu? "))

if num >= 0:
    resultado = math.sqrt(num)
    print("O resultado é ", resultado)
else:
    resultado = num ** 2
    print("O resultado é ", resultado)
