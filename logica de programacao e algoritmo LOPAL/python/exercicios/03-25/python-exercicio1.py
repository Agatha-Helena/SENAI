# -*- coding: UTF-8 -*-

print("Oioi usuário!!!!!!!!!!!!!!!!!!!!!! Vou te mostrar 5 números inteiros de uma lista! :P")
L = [1, 2, 3, 4, 5]
print (L[0:5])
print (f"Nessa lista tem {len(L)} números!")


print("Maaas se você quiser, você pode digitar o seus números também!")
x = 1
L = []
for i in range (1, 6):
    n = int(input(f"Digite o {x}º número: "))
    L.append(n)
    x += 1

print (f"""Aqui está a sua lista:
{L}""")
