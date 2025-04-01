# -*- coding: UTF-8 -*-

print("Me informe o valor do salário e da prestação que te informarei se o empréstimo pode ou não ser concedido.")

sal = float(input("Digite o salário: "))
pre = float(input("Digite o valor da prestação: "))

if pre > sal * 0.3:
    print("O empréstimo não será concedido.")
else:
    print("O empréstimo será concedido.")
