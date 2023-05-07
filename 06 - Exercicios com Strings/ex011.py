import random

def desenha_boneco(vidas):
    if vidas == 6:
        print(" _____   ")
        print("|     |  ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|________")
    elif vidas == 5:
        print(" _____   ")
        print("|     |  ")
        print("|     O  ")
        print("|        ")
        print("|        ")
        print("|________")
    elif vidas == 4:
        print(" _____   ")
        print("|     |  ")
        print("|     O  ")
        print("|     |  ")
        print("|        ")
        print("|________")
    elif vidas == 3:
        print(" _____   ")
        print("|     |  ")
        print("|     O  ")
        print("|    /|  ")
        print("|        ")
        print("|________")
    elif vidas == 2:
        print(" _____   ")
        print("|     |  ")
        print("|     O  ")
        print("|    /|\ ")
        print("|        ")
        print("|________")
    elif vidas == 1:
        print(" _____   ")
        print("|     |  ")
        print("|     O  ")
        print("|    /|\ ")
        print("|    /   ")
        print("|________")
    else:
        print(" _____   ")
        print("|     |  ")
        print("|     O  ")
        print("|    /|\ ")
        print("|    / \ ")
        print("|________")


palavras = ["cachorro", "gato", "passarinho", "elefante", "macaco", "girafa", "tigre", "crocodilo", "panda"]
palavra_sorteada = random.choice(palavras)
letras = list(palavra_sorteada)
vidas = 6
acertos = ["_ " for letra in palavra_sorteada]  # lista com "_ " para cada letra
desenha_boneco(vidas)

while True:
    print()
    print("".join(acertos))  # converte lista em string

    letra = input("Informe uma letra: ")

    if letra in letras:
        print(f"A letra '{letra}' está correta!")
        # atualiza a lista de acertos com a letra adivinhada
        for i in range(len(letras)):
            if letras[i] == letra:
                acertos[i] = letra + " "
    else:
        print(f"A letra '{letra}' não existe!")
        vidas -= 1
        print(f"Voce tem {vidas} vidas")
        
    if vidas == 0:
        print("Você perdeu! A palavra era:", palavra_sorteada)
        desenha_boneco(vidas)
        break
        
    if "_ " not in acertos:
        print("Parabéns, você venceu!")
        break
    desenha_boneco(vidas)
    
        
