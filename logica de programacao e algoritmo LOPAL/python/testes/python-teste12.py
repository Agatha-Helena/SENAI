# -*- UTF-8 -*-

tabuada = 1
while tabuada <= 10:
    n = 0
    print("""---------------
Tabuada do %d
  """ % tabuada)
    while n <=10:
        print(f"{tabuada} X {n} = {tabuada * n}")
        n = n + 1
    tabuada = tabuada + 1
print("---------------")
