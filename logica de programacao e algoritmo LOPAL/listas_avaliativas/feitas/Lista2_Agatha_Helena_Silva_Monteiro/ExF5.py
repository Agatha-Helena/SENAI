# -*- coding: UTF-8 -*-

print("Irei lhe mostrar a tabuada caso precise de ajuda em algum cálculo matemático.")

tabuada = 0
for tabuada in range(10):
    n = 0
    print("""_______________
  Tabuada %d
""" % tabuada)
    for n in range(11):
        print("  %d X %d = %d" % (tabuada, n, tabuada * n))
        n = n + 1
    tabuada = tabuada + 1
    print("_______________")
