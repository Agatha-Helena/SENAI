# -*- coding: UTF-8 -*-

print("""Oioi, usuário! Digite o valor de uma compra e eu irei aplicar um desconto de acordo com a tabela abaixo!
   _________________________________________
  |          Valor            |   Desconto  |
  |---------------------------|-------------|
  |  entre R$50,00 e R$100,00 |     5%      |
  |---------------------------|-------------|
  |  mais que R$100,00        |     10%     |
  | ----------------------------------------|

  """)

v = float(input("""Digite o valor da sua compra aqui:
R$"""))

if v <= 50.00:
    print(f"O valor da sua compra é de R${v:.2f}.")
elif v > 50.00 and v <= 100.00:
    v1 = v * 5 /100
    v1t = v - v1
    print(f"O valor da compra é de R${v1t:.2f}.")
elif v > 100.00:
    v2 = v * 10 /100
    v2t = v - v2
    print(f"O valor da compra feita é de R${v2t:.2f}.")
