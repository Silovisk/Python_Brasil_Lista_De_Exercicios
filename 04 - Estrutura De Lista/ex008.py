idades = []
alturas = []

for i in range(1, 6):
    idade = int(input(f"Informe a {i}° idade: "))
    idades.append(idade)

    altura = float(input(f"Digite a {i}° altura: "))
    alturas.append(altura)


inverso_alturas = [alturas[i] for i in range(len(alturas) -1, -1, -1)]

print(f"""
Ordem digitado

idades: {idades}
alturas: {alturas}

Ordem inversa

idades: {idades[::-1]}
alturas: {inverso_alturas}

""")