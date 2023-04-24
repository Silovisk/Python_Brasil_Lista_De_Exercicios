def quadrados_magicos():
    quadrados = []
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Gera todas as combinações possíveis dos números de 1 a 9
    for a in numeros:
        for b in numeros:
            for c in numeros:
                for d in numeros:
                    for e in numeros:
                        for f in numeros:
                            for g in numeros:
                                for h in numeros:
                                    for i in numeros:
                                        # Verifica se os números formam um quadrado mágico
                                        if a + b + c == 15 and d + e + f == 15 and g + h + i == 15 and \
                                           a + d + g == 15 and b + e + h == 15 and c + f + i == 15 and \
                                           a + e + i == 15 and c + e + g == 15 and \
                                           len(set([a, b, c, d, e, f, g, h, i])) == 9:
                                            # Adiciona o quadrado mágico à lista de quadrados
                                            quadrado = [[a, b, c], [d, e, f], [g, h, i]]
                                            quadrados.append(quadrado)

    # Mostra na tela os quadrados mágicos encontrados
    print("Quadrados Mágicos encontrados:")
    for i, quadrado in enumerate(quadrados):
        print(f"Quadrado Mágico {i+1}:")
        for linha in quadrado:
            print(linha)
        print()

# Chamada da função
quadrados_magicos()
