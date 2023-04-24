nome = "SILAS"

for i in range(len(nome)):
    linha = ""
    for j in range(len(nome) - i):
        linha += nome[j]

    print(linha)