# -*- coding: UTF-8 -*-

print("Irei calcular quanto tempo de vida você perdeu de acordo com a quantidade de cigarros que você já fumou.")
qtc = int(input("Me informe a quantidade de cigarros que você fuma por dia: "))
qta = float(input("Me informe há quantos anos você fuma: "))

mipc = 10
mipd = qtc * mipc
temptomi = mipd * 365 * qta
temptodi = temptomi / (60 * 24)
qtct = qtc * qta * 365

print("Você perdeu aproximadamente %i dias de sua vida tendo fumado %i cigarros." %(temptodi, qtct))
