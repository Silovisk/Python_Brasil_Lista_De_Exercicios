codigo_cidades = []
n_veiculos = []
n_acidentes = []
acidentes_2000 = []


for i in range(5):

    codigo_cidade = int(input("Informe o codigo da cidade: "))
    numero_acidentes = int(input("Informe o numero de acidentes: "))
    numero_veiculos = int(input("Informe o numero de veiculos: "))

    if numero_veiculos > 2000:
        acidentes_2000.append(numero_acidentes)
        n_acidentes.append(numero_acidentes)
    else:
        n_acidentes.append(numero_acidentes)

    n_veiculos.append(numero_veiculos)
    codigo_cidades.append(codigo_cidade)

indice_acidente_maior = n_acidentes.index(max(n_acidentes))

print(f"""\n 
Menos acidentes
Quantidade de acidentes: {min(n_acidentes)}
codigo da cidade: {codigo_cidades[n_acidentes.index(min(n_acidentes))]}\n

Mais acidentes
Quantidade de acidentes: {max(n_acidentes)}
codigo da cidade: {codigo_cidades[n_acidentes.index(max(n_acidentes))]}\n

Media de veiculos 
Media de veiculos nas 5 cidades: {sum(n_veiculos) / len(n_veiculos)}\n

Media de acidentes
media de acidentes nas cidades com menos de 2000 veiculos: {sum(acidentes_2000) / len(acidentes_2000)}
""")