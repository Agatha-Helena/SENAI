# -*- coding: UTF-8 -*-

print("Oioi! Digite alguns números e eu lhe direi qual deles é o maior e o menor! Se quiser parar o programa, digite um número negativo. E esteja avisado: Não digite número de mesmo valor! >:(")

M = 0
m = 0

while True:
    n = int(input("Digite um número ou então digite um negativo para finalizar: "))

    if n < 0:
        print("Você decidiu finalizar o programa.")
        print(f"O maior número é {M} e o menor é {m}!")
        break
    elif M == 0 or n > M:
        M = n

    elif m == 0 or n < m:
        m = n
