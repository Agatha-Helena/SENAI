# -*- coding: UTF-8 -*-

print("Me diga qual as suas três notas e o número de faltas, assim poderei lhe dizer qual sua situação final!")

N1 = float(input("Digite sua primeira nota: "))
N2 = float(input("Digite sua segunda nota: "))
N3 = float(input("Digite sua terceira nota: "))
F = int(input("Digite sua quantidade de faltas: "))

media = (N1 + N2 + N3) / 3
LF = 80 * 0.25

if media > 7 and F < LF:
    print("Você foi aprovado.")
elif media < 7 and F > LF:
    print("Você foi reprovado por falta e por média.")
elif F >= LF:
    print("Você foi reprovado por falta.")
elif media < 7:
    print("Você foi reprovado por média.")
else:
    print("Erro.")
