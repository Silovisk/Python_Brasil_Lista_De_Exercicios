import random

# Inicializa as variáveis
idades = []
alturas = []
soma_alturas = 0
count_alunos = 0

# Lê as idades e alturas dos 30 alunos
for i in range(30):
    #idade = int(input("Digite a idade do aluno {}: ".format(i+1)))
    #altura = float(input("Digite a altura do aluno {}: ".format(i+1)))

    idade = random.randint(10, 16)
    altura = random.uniform(1.50, 1.90)


    idades.append(idade)
    alturas.append(altura)

# Calcula a média de altura dos alunos com mais de 13 anos
count_idades = 0
for i in range(30):
    if idades[i] > 13:
        soma_alturas += alturas[i]
        count_idades += 1

if count_idades > 0:
    media_alturas = soma_alturas / count_idades
else:
    media_alturas = 0

# Conta quantos alunos com mais de 13 anos possuem altura inferior à média calculada
for i in range(30):
    if idades[i] > 13 and alturas[i] < media_alturas:
        count_alunos += 1

# Exibe o resultado
print("Quantidade de alunos com mais de 13 anos e altura inferior à média: ", count_alunos)
