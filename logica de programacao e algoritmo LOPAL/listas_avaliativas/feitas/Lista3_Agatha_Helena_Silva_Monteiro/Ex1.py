# -*- coding: UTF-8 -*-

print("Oi usuário! Me diga uma altura e o raio de um cilindro que eu irei calcular o volume dele!")

def Vcili():
    raio = float(input("Digite um número real para ser o raio do cilindro: "))
    h = float(input("Digite um número real para ser a altura do cilindro: "))
    return 3.14 * (raio ** 2) * h

print(f"O volume do cilindro é de {Vcili():.2f}.")
