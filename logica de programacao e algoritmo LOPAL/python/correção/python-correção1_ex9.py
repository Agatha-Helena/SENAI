# -*- coding: UTF-8 -*-

print("Irei calcular quanto tempo de vida você perdeu de acordo com a quantidade de cigarros que você já fumou.")
cigarros = int(input("Me informe a quantidade de cigarros que você fuma por dia: "))
anos_fumados = float(input("Me informe há quantos anos você fuma: "))

qtd_total_cigarros = cigarros * anos_fumados * 365
tempo_minutos = qtd_total_cigarros = qtd_total_cigarros * 10
total_dias = tempo_minutos / 60 / 24

print("Você perdeu %i dias e fumou %i cigarros" %(total_dias, qtd_total_cigarros))
