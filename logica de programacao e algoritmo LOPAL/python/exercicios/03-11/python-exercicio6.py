# -*- coding: UTF-8 -*-

print("Oi usuário! Digite qualquer número e eu lhe direi se é positivo ou negativo.")
def P():
    valor = float(input("Digite um valor: "))
    return valor > 0

def PouN():
    if P():
        return "P"
    else:
        return "N"

print(PouN())
