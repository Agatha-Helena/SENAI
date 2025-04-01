# -*- coding: UTF-8 -*-

print("Olá usuário. Irei calcular a área de um quadrado, mas você tem que me informar o lado.")

def Aquad():
    lado = int(input("Digite o valor do lado: "))
    return lado ** 2

print("A área é ", Aquad())
