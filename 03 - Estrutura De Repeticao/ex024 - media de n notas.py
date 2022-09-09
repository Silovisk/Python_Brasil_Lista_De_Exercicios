"""Faça um programa que calcule o mostre a média aritmética de N notas. """

cont = 1
soma = 0

n_ = int(input("Digite quantos notas quer colocar:"))
while cont <= n_:
  nota = float(input("Digite a {} nota: ".format(cont)))
  soma = soma + nota
  cont = cont + 1
media = soma / cont
print(f"A media e {media}")
