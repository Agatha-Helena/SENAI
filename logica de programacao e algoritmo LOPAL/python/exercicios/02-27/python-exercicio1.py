# -*- UTF-8 -*-

print("Digite um número para eu calcular o triplo dele! Caso queira sair do programa, digite -999")

while True:
    n = int(input("Digite um número: "))
    if n == -999:
        print("Você escolheu sair, tchau!")
        break
    elif n != -999:
        n2 = n * 3
        print(n2)
