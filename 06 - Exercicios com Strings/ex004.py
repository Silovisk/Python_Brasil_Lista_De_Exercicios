nome = input("Informe seu nome: ").upper()

for i in range(len(nome)):
    linha = ""
    for j in range(i+1):
        linha += nome[j]
    print(linha)
