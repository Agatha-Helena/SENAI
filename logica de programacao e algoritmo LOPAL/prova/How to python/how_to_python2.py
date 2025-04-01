# -*- coding: UTF-8 -*-

print("Olá")
r = input("""Quer saber sobre if, elif e else?
""")
if r == "não" or r == "Não":
    print("Você não vai saber o que é isso então.")
elif r == "Sim" or r == "sim":
    print("""
If é o "se" da lingua portuguesa, ou seja,
você vai estar falando, por exemplo:
"Se você fizer tal coisa, tal coisa será feita."

Elif só pode aparecer depois que um If já apareceu,
já que indica o "senão, se".
if = "Se você fizer tal coisa, tal coisa será feita."
elif = "Senão, se tal coisa for feita, outra tal coisa será feita."

Else é a última "coisa", o "senão" final.

if = "Se você fizer tal coisa, tal coisa será feita."
elif = "Senão, se tal coisa for feita, outra tal coisa será feita."
else - "Senão, a última tal coisa será feita."
""")
else:
    print("Eu fiz pergunta de sim ou não.")
