from random import randint 


def lancar_dado(valor):

    if valor in [7,11]:
        resultado = "Natural voce ganhou"
    elif valor in [2,3,12]:
        resultado = "Craps voce perdeu"
    elif valor in [4,5,6,8,9,10]:
        resultado = "Ponto Continuar jogando"
        ponto += 1     

    return resultado

valor_dado = randint(2, 12)

resultado = ""

