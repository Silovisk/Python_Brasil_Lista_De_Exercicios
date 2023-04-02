def calcular_percentual_votos(votos_jogador, total_votos):
    return (votos_jogador / total_votos) * 100

votos_jogadores = [0] * 23 # lista de 23 posições iniciada com 0
numero_jogador = int(input("Número do jogador (0=fim): "))
total_votos = 0

while numero_jogador != 0:
    if numero_jogador >= 1 and numero_jogador <= 23:
        votos_jogadores[numero_jogador-1] += 1
        total_votos += 1
    else:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
    numero_jogador = int(input("Número do jogador (0=fim): "))

print("\nResultado da votação:\n")

print("Foram computados {} votos.\n".format(total_votos))

print("Jogador   Votos          %")
for i in range(23):
    if votos_jogadores[i] > 0:
        percentual_votos = calcular_percentual_votos(votos_jogadores[i], total_votos)
        print("{:<10}{:<15}{:.1f}%".format(i+1, votos_jogadores[i], percentual_votos))

maior_votos = max(votos_jogadores)
indice_maior_votos = votos_jogadores.index(maior_votos)
percentual_maior_votos = calcular_percentual_votos(maior_votos, total_votos)

print("\nO melhor jogador foi o número {}, com {} votos, correspondendo a {:.1f}% do total de votos.".format(indice_maior_votos+1, maior_votos, percentual_maior_votos))

# Gravando os dados em um arquivo texto
with open("resultado_enquete.txt", "w") as arquivo:
    arquivo.write("Foram computados {} votos.\n\n".format(total_votos))
    arquivo.write("Jogador   Votos          %\n")
    for i in range(23):
        if votos_jogadores[i] > 0:
            percentual_votos = calcular_percentual_votos(votos_jogadores[i], total_votos)
            arquivo.write("{:<10}{:<15}{:.1f}%\n".format(i+1, votos_jogadores[i], percentual_votos))
    arquivo.write("\nO melhor jogador foi o número {}, com {} votos, correspondendo a {:.1f}% do total de votos.".format(indice_maior_votos+1, maior_votos, percentual_maior_votos))
