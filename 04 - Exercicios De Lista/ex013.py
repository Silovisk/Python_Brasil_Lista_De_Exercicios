media_temperaturas = []
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'jul/ho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

for mes in meses:
    media = float(input(f"Digite a temperatura media do mes de {mes}: "))
    media_temperaturas.append(media)

media_anual = sum(media_temperaturas) / len(meses)

print(f"""
Media das temperaturas: {media_temperaturas}
Media anual: {media_anual}
""")