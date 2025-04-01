# -*- UTF-8 -*-

print("Me informe alguns números que eu lhe falarei quantos números entre 100 e 200 foram digitados.")
print("Se você digitar o número 0, eu pararei o programa.")

cont = 0

while True:
    n = int(input("Digite um número: "))

    if n >= 100 and n <=200:
        cont = cont + 1

    elif n == 0:
        print(f"No total, {cont} números entre 100 e 200 foram digitados.")
