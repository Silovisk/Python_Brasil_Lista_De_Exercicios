"""Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
 while alunos > 40:
    alunos = int(input("Numero de Alunos :")) 
"""

cont = 1
soma = 0
turma = int(input("Digite a Qtd de turmas :"))
while cont <= turma:
  alunos = int(input(f"Numero de Alunos na turma {cont}°:"))
  while alunos > 40:
    alunos = int(input(f"\n[Erro]\n\nNumero de Alunos na turma {cont}°:"))
  soma = soma + alunos
  cont = cont + 1
media = soma / turma
print(f"Media = {media}")