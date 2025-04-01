# -*- coding: UTF-8 -*-

tabela = {"Alface": 0.45,
          
          "Batata": 1.20,
          
          "Tomate": 2.30,
          
          "Feijão": 1.50}

print(tabela["Tomate"])
print(tabela)

tabela["Tomate"] = 2.50
print(tabela["Tomate"])

tabela["Cebola"] = 1.20
print(tabela)
print("----------------------------------------------")
# -----------------------------------------------------

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}
print("Manga" in tabela)
print("Batata" in tabela)
print("----------------------------------------------")
# -----------------------------------------------------
tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}
print(tabela.keys())
print(tabela.values())
print("----------------------------------------------")
# -----------------------------------------------------

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}
while True:
    produto = input("Digite o nome do produto, fim para terminar: ")
    if produto == "fim" or produto == "Fim":
        break
    if produto in tabela:
        print("Preço: %5.2f" % tabela[produto])
    else:
        print("Produto não encontrado ou digitado incorretamente!")
print("----------------------------------------------")
# -----------------------------------------------------

tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}
print(tabela)
del tabela["Tomate"]
print(tabela)
print("----------------------------------------------")
# -----------------------------------------------------


