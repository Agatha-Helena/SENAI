#-*- coding: UTF-8 -*-

print("Me informe seu peso e sua altura, assim falarei se você está com um peso favorável ou não.")

peso = float(input("Me informe seu peso: "))
altura = float(input("Me informe sua altura: "))

IMC = peso / (altura ** 2)

if IMC < 0:
    print("Digite uma altura e um peso válido.")
elif IMC < 20:
    print("Você está abaixo do peso.")
elif IMC >= 20 and IMC < 25:
    print("Você está com o peso normal.")
elif IMC >= 25 and IMC < 30:
    print("Você está sobre peso.")
elif IMC >= 30 and IMC < 40:
    print("Você está obeso.")
else:
    print("Você é peso mórbido.")
