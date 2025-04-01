# -*- coding: UTF-8 -*-

print("Informe suas duas notas e eu direi se você foi aprovado, reprovado ou se está de recuperação.")

n1 = float(input("Me diga a primeira nota: "))
n2 = float(input("Me diga a segunda nota: "))

media = (n1 + n2) / 2

if media >11:
    print("Digite uma nota válida.")
elif media <3:
    print("Você está reprovado.")
elif media >=3 and media <7:
    print("Você está de recuperação.")
else:
    print("Você foi aprovado.")
