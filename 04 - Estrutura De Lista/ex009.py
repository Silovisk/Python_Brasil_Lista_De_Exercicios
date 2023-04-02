numeros = []
quadrado_numeros = []

for i in range(1, 6):
    numero = int(input(f"Digite o {i}° numero: "))
    numeros.append(numero)

    numero *= 2
    quadrado_numeros.append(numero)

print(f"""
Numeros: {numeros}
Quadrado dos numeros: {quadrado_numeros}

Soma dos quadrados: {sum(quadrado_numeros)}

""")