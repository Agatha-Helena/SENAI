# -*- coding: UTF-8 -*-

print("Oláááá, irei te mostrar os números que são divisores do número que você escrever!")

n = int(input("Digite um número: "))

for v in range(1, n):
    if n % v == 0:
        print(v)
