#-*- coding: UTF-8 -*-
print("Olá! Irei calcular o aumento do seu salário, mas precisarei de algumas informações.")
salário_n = float(input("Me informe o valor do seu salário normal: "))
porcentagem = int(input("Agora me informe a porcentagem do aumento: "))

valor_au = salário_n * porcentagem / 100
total= salário_n + valor_au
print("O valor do aumento do salário é de ",valor_au, "e o total é de ",total)
