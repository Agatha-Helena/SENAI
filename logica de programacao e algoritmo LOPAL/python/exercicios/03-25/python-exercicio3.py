# -*- coding: UTF-8 -*-

L = []
x = 1

print("Oiiii! Vou ver sua média a partir das 4 notas que você digitar!")

for i in range (1, 5):
    n = float(input(f"Digite o {x}º número: "))
    L.append(n)
    x += 1

media = sum(L) / 4

print(f"A sua média é {media:.2f}!")
