# -*- coding: UTF-8 -*-

print("Me diga dois números inteiros e eu os colocarei em ordem crescente.")

valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

if valor1 > valor2:
    A = valor2
    B = valor1
    print(f"A ordem dos números é {A} e {B}.")
elif valor2 > valor1:
    A = valor1
    B = valor2
    print(f"A ordem dos números é {A} e {B}.")
else:
    print("Digite números diferentes, não podem ser iguais.")
