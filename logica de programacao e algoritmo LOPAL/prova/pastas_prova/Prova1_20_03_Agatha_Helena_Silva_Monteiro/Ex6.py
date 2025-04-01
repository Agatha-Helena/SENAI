# -*- coding: UTF-8 -*-

print("Oi, usuário! Nesse programa você irá escrever um número e mostrarei somente os ímpares de 1 até o número que você escolheu!")

n = int(input("Digite um número, mas tenha em mente que deve ser um número inteiro: "))

if n % 2 == 0:
    n2 = 0 + 1
    for i in range(n2, n, 2):
        print (i)
elif n % 2 != 0:
    n3 = n + 1
    for i in range(1, n3, 2):
        print (i)
else:
    print("Erro")
