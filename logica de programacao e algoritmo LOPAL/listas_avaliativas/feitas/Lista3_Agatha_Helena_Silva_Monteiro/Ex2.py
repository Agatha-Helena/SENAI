# -*- coding: UTF-8 -*-

"""print("Olá, me diga um número inteiro e eu lhe direi o produto de todos os digitos.")
print("Por exemplo: 123 ---> 1 x 2 x 3 = 6")

ac = 1

def produto():
        for v in ne:
            nn = int(v)
            if nn <= 0:
                print("Digite um valor positivo!")
            else:
                global ac
                ac = nn * ac
                print(ac)

ne = input("Digite o valor: ")
produto()"""

print("Olá, me diga um número inteiro e eu lhe direi o produto de todos os digitos.")
print("Por exemplo: 123 ---> 1 x 2 x 3 = 6")

ac = 1

def produto():
    if ne <= 0:
        print("Digite um número positivo.")
    else:
        nn = str(ne)
        for v in nn:
            nn = int(v)
            global ac
            ac = nn * ac
            print(ac)

ne = int(input("Digite o valor: "))
produto()
