maior_eliminar = 0
soma = media = 0
menor_eliminar = 999999999

num_notas = 8

atleta = input("Digite o nome do atleta :")
for i in range(1,num_notas):
    voto = float(input(f"Nota {i}° jurado :"))

    if voto > maior_eliminar:
        maior_eliminar = voto

    if voto < menor_eliminar:
        menor_eliminar = voto

    soma += voto

soma = (soma - menor_eliminar) - maior_eliminar

media = soma / (num_notas-2)

print(f"Atleta: {atleta} ")
print(f"Melhor nota: {maior_eliminar}")
print(f"Menor nota: {menor_eliminar}")
print(f"Media = {media:.2f}")