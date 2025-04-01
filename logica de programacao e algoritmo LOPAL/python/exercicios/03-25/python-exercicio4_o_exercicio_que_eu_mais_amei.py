# -*- coding: UTF-8 -*-

L = []
ttl = 0
lc = 0
lv = 0

print("Oioi! Vou dizer quantas consoantes você utilizou ao digitar uma frase.")
le = input("Digite uma palavra com 10 letras minúsculas (ou digite uma frase, se quiser): ")
for i in range (len(le)):
    if le[i] == "a" or le[i] == "e" or le[i] == "i" or le[i] == "o" or le[i] == "u":
        lv += 1
    elif le[i] == " ":
        lv + 0
        lc + 0
    elif le[i] == "." or le[i] == "," or le[i] == ":" or le[i] == ";" or le[i] == "!" or le[i] == "?":
        lv + 0
        lc + 0
    elif le[i] == "á" or le[i] == "â" or le[i] == "à":
        lv += 1
    elif le[i] == "é" or le[i] == "ê" or le[i] == "è":
        lv += 1
    elif le[i] == "í" or le[i] == "î" or le[i] == "ì":
        lv += 1
    elif le[i] == "ó" or le[i] == "ô" or le[i] == "ò":
        lv += 1
    elif le[i] == "ú" or le[i] == "û" or le[i] == "ù":
        lv += 1
    else:
        lc += 1

ttl = lv + lc
print(f"No total há {ttl} letras, sendo {lc} consoantes e {lv} vogais.")
