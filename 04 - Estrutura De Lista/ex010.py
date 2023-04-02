# Lê os três vetores
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(10):
    vetor1.append(int(input("Digite um valor para o primeiro vetor: ")))
    vetor2.append(int(input("Digite um valor para o segundo vetor: ")))
    vetor3.append(int(input("Digite um valor para o terceiro vetor: ")))

# Cria o quarto vetor e adiciona os elementos intercalados dos três primeiros vetores
vetor4 = []
for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])

# Exibe o quarto vetor
print("Vetor intercalado: ", vetor4)
