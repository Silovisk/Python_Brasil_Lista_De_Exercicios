def imprimir_triagulo_numerico(n):
    for i in range(1, n+1):
        linha = ""
        for j in range(i):
            linha += str(i) + "\t"
        print(linha)

n = int(input("Digite o valor de n: "))
imprimir_triagulo_numerico(n)
