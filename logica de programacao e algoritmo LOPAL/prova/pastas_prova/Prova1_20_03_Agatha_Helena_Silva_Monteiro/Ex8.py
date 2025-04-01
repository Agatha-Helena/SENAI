# -*- coding: UTF-8 -*-

print("Olá! Irei contar quantos números positivos há até o número que você digitar.")

while True:
    n = int(input("O número deve ser um número inteiro: "))
    if n < 0:
        print("""Houve 1 número positivo até seu número (0).
----------------------------------------------------------------------""")
    elif n >= 0:
        n2 = n + 1
        print(f"""Houveram {n2} números positivos até o seu número (contando com 0).
-------------------------------------------------------------------------""")
