saltos = []
nome = str(input("Digite seu Nome: "))

for i in range(1, 6):
    salto = float(input(f"Digite o {i}° Salto: "))
    saltos.append(salto)


print(f"""
Resultado final: 
Atleta: {nome}
Saltos: {saltos}
media: {sum(saltos) / len(saltos)} m
""")