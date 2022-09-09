"""Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. """


soma = 0
n_pepols = int(input("Digite quantas pessoas :"))
for i in range(n_pepols):
  idade = int(input("Digite sua idade :"))
  soma = soma + idade

m = soma / n_pepols
print(f"Media = {m:.2f}")

if m >= 0 and m <= 25:
  print("Turma Jovem")
elif m >=26 and m <= 60:
  print("Turma Adulta")
elif m > 60:
  print("Turma Idosa")
else:
  print("Invalido")