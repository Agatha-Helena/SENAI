# -*- coding: UTF-8 -*-

print("Oioi usuário! Me informe a altura e a base de um triângulo e eu irei calcular a área!")

area = 0

def Atri():
    global area

h = int(input("Digite a altura do quadrado: "))
b = int(input("Digite a base do quadrado: "))
area = (b * h)/2
print(f"A área do triângulo é de {area}.")
