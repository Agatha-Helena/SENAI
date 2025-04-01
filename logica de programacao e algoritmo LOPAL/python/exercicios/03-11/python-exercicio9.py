# -*- coding: UTF-8 -*-

print("Olá, aluno! Direi seu conceito a partir da sua nota!")

def con():
    if n < 3:
        return "E"
    elif n >= 3 and n <= 5:
        return "D"
    elif n == 6 or n == 7:
        return "C"
    elif n == 8 or n == 9:
        return "B"
    elif n == 10:
        return "A"

n = int(input("Digite sua nota: "))

if n <0 or n > 10:
    print("Digite uma nota válida.")
else:
    print(f"Seu conceito é {con()}.")
