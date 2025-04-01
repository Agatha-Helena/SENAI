#-*- coding: UTF-8 -*-

pergunta = int(input("Qual a velocidade do seu carro? "))

if pergunta <=0:
     print("Erro.")

elif pergunta > 80:
 vm = (pergunta - 80) * 5
 km_acima = pergunta - 80

print("Você andou acima da velocidade e foi multado, o preço é de ",vm, "e você andou ",km_acima, "da velocidade normal.")

 else: pergunta <80
    print("Você andou dentro da velocidade recomendada, bom trabalho!")

