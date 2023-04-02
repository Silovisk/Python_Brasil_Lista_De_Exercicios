numeros = []
numero = 0
contador = 1
quantidade_valores_acima_da_media = 0
quantidade_valores_abaixo_de_sete = 0

while numero != -1:
    numero = float(input(f"Inform e a {contador}° nota: "))
    numeros.append(numero)
    contador += 1

numeros_inverso = [numeros[i] for i in range(len(numeros) -1, -1, -1)]

media = sum(numeros) / len(numeros)

for num in numeros:
    if num > media:
        quantidade_valores_acima_da_media += 1
    if num < 7:
        quantidade_valores_abaixo_de_sete += 1

print(f"""
a - Valores lidos: {len(numeros)}
b - Valores na ordem: {numeros}
c - Valores inversos: {numeros_inverso}
d - Soma dos valores: {sum(numeros)}
e - Media dos valores: {media}
f - Quantidade valores acima da media: {quantidade_valores_acima_da_media}
g - Quantidade valores abaixo de sete: {quantidade_valores_abaixo_de_sete}
h - Programa encerrado..........
""")
