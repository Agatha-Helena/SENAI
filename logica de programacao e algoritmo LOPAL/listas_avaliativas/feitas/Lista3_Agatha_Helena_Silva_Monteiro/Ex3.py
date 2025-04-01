# -*- coding: UTF-8 -*-

print("Eu irei fazer uma tabela de multiplicação para seus estudos, caro usuário!")

def Tab():
    n = int(input("Digite um número e eu mostrarei a tabuada dele: "))
    for y in range(1, 11):
        print(f"{n} X {y} = {n*y}")

Tab()
