# -*- coding: UTF-8 -*-

print("Me diga dois números inteiros e o direi qual deles é o maior!")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))


if n1 == n2:
    print("Não há maior, digite outro valor")
elif n1>2:
    print("O maior número é ", n1)
else:
    print("O maior número é ", n2)
