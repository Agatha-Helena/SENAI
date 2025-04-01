#-*- coding: UTF-8 -*-

print("Me informe uma quantidade de dias, horas, minutos e segundos, que eu lhe direi quanto tudo isso é em segundos!")
dias = int(input("Digite a quantidade de dias: "))
hrs = int(input("Digite a quantidade de horas: "))
minu = int(input("Digite a quantidade de minutos: "))
segun = int(input("Digite a quantidade de segundos: "))

cond = dias*86400
conh = hrs*3600
conm = minu*60
soma = (cond+conh+conm)+segun
print("O total de tudo isso em segundos é de: ", soma)

