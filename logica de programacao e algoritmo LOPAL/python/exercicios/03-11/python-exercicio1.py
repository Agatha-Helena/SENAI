# -*- coding: UTF-8 -*-

print("Usuário, digite dois números e irei lhe falar qual é o maior.")

def mn():
    if n1 > n2:
        return n1
    else:
        return n2

n1 = int(input("Digite o número: "))
n2 = int(input("Digite o número: "))

mn = mn()
print(f"O maior número entre {n1} e {n2} é {mn}")
