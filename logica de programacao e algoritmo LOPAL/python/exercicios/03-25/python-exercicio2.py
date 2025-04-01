# -*- coding: UTF-8 -*-

L = []
x = 1

print("Oi usuário! Nesse programa você vai digitar 10 número reais e eu lhes mostrarei na ordem decrescente!")

for i in range (1, 11):
    n = float(input(f"Digite o {x}º número: "))
    L.append(n)
    x += 1
print(L[::-1])
