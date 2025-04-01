# -*- coding: UTF-8 -*-

print("Oioi usuário!!! Nesse programa, você pode digitar um número inteiro e eu irei fatorar ele, mostrando o resultado!")

n = int(input("Digite um número inteiro: "))

f = 1
for i in range(1, n + 1):
    f *= i

print(f"O fatorial de {n} é {f}")
