# -*- coding: UTF-8 -*-

print("Oioi! Diga-me alguns números que eu lhe mostrarei a soma dos pares e a soma dos ímpares! Mas esteja avisado que o programa vai parar caso mande um número maior que 1000.")

sp = 0
si = 0

while True:
    n = int(input("Digite um número ou então digite um número maior que 1000 para sair: "))
    if n > 1000:
        break
    elif n % 2 == 0:
        sp += n
    elif n % 2 != 0:
        si += n

print(f"A soma dos números ímpares é {si} e a dos pares é {sp}.")
