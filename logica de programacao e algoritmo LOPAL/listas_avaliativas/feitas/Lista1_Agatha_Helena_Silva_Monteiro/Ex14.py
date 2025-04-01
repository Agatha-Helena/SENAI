# -*- coding: UTF-8 -*-

print("Olá! Me diga o valor do produto e eu lhe direi o valor de venda.")

valor = float(input("Digite o valor do produto: "))

luc45 = valor * 0.45
luc30 = valor * 0.30

total = valor + luc45
total2 = valor + luc30

if valor < 20:
    print("O valor da venda é de R$%.2f" % total)
else:
    print("O valor é de R$%.2f" % total2)
