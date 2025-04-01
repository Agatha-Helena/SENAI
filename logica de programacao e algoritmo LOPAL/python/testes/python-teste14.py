# -*- coding: UTF-8 -*-

#Usando def

"""def soma(a, b):

print(a + b)

soma(2, 9)

soma(7, 8)

soma(10, 15)"""

"""def soma(a, b):
    print(f" {a} + {b} = {a+b} ")

soma(2, 9)

soma(7, 8)

soma(10, 15)"""


# Usando return

"""def soma(a, b):
    return(a + b)

print(soma(2, 9))

print(soma(7, 8))

print(soma(10, 15))"""


"""def soma(a, b):
    return(a + b)

resultado = 2 + soma(2, 9)

print(soma(2, 9))

print(soma(7, 8))

print(soma(10, 15))

print(resultado)"""

#def e return

"""def epar(x):
    return(x % 2 == 0)

print(epar(2))

print(epar(3))

print(epar(10))"""

#def, return, if e else

"""def epar(x):
    return(x % 2 == 0)

def par_ou_impar(x):
    if epar(x):
        return "par"
    else:
        return "ímpar"

print(par_ou_impar(4))

print(par_ou_impar(5))"""

#def e global

"""resultado = 0
def soma():
    global resultado
    num1 = int(input("Valor1: "))
    num2 = int(input("Valor2: "))
    resultado = num1 + num2
    print("o resultado é: ", resultado)

print("O resultado é ", resultado)
soma()"""

#def, global e return

"""def soma():
    global resultado
    num1 = int(input("Valor1: "))
    num2 = int(input("Valor2: "))
    resultado = num1 + num2
    return resultado"""
