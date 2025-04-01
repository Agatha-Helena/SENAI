# -*- coding: UTF-8 -*-

print("Oi usuário! Irei escrever a quantidade de casas que tem o número que você digitar!")

def ca(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

n = float(input("Digite o número: "))
print(f"O número tem {ca(n)} casas.")
