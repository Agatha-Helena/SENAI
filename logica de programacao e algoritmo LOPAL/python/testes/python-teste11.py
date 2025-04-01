# -*- UTF-8 -*-

cont = 0
acum = 0

while True:
    valor = float(input("Digite valores e no final lhe darei a média. Digite valor negativo para sair: "))
    if valor < 0:
    	print("Você escolheu sair,tchau!")
    	break
    acum = acum + valor
    cont = cont + 1

print("A média dos valores digitados é de : ", acum / cont)
