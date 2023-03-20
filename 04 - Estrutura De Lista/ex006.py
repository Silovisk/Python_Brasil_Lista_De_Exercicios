medias = []
numero_aprovados = 0

for i in range(1, 11):
    notas = [] # resetar notas dos alunos
    print(f"Digite as notas do {i}° Aluno")

    for i in range(1, 5):
        nota = float(input(f"Digite a {i}° nota: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    medias.append(media)

for media in medias:
    if media >= 7:
        numero_aprovados += 1

print(f"O número de alunos com média maior ou igual a 7.0 e igual a {numero_aprovados}")