# -*- coding: UTF-8 -*-

print("Olá! Farei alguns cálculos básicos para você, como soma (+), subtração (-), multiplicação (x) e divisão (/).")

def ad():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    return n1 + n2

def sub():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    return n1 - n2

def mul():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    return n1 * n2

def div():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    return n1 / n2

def esco():
    if r == "+":
        print(f"O resultado é {ad():.2f}.")
    elif r == "-":
        print(f"O resultado é {sub():.2f}.")
    elif r == "x" or r == "X":
        print(f"O resultado é {mul():.2f}.")
    elif r == "/":
        print(f"O resultado é {div():.2f}.")
    else:
        print("Erro.")

r = input("Escolha o cálculo de acordo com a mensagem acima: ")
esco()
