# -*- coding: UTF-8 -*-

print("Me diga três valores reais e eu irei lhe informar se eles podem formar os lados de um triângulo e de qual tipo ele será.")

A = float(input("Digite o primeiro número: "))
B = float(input("Digite o segundo número: "))
C = float(input("Digite o terceiro número: "))

if (A + B < C) or (A + C < B) or (B + C < A):
    print("Isso não é um triângulo.")
elif (A == B) and (A == C):
    print("É um triângulo equilátero.")
elif (A == B) or (A == C) or (B == C):
    print("É um triângulo Isósceles.")
else:
    print("É um triângulo Escaleno.")
