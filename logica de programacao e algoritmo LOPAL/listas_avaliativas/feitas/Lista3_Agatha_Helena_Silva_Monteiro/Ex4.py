print("Farei uma contagem regressiva para você, usuário!")

def Cont():
    n = int(input("Digite o primeiro número para eu fazer a contagem regressiva: "))
    if n <= 0:
        print("Erro.")
    else:
        for n in range(n, -1 , -1):
            print(n)
        print("Terminou, eba!")

Cont()
