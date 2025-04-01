# -*- coding: UTF-8 -*-

print("Me diga qual a temperatura atual e eu lhe direi como está o clima!")

temp = float(input("Digite a temperatura: "))

if temp <= 15:
    print("Muito frio.")
elif temp >= 16 and temp < 23:
    print("Frio.")
elif temp >=23 and temp <26:
    print("Agradável.")
elif temp >= 26 and temp <=30:
    print("Calor.")
else:
    print("Muito quente.")
