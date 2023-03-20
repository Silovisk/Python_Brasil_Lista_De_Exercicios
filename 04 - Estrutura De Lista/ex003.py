notas = []

for i in range(1, 5):
    nota = float(input(f"Digite a {i}° nota :"))
    notas.append(nota)

media = sum(notas)/len(notas)

print(f"A Media das notas {notas} e {media}")