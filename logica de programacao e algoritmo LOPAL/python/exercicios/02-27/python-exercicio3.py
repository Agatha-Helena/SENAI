# -*- UTF-8 -*-

cont = 0
acum = 0

print("Digite valores e no final lhe darei a média. Digite um valor negativo para sair.")
while True:
    valor = float(input("Digite um valor: "))
    if valor < 0:
    	print("Você escolheu sair,tchau!")
    	break
    acum = acum + valor
    cont = cont + 1

print("A média dos valores digitados é de : ", acum / cont)

