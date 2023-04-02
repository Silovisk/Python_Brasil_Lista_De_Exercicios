carros = ["Fusca", "Corolla", "Gol", "Palio", "Civic", "HB20", "Uno", "Onix", "Celta", "Sandero"]

km_por_litro = [10.5, 12.3, 11.2, 10.8, 9.7, 13.2, 12.1, 11.5, 11.8, 12.5]

litros_por_mil_km = [] 
valor_mil_km_litro = []

valor_combustivel_economico = 0.0
carro_economico = ''

for i in range(len(carros)):
    print(f"""
    Veiculo {i+1}
    Nome: {carros[i]}
    Km por litro: {km_por_litro[i]}
    """)

    litros_por_mil_km.append(1000 / km_por_litro[i])
    valor_mil_km_litro.append(litros_por_mil_km[i] * 2.25)

print("+=+=+=+=+=+=++=+=+=+=+==+=+=+=+= Relatorio Final +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
print("N° carro\tNome\t\tKm Por litro\tLitros Por mil km\tValor")
for i in range(len(carros)):
    print(f"{i+1}\t\t{carros[i]}\t\t{km_por_litro[i]:.2f}Km\t\t{litros_por_mil_km[i]:.2f} litros\t\tR${valor_mil_km_litro[i]:.2f}")


# Pegando o modelo mais economico
valor_combustivel_economico = min(valor_mil_km_litro) # Acha o menor valor do vetor dos combustiveis
index_carro_economico = valor_mil_km_litro.index(valor_combustivel_economico) # Pega o index com base no valor do valor_combustivel_economico
carro_economico = carros[index_carro_economico] # Usa o index para achar o modelo mais economico

print(f"""
O menor consumo e do {carro_economico}
""")



