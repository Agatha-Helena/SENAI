# -*- coding: UTF-8 -*-

print("Me informe o preço de um produto e seu percentual de desconto. Eu lhe direi o valor do desconto e o total a ser pago.")
preço= float(input("Me informe o preço do produto: "))
desconto= int(input("Me informe o percentual de desconto: "))

valord= preço * desconto /100
total= preço - valord

print("O valor do desconto é de ", valord, ", já o preço total a pagar é de ",total)
