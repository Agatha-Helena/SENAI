# -*- coding: UTF-8 -*-
print("Olá! Me diga dois números inteiros e farei uma adição. Se o número for maior que 20, anunciarei com o resultado somando mais 8. Se for menor, irei subtrair 5 do resultado.")
X = int(input("Digite um número: "))
Y = int(input("Digite o segundo número: "))

resultado = X + Y

if resultado >20:
    resposta = resultado + 8
    print("O resultado é de  ", resposta)

else:
    resultado <= 20
    resposta = resultado - 5
    print("O resultado é de ", resposta)
