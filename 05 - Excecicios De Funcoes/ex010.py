import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def jogar_craps():
    primeira_jogada = lancar_dados()
    print("Você lançou os dados e obteve um valor de", primeira_jogada)

    if primeira_jogada == 7 or primeira_jogada == 11:
        print("Você ganhou! Natural!")
    elif primeira_jogada == 2 or primeira_jogada == 3 or primeira_jogada == 12:
        print("Você perdeu! Craps!")
    else:
        print("Você obteve um ponto!")
        ponto = primeira_jogada
        while True:
            print("Lançando os dados novamente...")
            nova_jogada = lancar_dados()
            print("Você obteve um valor de", nova_jogada)
            if nova_jogada == 7:
                print("Você perdeu!")
                break
            elif nova_jogada == ponto:
                print("Você ganhou!")
                break

jogar_craps()
