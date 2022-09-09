numero_alunos = []
altura_alunos = []

for i in range(10):
    n_aluno = int(input("Informe o numero do aluno: "))
    a_aluno = altura_alunos.append(float(input("Informe a altura do aluno: ")))
    numero_alunos.append(n_aluno)

print(f"Menor Aluno\n Numero: {numero_alunos[altura_alunos.index(min(altura_alunos))]} \n Altura: {min(altura_alunos)}\n")
print(f"Maior Aluno\n Numero: {numero_alunos[altura_alunos.index(max(altura_alunos))]} \n Altura: {max(altura_alunos)}")


    
