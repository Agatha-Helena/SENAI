# -*- coding: UTF-8 -*-

print("Olá usuário! Me diga a idade de várias pessoas e eu irei lhe mostrar o total de pessoas com menos de 21 anos e o total com as que tem mais de 50. Caso queira que o programa termine, digite -99.")

x = 0
y = 0
z = 0

while True:
    v = int(input("Digite uma idade ou -99 para parar o programa: "))
    if v == -99:
        break
    elif v <= 0:
        print("Digite uma idade válida.")
    elif v > 0 and v < 21:
        x = x + 1
    elif v >= 21 and v <= 50:
        y = y + 0
    elif v > 50:
        z = z + 1
    else:
        print("Erro")

print(f"A quantidade total é de {x} pessoas com menos de 21 anos e {z} pessoas com mais de 50")
