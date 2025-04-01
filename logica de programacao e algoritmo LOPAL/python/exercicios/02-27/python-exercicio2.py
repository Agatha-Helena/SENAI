# -*- UTF-8 -*-

cont = 0

print("Me diga números positivos e falarei quantos números foram digitados até que você digite um negativo.")
while True:
    valor = int(input("Digite um valor: "))
    if valor < 0:
        print("Você escolheu sair, mas antes lhe mostrarei os resultados.")
        break
    cont = cont + 1

print(f"A quantidade de números digitados foi de {cont} números.")
    
