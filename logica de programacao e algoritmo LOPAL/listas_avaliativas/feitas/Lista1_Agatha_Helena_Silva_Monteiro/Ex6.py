# -*- coding: UTF-8 -*-

print("Me informe dois números inteiros e lhe direi se o primeiro é divisível pelo segundo.")

A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))

if B == 0:
    print("Não é possível dividir por ", B)
elif A % B == 0:
    print("O número é divisível por ", B)
else:print("O número não é divisível por ", B)
