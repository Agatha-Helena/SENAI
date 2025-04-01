# -*- coding: UTF-8 -*-

print("Oioi! Me informe a quantidade de km percorrido por um carro que você alugou e por quantos dias você alugou.")
km = float(input("Me informe a quantidade de km rodado: "))
dia = int(input("Me informe a quantidade de dias que o carro foi alugado: "))

total = (km*00.15) + (dia*60.00)

print("O preço total a pagar é: ", total)
