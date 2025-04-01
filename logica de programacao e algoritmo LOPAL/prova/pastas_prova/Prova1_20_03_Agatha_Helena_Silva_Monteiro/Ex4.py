# -*- coding: UTF-8 -*-

print("Olá, usuário. Informarei, de acordo com sua resposta, se o número que você digitar é primo ou não.")

def Primo(n):
    if n <= 1:
        return "Não é primo."
    for v in range(2, n):
        if n % v == 0:
            return "Não é primo."
    return "Primo."

n = int(input("Digite um número inteiro: "))

print(Primo(n))
