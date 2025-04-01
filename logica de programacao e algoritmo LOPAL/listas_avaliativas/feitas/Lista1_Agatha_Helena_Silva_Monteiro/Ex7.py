# -*- coding: UTF-8 -*-

print("Me informe por quantas horas você trabalha por mês e lhe direi o valor do seu salário.")

hr = float(input("Digite por quantas horas você trabalha: "))

sal = hr * 19.50

if hr <= 0:
                 print("Digite um valor válido.")

elif sal > 1500.00:
    total = sal * 0.10
    print("O seu salário é de ", total)

else:
    total = sal
    print("O seu salário é de ", total)
