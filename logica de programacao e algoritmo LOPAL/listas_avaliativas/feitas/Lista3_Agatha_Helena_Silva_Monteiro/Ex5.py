# -*- coding: UTF-8 -*-

print("Olá, aventureiro! Este programa irá lhe ajudar na jornada de descobrir qual número é primo!")

def Primo(n):
    if n <= 1:
        return f"O número {n} não é primo!"
    for v in range(2, n):
        if n % v == 0:
            return f"O número {n} não é primo!"
    return f"O número {n} é primo!"

n = int(input("Digite um número: "))

print(Primo(n))
