# -*- coding: UTF-8 -*-

print("Olá usuário! Irei fazer um truque que acabei de aprender. Farei a soma dos primeiros 50 números pares!")
print("""Veja só:
""")

print("Os números são")
for v in range(0, 51, 2):
    print(v)

for v in range(0, 51, 2):
    sn = 2+100
    sn2 = sn * 50
    sn3 = sn2 / 2

print(f"""E o resultado da soma deles é de {sn3}.
Fato curioso: esse cálculo pode ser feito usando a fórmula da P.A. (que significa progressão aritmética 🤓)""")
