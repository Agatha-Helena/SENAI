# -*- coding: UTF-8 -*-
print("Irei calcular o tempo de viagem do seu carro, mas preciso de informações.")
distância = float(input("Me informe a distância que precisará percorrer em km: "))
vm = float(input("Me diga a velocidade média para a viagem em km/h: "))

tempo = distância / vm

print("O tempo da viagem é de ", tempo, "horas")
