# -*- coding: UTF-8 -*-

L = [1, 2, 3, 4, 5]
print (L[0:5]) # [1, 2, 3, 4, 5]   da posição 0 até a posição 5, sem incluí-la
print (L[:5])  # [1, 2, 3, 4, 5]   do início até a posição 5, sem incluí-la
print (L[:-1]) # [1, 2, 3, 4]      do início até o último, sem incluí-lo
print (L[1:3]) # [2, 3]            da posição 1 até a posição 3, sem incluí-la
print (L[1:4]) # [2, 3, 4]         da posição 1 até a posição 4, sem incluí-la
print (L[3:])  # [4, 5]            da posição 3 até o final
print (L[:3])  # [1, 2, 3]         do início até a posição 3, sem incluí-la
print (L[-1])  # 5                 último elemento
print (L[-2])  # 4                 penúltimo elemento
print ("---------------------------------------------------")
# -------------------------------------------------------------

#     0  1  2
L = [12, 9, 5]
print (len(L))
V = []
print (len(V))

# len vai mostrar a quantidade de números que tem na lista
# L tem três números
# V tem 0
print ("---------------------------------------------------")

# -------------------------------------------------------------

L = ['Nome 1', 'nome 2', 'Nome 3']
print (L)
print (len(L))
print ("---------------------------------------------------")

# -------------------------------------------------------------

L = ["nós", "vai", "descer"]

x = 0

while x < len(L):
    print(L[x])
    x += 1
print ("---------------------------------------------------")

# -------------------------------------------------------------

L = []
while True:
    n = int(input("Digite um número (0 sai): "))
    if n == 0:
        break
    L.append(n) 
x = 0
while x < len(L):
    print (L[x])
    x = x + 1 
print ("---------------------------------------------------")

# --------------------------------------------------------------

L = []
while True:
    n = input("Digite algo ou digite Sair: ")
    if n == "sair" or n == "Sair":
        break
    L.append(n) 
x = 0
while x < len(L):
    print (L[x])
    x = x + 1 
print ("---------------------------------------------------")

# --------------------------------------------------------------

L = ["a"]
L.append("b")
print (L)
L.extend(["c"])
print (L)
L.append(["d", "e"]) # fica feio, fica "[a, b, c, [d, e]"
print (L)
L.extend(["f", "g", "h"]) # fica bonito "[a, b, c, [d, e], f, g, h]"
print (L)
print ("---------------------------------------------------")

# --------------------------------------------------------------

L = ["a", "b", "c"]
del L[1]  # del deleta ._.
print (L)
del L[0]
print (L)
print ("---------------------------------------------------")

# --------------------------------------------------------------

L = ["a"]
L.append("b")
print (L)
L.extend(["c"])
print (L)
L.append(["d", "e"]) # fica feio, fica "[a, b, c, [d, e]"
print (L)
L.extend(["f", "g", "h"]) # fica bonito "[a, b, c, [d, e], f, g, h]"
print (L)
del L[3:4]  # del deleta o erro ._.
print (L)
print ("---------------------------------------------------")

# --------------------------------------------------------------

L = list(range(101))
print (L)
del L[1:99]
print (L)
print ("---------------------------------------------------")
# --------------------------------------------------------------

L = [8, 9, 15]
for e in L:
    print (e)
print ("---------------------------------------------------")

L = ["oh", "denise", "sai", "da", "live", "filha"]
for e in L:
    print (e)
print ("---------------------------------------------------")
# --------------------------------------------------------------

numeros = [2, 5, 3.14, 1, -7]
numeros.sort() # organizou em ordem crescente
print (numeros)
animais = ["macacos", "gatos", "cachorros", "ursos", "elefantes"]
animais.sort() # organizou em ordem alfabética
print (animais)

print ("---------------------------------------------------")

