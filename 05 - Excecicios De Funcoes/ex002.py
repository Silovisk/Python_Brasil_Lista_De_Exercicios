def imprimir_triagulo_numerico(n):
    for i in range(1, n+1):
        linha = ""
        for j in range(1, i+1):
            linha += str(j) + "\t"
        print(linha)

n = int(input("Digite o valor de n: "))
imprimir_triagulo_numerico(n)
