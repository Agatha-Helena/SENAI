# -*- UTF-8 -*-

print("Me diga qual o sexo das pessoas e irei contabilizar a quantidade de pessoas que são do sexo masculino e lhe informar. Caso queira acabar o programa, aperte 0.")
print("Digite M ou m para Masculino e F ou f para Feminino.")
cont = 0

while True:
    sp = input("Digite seu sexo: ")

    if sp == "m" or sp == "M":
        cont = cont + 1
    elif sp == "0":
        print(f"Você escolheu sair e {cont} é a quantidade de pessoas que são do sexo masculino.")
        break




"""while True:
    s = input("Digite seu sexo ou 0 para sair: ")
    if s == 0:
        print("Você escolheu sair, tchau.")
        break
    elif s == F:
        cont = cont + 0
    elif s == M:
        cont = cont + 1"""
    
