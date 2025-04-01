# -*- coding: UTF-8 -*-

print("Olá usuário! Está com dificuldades em converter as temperaturas de Celsius para Fahrenheit ou o oposto? Eu te ajudo, meu caro!")

def conv():

    con = input("Digite aqui para que temperatura você quer converter (F para Fahrenheit ou C para Celsius): ")
    if con == "F" or con == "f":
        ce = int(input("Digite a temperatura em Celsius: "))
        Far = 9 / 5 * ce + 32
        print(f"A temperatura é de {Far:.2f}º Fahrenheit.")
    elif con == "C" or con == "c":
        fa = int(input("Digite a temperatura em Fahrenheit: "))
        Cel = (fa - 32) * (5 / 9)
        print(f"A temperatura é de {Cel:.2f}º Celsius.")
       
conv()
